# Project 2 — Auth0 Implementation

## Overview

This project implements identity and access management for the SecureNova AI platform using Auth0. The implementation covers OAuth 2.0 with PKCE, API scopes, JWT validation, MFA, attack protection, credential rotation, and Auth0 Actions.

## Project Objectives

- Configure an Auth0 tenant for the SecureNova AI platform.
- Register a Regular Web Application and an M2M application.
- Configure OAuth 2.0 Authorization Code with PKCE.
- Configure `read:ai-data` and `write:admin` API scopes.
- Validate JWT access tokens.
- Configure TOTP-based MFA.
- Enable Brute-Force Protection and Suspicious IP Throttling.
- Implement credential rotation and expired-token replay protection.
- Add an `agent_id` custom claim using an Auth0 Post-Login Action.

## Evidence

### Screenshots

| # | Evidence | File |
|---|---|---|
| 01 | Auth0 Applications — Web and M2M Applications | `01-auth0-applications.png` |
| 02 | Auth0 API — Custom Scopes | `02-auth0-api-scopes.png` |
| 03 | jwt.io — Decoded JWT Claims | `03-jwt-decoded.png` |
| 04 | Auth0 Universal Login — Custom Branding | `04-universal-login-branding.png` |
| 05 | Auth0 MFA — TOTP Challenge | `05-mfa-totp.png` |
| 06 | Auth0 Actions — Post-Login Custom Claim | `06-auth0-post-login-action.png` |
| 07 | Auth0 Attack Protection Configuration | `07-attack-protection.png` |
| 08 | Credential Rotation and Token Replay Test | `08-credential-rotation.png` |

### Documentation

The complete project evidence is available in:

`Documentation/Project 2 — Auth0 Implementation.pdf`

## Code

The implementation and testing code is provided in the `Code/` directory.

### `auth0_pkce_app.py`

Implements the OAuth 2.0 Authorization Code with PKCE flow, including authorization redirect, callback handling, token acquisition, and authenticated API access.

### `auth0_jwt_validation_app.py`

Implements JWT validation using Auth0 JWKS and verifies the token signature, audience, issuer, and expiration before allowing API access.

### `credential_rotation_server.py`

Provides the local API endpoints used to demonstrate credential rotation and rejection of a revoked credential.

### `credential_rotation_test.py`

Tests the credential lifecycle by performing an authenticated request, rotating the credential, and replaying the old credential to verify that it receives `401 Unauthorized`.

## Project Structure

```text
Project 2 - IAM Design/
├── README.md
├── Code/
│   ├── auth0_pkce_app.py
│   ├── auth0_jwt_validation_app.py
│   ├── credential_rotation_server.py
│   └── credential_rotation_test.py
├── Documentation/
│   └── Project 2 — Auth0 Implementation.pdf
└── Screenshots/
    ├── 01-auth0-applications.png
    ├── 02-auth0-api-scopes.png
    ├── 03-jwt-decoded.png
    ├── 04-universal-login-branding.png
    ├── 05-mfa-totp.png
    ├── 06-auth0-post-login-action.png
    ├── 07-attack-protection.png
    └── 08-credential-rotation.png