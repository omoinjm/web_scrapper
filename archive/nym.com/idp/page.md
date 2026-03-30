Title: Incident disclosure policy | Nym

URL Source: https://nym.com/idp

Markdown Content:
# Incident disclosure policy | Nym
![Image 1](https://nym.com/icons/nym-logo-new.svg)

[](https://nym.com/ "Home")

NymVPN

[Pricing](https://nym.com/pricing)

Download

Ecosystem

Resources

Blog

[Login](https://nym.com/account/login)[Get NymVPN](https://nym.com/pricing)

[](https://nym.com/ "Home")

[Login](https://nym.com/account/login)

### Incident disclosure policy

Table of contents

 

## How Nym Technologies SA responds to security incidents

_v1.0 as of 14 November 2025_

## I. Nym's commitments

**Transparency in real-time:** We believe privacy requires trust, and trust requires transparency. When incidents occur, whether security breaches or operational disruptions, we communicate quickly, clearly, and honestly with our community.

**User above all:** Every decision in our incident response process prioritizes user security and privacy.

## II. Types of incidents we disclose

We classify incidents into two categories:

1.   **Security and operational incidents** (immediate public disclosure required)
2.   **Internal issues** (no public disclosure required)

### Security and Operational Incidents (immediate disclosure)

1.   **Security incidents** involve the potential compromise of user data, privacy, or cryptographic systems:

*   User credentials, payment data, or personally identifiable information exposed or at risk
*   Compromise of cryptographic keys enabling traffic decryption
*   Breach of core infrastructure (authentication, payment systems, zk-nym issuance)
*   Zero-day vulnerabilities actively being exploited
*   Any incident requiring user action to maintain security

1.   **Operational incidents** are service disruptions (connectivity, performance, availability):

*   NymVPN connectivity problems or gateway unavailability
*   API or infrastructure outages preventing connections
*   Network performance degradation
*   Third-party infrastructure failures affecting service

**Disclosure requirement:** Immediate

**Note:** Security incidents require immediate user action and detailed impact assessment. Operational incidents are inconvenient but don't compromise privacy.

### Internal issues (no public disclosure)

Issues resolved before user impact include:

*   Vulnerabilities discovered and fixed pre-production
*   Operational improvements during routine maintenance
*   Configuration errors caught in audits with no exploitation
*   Internal security hardening

**Documentation:** Internal knowledge base only

## III. Nym's approach to disclosure

1.   **Disclose fast:** Operational incidents disclosed same-day with precise timestamps
2.   **Explain technically:** Clear root cause analysis without jargon
3.   **Credit our users:** Acknowledge users who report issues (Telegram, support channels)
4.   **Clarify architecture:** Distinguish between decentralized network and centralized services
5.   **Reassure privacy:** Explicitly state what privacy guarantees remain intact
6.   **Share fixes:** Detail remediation steps and prevention measures

## IV. Format for incident reports

Based on our actual practice, every incident report includes:

### Headline summary

A clear description of what happened and its current status

### Timeline

Precise timestamps (UTC) to explain

1.   When users first experienced issues
2.   When Nym team became aware
3.   When service was restored

### Root cause

Technical explanation of what went wrong, including:

1.   **For security issues:** Attack vector and how it occurred
2.   **For operational issues:** Infrastructure component that failed

### Architecture context

Clarification of which systems were affected:

*   **Decentralized network** (600+ independent nodes) and/or
*   **Centralized services** (account management, payments, API)

### Privacy impact assessment

*   What user data/activity was potentially affected
*   What privacy guarantees remained intact

### User and community acknowledgment

Credit given to users who reported the issue

### Remediation actions

*   Immediate fixes deployed
*   Additional resources or infrastructure changes
*   Long-term prevention measures

### What users should do

Including clear actions (even if it's "no action required")

## V. Communication channels

How we notify users:

*   Prominent banner on nym.com and in our [Help Center](https://support.nym.com/)
*   Real-time updates on [Discord](https://nym.com/go/discord), [Telegram](https://nym.com/go/telegram), and [X](https://nym.com/go/x)
*   Real-time status on our [Status](https://status.nymtech.net/status/mainnet) page
*   Post-event blog post on our [Blog](https://nym.com/blog) (incident report series)
*   In-app notifications (when possible)
*   Additional email notification (if we have user emails)

We often learn about issues from our community (Discord, support tickets, Telegram, X) and we acknowledge them by name in our reports. This creates a feedback loop that helps us respond faster.

## VI. Decentralized architecture disclosures

We clearly distinguish in every incident report:

*   **Centralized NymVPN** services: Account management, payments API, etc.
*   **Decentralized Nym network:** 600+ independent node operators running gateways and mix nodes, and doing distributed zk-nym credential issuance

**Why this matters:**

*   API outages affect login/connection but don't compromise privacy of existing connections
*   Network node issues are localized to specific operators
*   We cannot control node operators (the network is designed to penalize repeatedly bad performing node operators)

**Note:** users need to know that infrastructure outages don't compromise the fundamental privacy architecture. Our **zero-knowledge credential system** means:

*   Payments remain unlinkable to VPN usage
*   Even if centralized API fails, privacy guarantees persist
*   Multi-layer encryption remains intact

## VII. Post-incident actions

### Immediate (0-24 hours)

*   Restore service
*   Deploy emergency fixes

### Short-term (1-7 days)

*   Publish incident report on our Blog
*   Implement monitoring improvements

### Long-term (ongoing)

*   Architecture improvements to prevent recurrence
*   Enhanced automation for faster recovery

## VIII. Vulnerability Disclosure Policy & Bug Bounty Program

Please refer to our [policy and program](https://nym.com/vdp-bbp).

## Table of contents

*   [How Nym Technologies SA responds to security incidents](https://nym.com/idp#how-nym-technologies-sa-responds-to-security-incidents)
*   [I. Nym's commitments](https://nym.com/idp#i-nym's-commitments)
*   [II. Types of incidents we disclose](https://nym.com/idp#ii-types-of-incidents-we-disclose)
*   [III. Nym's approach to disclosure](https://nym.com/idp#iii-nym's-approach-to-disclosure)
*   [IV. Format for incident reports](https://nym.com/idp#iv-format-for-incident-reports)
*   [V. Communication channels](https://nym.com/idp#v-communication-channels)
*   [VI. Decentralized architecture disclosures](https://nym.com/idp#vi-decentralized-architecture-disclosures)
*   [VII. Post-incident actions](https://nym.com/idp#vii-post-incident-actions)
*   [VIII. Vulnerability Disclosure Policy & Bug Bounty Program](https://nym.com/idp#viii-vulnerability-disclosure-policy--bug-bounty-program)

### Nym incident reports

[![Image 2: NymVPN App Blog Image](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FVPN_1_5be0fcfc43.svg&w=3840&q=80)](https://nym.com/blog/incident-report-22-may-2025)

[NymVPN](https://nym.com/blog/category/nymvpn)

### [Incident report: NymVPN connectivity problem on 22 May 2025](https://nym.com/blog/incident-report-22-may-2025)

Results of fixes to NymVPN network connections

May 26, 2025 2 mins read

[![Image 3: Nym Blog Announcement](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FAnnouncements_1_201d679715.svg&w=3840&q=80)](https://nym.com/blog/incident-report-13-september-2025)

[Announcements,](https://nym.com/blog/category/announcements)[NymVPN](https://nym.com/blog/category/nymvpn)

### [Incident report: NymVPN connectivity problem on 13 September 2025](https://nym.com/blog/incident-report-13-september-2025)

What happened this weekend on the Nym network explained, and how we're preventing it in the future

September 16, 2025 2 mins read

[![Image 4: Pablo: Convert to webp.svg](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FNym_World_1_bcaaef7fac.svg&w=1920&q=80)](https://nym.com/blog/incident-report-21-june-2025)

[Announcements,](https://nym.com/blog/category/announcements)[NymVPN](https://nym.com/blog/category/nymvpn)

### [Incident report: Network outage morning of 21 June 2025](https://nym.com/blog/incident-report-21-june-2025)

All network operations and app connections now resolved

June 21, 2025 2 mins read

[![Image 5: Nym Blog Announcement](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FAnnouncements_1_201d679715.svg&w=3840&q=80)](https://nym.com/blog/incident-report-11-july-2025)

[Announcements,](https://nym.com/blog/category/announcements)[NymVPN](https://nym.com/blog/category/nymvpn)

### [Incident report: NymVPN gateway unavailability on 11–12 July 2025](https://nym.com/blog/incident-report-11-july-2025)

What you need to know about what happened and how the Nym team resolved it

July 15, 2025 2 mins read

## Nym Newsletter

​

- [x] I agree to the processing of my personal data in accordance with the[Privacy Policy](https://nym.com/nym-com-privacy-statement) 

[](https://nym.com/go/telegram "Telegram")[](https://nym.com/go/x "Twitter")[](https://nym.com/go/discord "Discord")[](https://nym.com/go/github "GitHub")[](https://nym.com/go/youtube "YouTube")[](https://nym.com/go/matrix "Matrix")

### About

*   [Nym's whitepaper ↗](https://nym.com/nym-whitepaper.pdf)
*   [NymVPN litepaper](https://nym.com/nymvpn-litepaper)
*   [NymVPN public roadmap ↗](https://trello.com/b/qVhBo3e2/nymvpn-public-roadmap)
*   [Status of Nym services ↗](https://status.nymtech.net/status/mainnet)

### Downloads

*   [NymVPN for Android](https://nym.com/download/android)
*   [NymVPN for iOS](https://nym.com/download/ios)
*   [NymVPN for Linux](https://nym.com/download/linux)
*   [NymVPN for macOS](https://nym.com/download/macos)
*   [NymVPN for Windows](https://nym.com/download/windows)

### Blog

*   [Announcements](https://nym.com/blog/category/announcements)
*   [NymVPN](https://nym.com/blog/category/nymvpn)
*   [Community](https://nym.com/blog/category/community)
*   [Network](https://nym.com/blog/category/network)
*   [Privacy](https://nym.com/blog/category/blog-category)

### Resources

*   [Nym Docs](https://nym.com/docs)
*   [Support ↗](https://support.nym.com/)
*   [Trust Center](https://nym.com/trust-center)
*   [Forum ↗](https://forum.nym.com/)
*   [GitHub repository ↗](https://github.com/nymtech)

### Company

*   [About](https://nym.com/about)
*   [Contact](https://nym.com/contact)
*   [Press](https://nym.com/press)
*   [Merch ↗](https://nym.shop/)
*   [Careers ↗](https://nym.teamtailor.com/)

*   [Imprint](https://nym.com/imprint)
*   [nym.com privacy statement](https://nym.com/nym-com-privacy-statement)
*   [NymVPN terms of use](https://nym.com/vpn-terms)
*   [NymVPN apps privacy statement](https://nym.com/vpn-privacy-statement)
*   [Nym Operators and Validators terms](https://nym.com/operators-validators-terms)
*   [Anonymous usage data](https://nym.com/anonymous-stats)
*   [Vulnerability disclosure and bug bounty](https://nym.com/vdp-bbp)
*   [Incident disclosure policy](https://nym.com/idp)

WireGuard is a registered trademark of Jason A. Donenfeld© 2025 Nym Technologies SA. All rights reserved.
