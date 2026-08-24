print("=== PROJECT 3 — CVSS FINDINGS TABLE ===")
print()

print(f"{'FINDING':<8} {'ATTACK':<35} {'SCORE':<8} {'VECTOR'}")
print("-" * 115)

print(f"{'1':<8} {'Indirect Prompt Injection':<35} {'9.6':<8} {'CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:L'}")
print(f"{'2':<8} {'Agent Identity Spoofing':<35} {'8.6':<8} {'CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:N/I:H/A:N'}")
print(f"{'3':<8} {'System Prompt Extraction':<35} {'7.7':<8} {'CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:L/I:L/A:N'}")
print(f"{'4':<8} {'Prompt-Based Privilege Escalation':<35} {'3.8':<8} {'CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N'}")
print(f"{'5':<8} {'RAG Poisoning and MCP Abuse':<35} {'9.1':<8} {'CVSS:3.1/AV:N/AC:L/PR:N/UI:S/C:H/I:H/A:N'}")

print()
print("=== ALL 5 FINDINGS RECORDED ===")
