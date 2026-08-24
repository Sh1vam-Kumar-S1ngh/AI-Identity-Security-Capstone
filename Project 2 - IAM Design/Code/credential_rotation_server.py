from flask import Flask, request, jsonify
import secrets

app = Flask(__name__)

CURRENT_CREDENTIAL = "securenova-initial-credential"


@app.route("/chat")
def chat():
    global CURRENT_CREDENTIAL

    auth_header = request.headers.get("Authorization")

    if not auth_header or not auth_header.startswith("Bearer "):
        return jsonify({
            "status": 401,
            "message": "Unauthorized"
        }), 401

    credential = auth_header.split(" ", 1)[1]

    if credential != CURRENT_CREDENTIAL:
        return jsonify({
            "status": 401,
            "message": "Unauthorized - credential revoked"
        }), 401

    return jsonify({
        "status": 200,
        "message": "SecureNova AI Chat API accessed successfully"
    }), 200


@app.route("/rotate", methods=["POST"])
def rotate():
    global CURRENT_CREDENTIAL

    CURRENT_CREDENTIAL = secrets.token_urlsafe(24)

    return jsonify({
        "message": "Credential rotated successfully",
        "new_credential": CURRENT_CREDENTIAL
    }), 200


if __name__ == "__main__":
    app.run(port=3000, debug=False)