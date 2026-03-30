Title: Vulnerability disclosure policy and bug bounty program | Nym

URL Source: https://nym.com/vdp-bbp

Markdown Content:
Table of contents

Nym takes a multifaceted approach to external security, using continuous testing, vulnerability disclosure, a bug bounty program, and regular audits and penetration tests from external firms and our internal Security team.

## 1. Guidelines

To participate, you must follow these guidelines:

*   Do not download, modify, or destroy other users’ data.
*   Do not cause denial of service (DoS) through exploits, traffic, or provider issues.
*   Test only with your own account in production, or run your own instance of our open source code.
*   Social engineering, DDoS, physical access, and similar attacks are out of scope.
*   Only the first report of a unique issue is eligible for a payout.
*   Nym decides payouts, severity, classification, and eligibility.
*   Threats, ransom demands, or unprofessional language disqualify you.

## 2. How to report a vulnerability ?

*   Email: [security@nym.com](mailto:security@nym.com) (encrypt with our [PGP key](https://github.com/nymtech/nym/security/policy) if possible).
*   Keep reports confidential and include proof-of-concept code or screenshots if you can.
*   Provide a detailed technical description, including tools and steps to reproduce. Avoid using LLMs as they tend to be vague.
*   Attach images or documents with clear names; scripts or exploit code must be in non-executable formats.
*   We accept common file types and archives (zip, 7zip, gzip).
*   You may remain anonymous or provide contact info. We may request clarification.
*   By submitting, you affirm no IP rights violations and grant Nym the right to use your report internally for security purposes.

## 3. Vulnerability scope

Any significant vulnerability with enough detail and a proof-of-concept may be eligible. Once confirmed, we’ll work to fix it, and you agree to assist in testing fixes if needed.

### Eligible issues (examples)

*   Cross-Site Request Forgery (CSRF)
*   Cross-Site Scripting (XSS)
*   Code executions
*   SQL injection
*   Server-Side Request Forgery (SSRF)
*   Privilege escalations
*   Authentication bypasses
*   Data leaks

### Ineligible issues (examples)

*   Rate limiting
*   Stack traces
*   Self-XSS
*   Man in the Middle (MiTM) attacks
*   Denial of Service (DoS) attacks
*   Cache poisoning
*   Clickjacking
*   Missing DNS records
*   Brute force attacks
*   Vulnerabilities in third-party services or third-party platforms
*   Vulnerabilities in past versions of the software
*   Vulnerabilities affecting outdated browsers or operating systems
*   Vulnerabilities found in support services (e.g., Zendesk)

## 4. How do we evaluate vulnerabilities?

### 1. Initial review

We acknowledge reports within ~72 hours. We then attempt to reproduce and validate the issue. Reports that are non-reproducible, out of scope, duplicates, or already covered in past Nym audits may be closed without reward.

### 2. Severity assessment

*   Critical (CVSS 9.0-10.0): Direct user privacy compromise, VPN encryption bypass, or account takeover.
*   High (CVSS 7.0-8.9): Broad security flaws affecting many users, including data leaks.
*   Medium (CVSS 4.0-6.9): Conditional exploits that may still expose user information.
*   Low (CVSS 0.1-3.9): Minor, hard-to-exploit issues.
*   Informational (CVSS 0): Helpful findings, not true vulnerabilities.

### 3. Rewards and payouts

Rewards in NYM tokens are based on severity. Include your NYM address when submitting a report. You are responsible for taxes. Submissions from countries on prohibited lists (e.g. US sanctions) are ineligible.

Indicative rewards structure:

*   **Critical**: 10,000 USD worth of NYM tokens
*   **High**: 1,000 USD worth of NYM tokens
*   **Medium**: 200 USD worth of NYM tokens
*   **Low**: 50 USD worth of NYM tokens
*   **Informational**: May receive acknowledgment or a nominal reward.

### 4. Handling disputes

If you disagree with severity or a rejection, request clarification. We can reevaluate with new info. After reevaluation, the security team’s decision is final.

### 5. Public disclosure

We encourage coordinated disclosure after a fix is in place.

Do not publicly share details for 60 days after our acknowledgment, unless you coordinate with us.

We may inform affected vendors but will not share your identity without permission.

## 5. Safe Harbor Policy

We won’t pursue legal action against researchers who act in good faith, follow this policy, and avoid unnecessary harm or data access.

### Scope of Policy

We cannot bind third parties. If in doubt, contact us first.

### Information sharing policy

We may share non-identifying details of your report with affected third parties who commit not to take legal action against you. Identifying info is only shared with your permission.

### Possible exemptions

Good faith research that may violate certain terms can be exempt under safe harbor conditions.

### Nym’s legal commitments

Nym will not file civil or criminal actions against compliant researchers. Non-compliance may lead to exclusion or, in severe cases, legal action.

## Questions?

Email [security@nym.com](mailto:security@nym.com) with questions. If unsure about specific methods, ask before testing. Suggestions for improving this policy are welcome.
