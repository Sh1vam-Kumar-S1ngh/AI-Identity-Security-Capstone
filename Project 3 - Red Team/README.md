# Project 3 — Red Team: AI Identity Attacks

## Overview

This project performs a Red Team security assessment of an AI identity system. The assessment focuses on AI-specific identity and agent security threats, including indirect prompt injection, agent identity spoofing, system prompt extraction, RAG poisoning, and MCP abuse.

Successful attacks are evaluated using CVSS 3.1 and mapped to the closest MITRE ATLAS technique.

## Attack Scenarios

### 1. Indirect Prompt Injection — OWASP LLM01

A simulated identity credential (fake JWT) is embedded in the agent's system context. Multiple payloads are hidden inside documents read by the agent, and the attack attempts to exfiltrate the credential without the user explicitly requesting it.

### 2. Agent Identity Spoofing — OWASP LLM09

A two-agent setup is used to craft a message that convinces Agent B that it originated from a trusted orchestrator. The attack demonstrates Agent B executing a privileged action that it should refuse under the correct identity context.

### 3. System Prompt Extraction — OWASP LLM07

Five system prompt extraction techniques are tested:

- Repeat-back
- Role-play override
- Translation trick
- Ignore-prior-instruction
- Suffix injection

Each technique is logged together with the complete model response. An attempt is also made to elevate from a user role to an admin role through prompt engineering alone.

### 4. RAG Poisoning and MCP Abuse

A malicious instruction is injected into the simulated RAG knowledge base. The assessment verifies whether the agent retrieves and acts upon the poisoned content and simulates an MCP tool call triggered by the poisoned chunk.

### 5. CVSS Scoring and MITRE ATLAS Mapping

Every successful attack is assessed using the CVSS 3.1 calculator. The complete CVSS vector string is recorded, and each finding is mapped to the closest MITRE ATLAS AML.TXXXX technique.

## Evidence

The project contains eight screenshots documenting the required evidence:

1. **Indirect Prompt Injection** — Simulated JWT token exposed through an indirect injection.
2. **Agent Identity Spoofing** — Agent B executing a privileged action after receiving a spoofed orchestrator message.
3. **System Prompt Extraction** — Partial system prompt content exposed through an extraction technique.
4. **RAG/MCP Poisoning** — Model response showing the malicious injected instruction being acted upon.
5. **CVSS 3.1 Score** — Highest-severity finding with all CVSS vector components completed.
6. **MITRE ATLAS Mapping** — MITRE ATLAS AML.TXXXX technique page for a mapped finding.
7. **CVSS Findings Table** — All five attacks scored with their corresponding CVSS vector strings.
8. **Attack Success Matrix** — Percentage success rate for each attack category before defensive controls.

## Deliverables

The project includes:

- Red Team assessment documentation
- Evidence screenshots
- CVSS 3.1 findings and vector strings
- MITRE ATLAS technique mappings
- Attack success analysis
- Executive summary
- One finding page per attack
- Top three hardening recommendations

## Project Structure

Project 3 - Red Team/
├── README.md
├── Documentation/
└── Screenshots/
