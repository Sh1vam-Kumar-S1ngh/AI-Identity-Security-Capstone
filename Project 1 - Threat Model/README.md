# Project 1 — Threat Model

## Overview

This project develops a threat model for the SecureNova AI Identity System. The assessment identifies the identity types used by the platform, analyses identity flows using the STRIDE methodology, develops attack trees for key AI identity threats, evaluates risks, and maps an attack path to MITRE ATLAS.

## Identity Types

The threat model covers the following identity types:

* Human User
* AI Agent
* OAuth M2M Client
* LLM API Key
* RAG Pipeline Service Identity
* MCP Server Identity

The authentication mechanisms and privilege levels for these identities are represented in the identity-system data-flow model.

## Threat Modelling

The complete data-flow diagram was developed in OWASP Threat Dragon. It represents the user layer, agent layer, and internal API layer, with trust boundaries identified between the layers.

## STRIDE Analysis

The identity flows were assessed against all six STRIDE categories:

* Spoofing
* Tampering
* Repudiation
* Information Disclosure
* Denial of Service
* Elevation of Privilege

The project includes both the Threat Dragon threat analysis and the completed STRIDE threat matrix.

## Attack Trees

Three attack trees were developed in draw.io:

1. **LLM API Key Exfiltration** — exploitation of prompt injection to obtain an LLM API key.
2. **Agent Identity Spoofing** — spoofing an agent identity to obtain elevated API scope.
3. **RAG Chunk Poisoning** — manipulating retrieved knowledge chunks to influence AI-agent behaviour.

Each attack tree contains the defined attack goal and contributing attack paths.

## Risk Assessment

The identified threats were evaluated using:

**Risk Score = Likelihood × Impact**

The resulting threats were scored, ranked, and assigned to owners in the risk register.

## MITRE ATLAS Mapping

The attack paths were mapped to MITRE ATLAS techniques. The submitted evidence includes the MITRE ATLAS page for **AML.T0051 — LLM Prompt Injection**.

## Evidence

### Screenshots

The `screenshots/` directory contains the eight evidence screenshots in the required project sequence:

1. OWASP Threat Dragon — Complete AI Identity Data-Flow Diagram
2. OWASP Threat Dragon — STRIDE Threat Panel
3. Attack Tree 1 — LLM API Key Exfiltration
4. Attack Tree 2 — Agent Identity Spoofing
5. Attack Tree 3 — RAG Chunk Poisoning
6. Complete STRIDE Threat Matrix
7. Risk Register — Scored and Ranked Threats
8. MITRE ATLAS — AML.T0051 LLM Prompt Injection

### Documentation

The `documentation/` directory contains the final Project 1 submission PDF:

`Project-1-Threat-Model.pdf`

## Project Structure

```text
Project 1 - Threat Model/
├── README.md
├── documentation/
│   └── Project-1-Threat-Model.pdf
└── screenshots/
    ├── 01-threat-dragon-data-flow.png
    ├── 02-stride-threat-panel.png
    ├── 03-attack-tree-llm-api-key.png
    ├── 04-attack-tree-agent-spoofing.png
    ├── 05-attack-tree-rag-poisoning.png
    ├── 06-stride-threat-matrix.png
    ├── 07-risk-register.png
    └── 08-mitre-atlas-aml-t0051.png
```
