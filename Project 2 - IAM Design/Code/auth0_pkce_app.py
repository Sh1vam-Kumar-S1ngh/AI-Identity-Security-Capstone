from flask import Flask, redirect, request, session
import requests
import secrets
import hashlib
import base64

app = Flask(__name__)
app.secret_key = "securenova-lab-secret"

AUTH0_DOMAIN = "example-tenantt.us.auth0.com"
CLIENT_ID = "waWZTkVx1413jg5yajzYgCg6k5GrKV3C"
CLIENT_SECRET = os.getenv("AUTH0_CLIENT_SECRET")
API_AUDIENCE = "https://securenova-ai-api"
REDIRECT_URI = "http://localhost:3000/callback"


@app.route("/")
def home():
    return '<a href="/login">Login with Auth0</a>'


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

    auth_url = (
        f"https://{AUTH0_DOMAIN}/authorize"
        f"?response_type=code"
        f"&client_id={CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        f"&scope=openid%20profile%20email%20read%3Aai-data"
        f"&audience={API_AUDIENCE}"
        f"&code_challenge={code_challenge}"
        f"&code_challenge_method=S256"
    )

    return redirect(auth_url)


@app.route("/callback")
def callback():
    code = request.args.get("code")

    if not code:
        return "Authorization failed."

    code_verifier = session.get("code_verifier")

    if not code_verifier:
        return "Code verifier not found."

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

        return (
            "Authentication successful!<br><br>"
            "Access token received successfully.<br><br>"
            '<a href="/test-api">Test API</a>'
        )

    return f"Status: {response.status_code}<br><br>{response.text}"


@app.route("/chat")
def chat():
    auth_header = request.headers.get("Authorization")

    if not auth_header:
        return "Missing Authorization header", 401

    if not auth_header.startswith("Bearer "):
        return "Invalid Authorization header", 401

    return "SecureNova AI Chat API accessed successfully."


@app.route("/test-api")
def test_api():
    access_token = session.get("access_token")

    if not access_token:
        return "No access token found. Login first."

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
        port=3000,
        debug=True
    )