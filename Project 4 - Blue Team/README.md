# Project 4 — Blue Team: Guardrails, Hardening and Detection

## Overview

This project implements defensive controls for the SecureNova AI system to mitigate the attacks demonstrated during the Red Team assessment.

The implementation focuses on guardrail-based attack blocking, sensitive JWT redaction, cryptographic agent-message integrity, Auth0 token lifecycle protection, and anomaly detection.

## Defensive Controls

### 1. Guardrail Blocking

Attack payloads are tested against the implemented guardrails to verify that malicious inputs are detected and blocked before reaching the AI system.

### 2. JWT Detection and Redaction

JWT-like credentials are detected using pattern matching and redacted to prevent sensitive identity information from being exposed in model inputs or outputs.

### 3. Agent Message Integrity

Ed25519 public/private key cryptography is used to verify the authenticity and integrity of agent messages.

Tampered messages are rejected when signature verification fails.

### 4. Auth0 Token TTL and Refresh Rotation

Short-lived access-token configuration and refresh-token rotation are used to reduce the impact of compromised credentials and prevent replay of previously used refresh tokens.

### 5. Anomaly Detection

Anomaly detection is implemented to identify suspicious AI identity activity and generate alerts when attack-like behavior is detected.

### 6. Before/After Attack Comparison

The project compares attack behavior before and after defensive controls are applied to demonstrate the effectiveness of the implemented Blue Team measures.

## Evidence

The `Screenshots/` directory contains the evidence collected during implementation:

1. Guardrail blocking attack payloads
2. JWT regex detection and guardrail redaction
3. Ed25519 key-pair generation
4. Tampered agent message rejection
5. Auth0 token TTL and refresh-token rotation
6. Rejection of an old refresh token
7. Anomaly detection alert
8. Before/after attack comparison

## Code

The `Code/` directory contains the Python scripts used to implement and test the defensive controls.

Key components include:

- Guardrail attack-payload testing
- JWT redaction testing
- Ed25519 agent-message signing and verification
- Auth0 refresh-token rotation testing
- Anomaly detection
- Before/after attack comparison

## Documentation

The complete project evidence and results are available in:

`Documentation/Project 4 - Blue Team - Guardrails, Hardening and Detection.pdf`

## Project Structure

```text
Project 4 - Blue Team/
├── README.md
├── Code/
│   ├── agent_public_key.pem
│   ├── agent_signature_test.py
│   ├── anomaly_detection.py
│   ├── before_after_comparison.py
│   ├── generate_keys.py
│   ├── guardrail_test.py
│   ├── jwt_redaction_test.py
│   └── refresh_token_rotation_test.py
├── Documentation/
│   └── Project 4 - Blue Team - Guardrails, Hardening and Detection.pdf
└── Screenshots/
    ├── SS1_Guardrail_Blocking_Attack_Payloads.png
    ├── SS2_JWT_Regex_Output_Guardrail_Redaction.png
    ├── SS3_Ed25519_Key_Pair_Generation.png
    ├── SS4_Tampered_Agent_Message_Rejected.png
    ├── SS5_Auth0_Token_TTL_Refresh_Rotation_1.png
    ├── SS5_Auth0_Token_TTL_Refresh_Rotation_2.png
    ├── SS6_Auth0_Old_Refresh_Token_Rejected.png
    ├── SS7_Anomaly_Detection_Alert.png
    └── SS8_Before_After_Attack_Comparison.png