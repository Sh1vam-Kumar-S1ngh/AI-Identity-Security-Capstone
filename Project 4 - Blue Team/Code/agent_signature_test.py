from cryptography.hazmat.primitives import serialization

print("=" * 60)
print("SECURENOVA PROJECT 4 - AGENT MESSAGE SIGNATURE TEST")
print("=" * 60)

with open("agent_private_key.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(
        f.read(),
        password=None
    )

with open("agent_public_key.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

original_message = b"Approve customer support request CS-1001"

signature = private_key.sign(original_message)

print("\nORIGINAL MESSAGE:")
print(original_message.decode())

print("\nSIGNATURE CREATED:")
print("Ed25519 signature generated successfully.")

try:
    public_key.verify(signature, original_message)
    print("ORIGINAL MESSAGE: VERIFIED")
except Exception:
    print("ORIGINAL MESSAGE: REJECTED")

tampered_message = b"Approve customer support request CS-1002"

print("\nTAMPERED MESSAGE:")
print(tampered_message.decode())

print("\nVERIFICATION RESULT:")

try:
    public_key.verify(signature, tampered_message)
    print("TAMPERED MESSAGE: VERIFIED")
except Exception:
    print("ERROR: Ed25519 signature verification failed")
    print("TAMPERED MESSAGE: REJECTED")
    print("REASON: Message integrity check failed")

print("\n" + "=" * 60)
print("SIGNATURE VERIFICATION TEST COMPLETE")
print("=" * 60)
