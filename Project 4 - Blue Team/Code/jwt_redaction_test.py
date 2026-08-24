import re

model_response = """
The customer authentication token is:
eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJTRUNVUkVOT1ZBLURFTU8ifQ.signature123
"""

jwt_pattern = r"\b[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\b"

print("=" * 60)
print("SECURENOVA PROJECT 4 - JWT OUTPUT GUARDRAIL")
print("=" * 60)

print("\nMODEL RESPONSE BEFORE GUARDRAIL:")
print(model_response)

if re.search(jwt_pattern, model_response):
    print("JWT-SHAPED CREDENTIAL DETECTED")

    redacted_response = re.sub(
        jwt_pattern,
        "[REDACTED]",
        model_response
    )

    print("\nGUARDRAIL ACTION: REDACTED")
    print("\nMODEL RESPONSE AFTER GUARDRAIL:")
    print(redacted_response)
else:
    print("NO JWT-SHAPED CREDENTIAL DETECTED")

print("=" * 60)
