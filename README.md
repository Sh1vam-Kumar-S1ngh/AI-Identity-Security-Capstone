# AI Identity Security Capstone

## Overview

This repository contains the complete AI Identity Security Capstone, covering the design, implementation, testing, Red Team assessment, Blue Team defenses, and security policy and compliance work.

The capstone applies identity security principles to AI systems, including authentication, authorization, agent identity, credential protection, threat modeling, attack simulation, defensive guardrails, monitoring, incident response, and compliance.

## Projects

### Project 1 — Threat Model

Threat modeling of the AI Identity Security architecture using STRIDE, attack trees, risk analysis, and MITRE ATLAS mapping.

**Includes:**
- Threat model documentation
- Data-flow and threat-model evidence
- STRIDE threat analysis
- Attack trees
- Risk register
- MITRE ATLAS mapping

---

### Project 2 — IAM Design

Implementation of an AI identity and access-management design using Auth0.

**Includes:**
- Auth0 application configuration
- API scopes
- PKCE authentication
- JWT validation
- Universal Login configuration
- MFA/TOTP
- Auth0 Post-Login Action
- Attack protection
- Credential rotation and replay protection
- Python implementation files
- Implementation evidence

---

### Project 3 — Red Team

Red Team assessment of AI identity security controls and AI-specific attack scenarios.

**Includes:**
- Indirect prompt injection
- Agent identity spoofing
- System prompt extraction
- RAG poisoning
- MCP abuse
- CVSS 3.1 assessment
- MITRE ATLAS mapping
- Attack findings
- Attack success analysis
- Red Team evidence and documentation

---

### Project 4 — Blue Team

Implementation of defensive controls to mitigate the attacks identified during the Red Team assessment.

**Includes:**
- Guardrail-based attack blocking
- JWT detection and redaction
- Ed25519 agent-message signing and verification
- Auth0 token TTL and refresh-token rotation
- Replay protection
- Anomaly detection
- Before/after attack comparison
- Python security testing scripts
- Defensive-control evidence

---

### Project 5 — Policy, Compliance and Summary

Final governance and policy layer consolidating the AI Identity Security capstone.

**Includes:**
- AI Identity Security Policy
- Incident Response Playbook
- NIST AI RMF compliance mapping
- OWASP LLM Top 10 compliance mapping
- GitHub repository evidence
- Contribution history
- Risk Priority Matrix
- Top 5 security recommendations
- Final project documentation

## Repository Structure

```text
AI-Identity-Security-Capstone/
│
├── README.md
│
├── Project 1 - Threat Model/
│   ├── README.md
│   ├── documentation/
│   └── screenshots/
│
├── Project 2 - IAM Design/
│   ├── README.md
│   ├── Code/
│   ├── Documentation/
│   └── Screenshots/
│
├── Project 3 - Red Team/
│   ├── README.md
│   ├── Code/
│   ├── Documentation/
│   └── Screenshots/
│
├── Project 4 - Blue Team/
│   ├── README.md
│   ├── Code/
│   ├── Documentation/
│   └── Screenshots/
│
└── Project 5 - Policy/
    ├── README.md
    ├── Documentation/
    └── Screenshots/