# Risk, Ethics, and Budget

## 1. Risk Register
1. Dataset quality risk
- Impact: high
- Mitigation: source verification and data cleaning checklist.

2. Model/runtime limitations
- Impact: medium
- Mitigation: lighter model fallback and batch experiment scheduling.

3. Cloud configuration/security issues
- Impact: high
- Mitigation: least-privilege IAM, firewall, TLS, key rotation.

4. Time overrun
- Impact: high
- Mitigation: strict milestones, weekly progress reviews.

## 2. Ethics
- Do not present generated responses as guaranteed truth.
- Include uncertainty messaging when evidence is absent.
- Avoid sensitive/private data without explicit approval.
- Document model limitations and failure cases.

## 3. Compliance and Governance
- Maintain source attribution for document-based answers.
- Keep experiment records for reproducibility.
- Respect data licensing and institutional policy.

## 4. Budget (Student-Friendly Estimate)
- Local development: mostly free.
- Cloud VM (short-term experiments): low to moderate.
- Optional API usage: variable based on token volume.
- Contingency: 10-15% of estimated compute cost.
