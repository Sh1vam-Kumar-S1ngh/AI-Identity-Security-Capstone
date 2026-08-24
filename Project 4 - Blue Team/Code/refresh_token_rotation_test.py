import requests
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

DOMAIN = "https://example-tenantt.us.auth0.com"
CLIENT_ID = "waWZTkVx1413jg5yajzYgCg6k5GrKV3C"
CLIENT_SECRET = "X9LgLOHCaGl0439luLB-V_2GbNcPKn07BQ8bg8BENEtdkO1GLfROovPRHi0X6Tqz"
AUDIENCE = "https://securenova-ai-api"
REDIRECT_URI = "http://localhost:3000/callback"

authorization_code = None


class CallbackHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global authorization_code

        query = parse_qs(urlparse(self.path).query)

        if "code" in query:
            authorization_code = query["code"][0]

            self.send_response(200)
            self.end_headers()
            self.wfile.write(
                b"Authorization successful. You can return to the terminal."
            )
        else:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Authorization failed.")

    def log_message(self, format, *args):
        return


print("=" * 60)
print("SECURENOVA PROJECT 4 - REFRESH TOKEN ROTATION TEST")
print("=" * 60)

auth_url = (
    f"{DOMAIN}/authorize?"
    f"response_type=code&"
    f"client_id={CLIENT_ID}&"
    f"redirect_uri={REDIRECT_URI}&"
    f"audience={AUDIENCE}&"
    f"scope=openid%20profile%20offline_access"
)

print("\nSTEP 1: Opening Auth0 authorization page...")
print("Please log in when the browser opens.")

webbrowser.open(auth_url)

server = HTTPServer(("localhost", 3000), CallbackHandler)

print("\nWaiting for authorization callback...")

while authorization_code is None:
    server.handle_request()

server.server_close()

print("AUTHORIZATION CODE: RECEIVED")

print("\nSTEP 2: Exchanging authorization code for tokens...")

response = requests.post(
    f"{DOMAIN}/oauth/token",
    data={
        "grant_type": "authorization_code",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": authorization_code,
        "redirect_uri": REDIRECT_URI
    }
)

print("TOKEN RESPONSE STATUS:", response.status_code)

if response.status_code != 200:
    print("ERROR:", response.text)
    exit()

tokens = response.json()

access_token = tokens.get("access_token")
refresh_token = tokens.get("refresh_token")

print("ACCESS TOKEN: RECEIVED")
print("REFRESH TOKEN: RECEIVED")

print("\nSTEP 3: Using refresh token for the first time...")

response = requests.post(
    f"{DOMAIN}/oauth/token",
    data={
        "grant_type": "refresh_token",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "refresh_token": refresh_token
    }
)

print("FIRST REFRESH STATUS:", response.status_code)

if response.status_code != 200:
    print("ERROR:", response.text)
    exit()

new_tokens = response.json()
new_refresh_token = new_tokens.get("refresh_token")

print("FIRST REFRESH: SUCCESS")
print("NEW REFRESH TOKEN: ISSUED")

print("\nSTEP 4: Replaying the OLD refresh token...")

response = requests.post(
    f"{DOMAIN}/oauth/token",
    data={
        "grant_type": "refresh_token",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "refresh_token": refresh_token
    }
)

print("OLD REFRESH TOKEN REPLAY STATUS:", response.status_code)

if response.status_code != 200:
    print("OLD REFRESH TOKEN REPLAY: REJECTED")
    print("REASON:", response.json().get("error_description", response.text))
else:
    print("OLD REFRESH TOKEN REPLAY: ACCEPTED")

print("\n" + "=" * 60)
print("REFRESH TOKEN ROTATION TEST COMPLETE")
print("=" * 60)
