import requests
from datetime import datetime

API_URL = "http://localhost:3000/chat"
ROTATE_URL = "http://localhost:3000/rotate"

old_credential = "securenova-initial-credential"


def timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


print("=" * 65)
print("SecureNova AI - Credential Rotation & Replay Test")
print("=" * 65)

print(f"[{timestamp()}] Using initial credential")

response = requests.get(
    API_URL,
    headers={
        "Authorization": f"Bearer {old_credential}"
    }
)

print(
    f"[{timestamp()}] First authenticated call -> "
    f"{response.status_code} {response.reason}"
)

if response.status_code == 200:
    print("           Initial credential accepted")

print()
print(f"[{timestamp()}] Rotating credential...")

rotation_response = requests.post(ROTATE_URL)

if rotation_response.status_code == 200:
    print(
        f"[{timestamp()}] Credential rotated successfully"
    )

print()
print(f"[{timestamp()}] Replaying OLD credential...")

replay_response = requests.get(
    API_URL,
    headers={
        "Authorization": f"Bearer {old_credential}"
    }
)

print(
    f"[{timestamp()}] Replay old credential -> "
    f"{replay_response.status_code} {replay_response.reason}"
)

if replay_response.status_code == 401:
    print("           OLD credential rejected successfully")

print()
print("=" * 65)
print("Credential rotation / replay protection test complete")
print("=" * 65)