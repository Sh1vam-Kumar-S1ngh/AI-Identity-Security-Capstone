from flask import Flask, redirect, request, session
import requests
import secrets
import hashlib
import base64
import jwt
from jwt import PyJWKClient
from urllib.parse import urlencode
from datetime import datetime

app = Flask(__name__)

app.secret_key = "securenova-lab-secret"

AUTH0_DOMAIN = "example-tenantt.us.auth0.com"

CLIENT_ID = "waWZTkVx1413jg5yajzYgCg6k5GrKV3C"

CLIENT_SECRET = os.getenv("AUTH0_CLIENT_SECRET")

API_AUDIENCE = "https://securenova-ai-api"

REDIRECT_URI = "http://localhost:3000/callback"

ISSUER = f"https://{AUTH0_DOMAIN}/"

JWKS_URL = f"https://{AUTH0_DOMAIN}/.well-known/jwks.json"

jwks_client = PyJWKClient(JWKS_URL)


@app.route("/")
def home():
    return """
    <h1>SecureNova AI Chat</h1>
    <a href="/login">Login with Auth0</a>
    """


@app.route("/login")
def login():

    code_verifier = secrets.token_urlsafe(64)

    session["code_verifier"] = code_verifier

    challenge = hashlib.sha256(
        code_verifier.encode()
    ).digest()

    code_challenge = base64.urlsafe_b64encode(
        challenge
    ).decode().rstrip("=")

    params = {
        "response_type": "code",
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "scope": "openid profile email read:ai-data",
        "audience": API_AUDIENCE,
        "code_challenge": code_challenge,
        "code_challenge_method": "S256"
    }

    auth_url = (
        f"https://{AUTH0_DOMAIN}/authorize?"
        + urlencode(params)
    )

    return redirect(auth_url)


@app.route("/callback")
def callback():

    code = request.args.get("code")

    if not code:
        return "Authorization failed.", 401

    code_verifier = session.get("code_verifier")

    if not code_verifier:
        return "Code verifier not found.", 400

    token_url = f"https://{AUTH0_DOMAIN}/oauth/token"

    response = requests.post(
        token_url,
        json={
            "grant_type": "authorization_code",
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "code": code,
            "redirect_uri": REDIRECT_URI,
            "code_verifier": code_verifier
        }
    )

    if response.status_code == 200:

        token_data = response.json()

        session["access_token"] = token_data["access_token"]

        return """
        <h2>Authentication successful!</h2>

        <p>Access token received successfully.</p>

        <a href="/test-api">Test API</a>
        """

    return (
        f"Status: {response.status_code}"
        f"<br><br>"
        f"{response.text}"
    )


@app.route("/chat")
def chat():

    auth_header = request.headers.get("Authorization")

    if not auth_header:
        return "Unauthorized: Missing Authorization header", 401

    if not auth_header.startswith("Bearer "):
        return "Unauthorized: Invalid Authorization header", 401

    token = auth_header.split(" ", 1)[1]

    try:

        signing_key = jwks_client.get_signing_key_from_jwt(token)

        payload = jwt.decode(
            token,
            signing_key.key,
            algorithms=["RS256"],
            audience=API_AUDIENCE,
            issuer=ISSUER
        )

        return (
            "SecureNova AI Chat API accessed successfully."
            "<br><br>"
            "JWT validation successful."
        )

    except jwt.ExpiredSignatureError:

        return "Unauthorized: Access token expired.", 401

    except jwt.InvalidAudienceError:

        return "Unauthorized: Invalid audience.", 401

    except jwt.InvalidIssuerError:

        return "Unauthorized: Invalid issuer.", 401

    except jwt.InvalidTokenError:

        return "Unauthorized: Invalid access token.", 401

    except Exception as e:

        return f"Unauthorized: {str(e)}", 401


@app.route("/test-api")
def test_api():

    access_token = session.get("access_token")

    if not access_token:
        return "No access token found. Login first.", 401

    API_URL = "http://localhost:3000/chat"

    response = requests.get(
        API_URL,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )

    return (
        f"Status: {response.status_code}"
        f"<br><br>"
        f"{response.text}"
    )


if __name__ == "__main__":

    app.run(
        host="localhost",
        port=3000,
        debug=True
    )