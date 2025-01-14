# Copyright 2023 Infleqtion
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import base64
import hashlib
import os
import webbrowser
from multiprocessing import Queue

import requests
import uvicorn
from fastapi import APIRouter, FastAPI, Request
from fastapi.responses import RedirectResponse

from oqtant.settings import Settings
from oqtant.util.server import ThreadServer

settings = Settings()

app = FastAPI(title="Login API", openapi_url="/openapi.json")
router = APIRouter()


def generate_random(length: int) -> str:
    return base64.urlsafe_b64encode(os.urandom(length)).decode("utf-8").replace("=", "")


verifier = generate_random(80)


def generate_challenge(verifier: str) -> str:
    hashed = hashlib.sha256(verifier.encode("utf-8")).digest()
    return base64.urlsafe_b64encode(hashed).decode("utf-8").replace("=", "")


def get_authentication_url(auth_server_port: int):
    code_challenge = generate_challenge(verifier)
    auth_url = "".join(
        [
            f"{settings.auth0_base_url}/authorize",
            "?response_type=code",
            f"&scope={settings.auth0_scope}",
            f"&audience={settings.auth0_audience}",
            f"&code_challenge={code_challenge}",
            "&code_challenge_method=S256",
            f"&client_id={settings.auth0_client_id}",
            f"&redirect_uri=http://localhost:{auth_server_port}",
        ]
    )
    return auth_url


queue = Queue()


@app.get("/")
async def main(request: Request, code):
    resp = await get_token(verifier, code, request.url.port)
    token = resp["access_token"]
    queue.put({"token": token})
    if token:
        return "Successfully authenticated, you may close this tab now"
    else:
        return "Failed to authenticate, please close this tab and try again"


@app.get("/login")
def login(request: Request):
    return RedirectResponse(
        url=get_authentication_url(auth_server_port=request.url.port)
    )


async def get_token(verifier: str, code: str, auth_server_port: int):
    url = f"{settings.auth0_base_url}/oauth/token"
    headers = {"content-type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "authorization_code",
        "client_id": settings.auth0_client_id,
        "code_verifier": verifier,
        "code": code,
        "redirect_uri": f"http://localhost:{auth_server_port}",
    }
    resp = requests.post(
        url, headers=headers, data=data, allow_redirects=False, timeout=(5, 30)
    )
    return resp.json()


def get_user_token(auth_server_port: int = 8080) -> str:
    """A utility function required for getting Oqtant authenticated with your Oqtant account.
       Starts up a server to handle the Auth0 authentication process and acquire a token.
    Args:
        auth_server_port (int): optional port to run the authentication server on
    Returns:
        str: Auth0 user token
    """
    allowed_ports = [8080, 8081, 8082, 8083, 8084, 8085]
    if auth_server_port not in allowed_ports:
        raise ValueError(f"{auth_server_port} not in allowed ports: {allowed_ports}")
    server_config = uvicorn.Config(
        app=app, host="localhost", port=auth_server_port, log_level="error"
    )
    server = ThreadServer(config=server_config)
    with server.run_in_thread():
        webbrowser.open(f"http://localhost:{auth_server_port}/login")
        token = queue.get(block=True)
    return token["token"]
