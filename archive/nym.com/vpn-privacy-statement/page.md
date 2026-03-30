Title: NymVPN apps Privacy Statement | Nym

URL Source: https://nym.com/vpn-privacy-statement

Markdown Content:
Table of contents

_Updated 28 January 2026_

**Privacy by design** is Nym’s guiding principle. NymVPN is designed with the aim of building privacy _directly into the software_ instead of relying on promises and policies. This prevents Nym or any third parties from ever having access to information about users that could connect their personal identifying information with their online activities.

To provide a good quality of service, **anonymized NymVPN performance metrics** and **billing information** may be collected, processed, or stored. This information is used solely to improve and deliver NymVPN services, manage billing, or if you have explicitly consented to collection of it by **enabling telemetry features**.

This privacy policy provides **transparency** on such data processing and applies to **NymVPN apps only**. For privacy details related to the **nym.com** website, please [read here](https://nym.com/nym-com-privacy-statement).

## I. Nym’s legal jurisdiction

When choosing a VPN provider, it is important to note who they are and the jurisdiction in which they are based. Any VPN provider is subject to the data protection and privacy laws of that country.

**Nym Technologies SA** (hereafter **Nym**) is a Swiss company established under the laws of Switzerland, and registered with the business registry of the Canton of Neuchâtel in Switzerland with number **CHE-367.426.629**. Its primary product is a **Virtual Private Network (VPN)** service named **NymVPN.** Nym considers itself the **data controller** of any personal data it processes about you.

In this policy we explain, in accordance with the legal regulations of the [Swiss Federal Act on Data Protection](https://www.edoeb.admin.ch/en/basic-knowledge) (“FADP”), how Nym Technologies and any trusted third parties process your data.

## II. No logs network

NymVPN is a **decentralized VPN (dVPN)**. The app sends your internet traffic through a **network of independently operated servers** across the world that are **not under the direct control of Nym**. To be part of the Nym network, these operators must sign a legal agreement **obliging them to abstain from gathering logs of user traffic**.

NymVPN is designed to make it very difficult to track your usage both for those operators and for Nym itself. Thanks to decentralization, even if logs were to kept on a node in violation of Nym’s contractual obligation for operators, **you remain unlinkable to your activity**. Linking you to your activity online would require that the entry and exit nodes you are using to both (a) break their no logging commitments and (b) collude.

You can read more on [Nym node operator Terms and Conditions](https://nym.com/operators-validators-terms).

### III. Purpose limited payments

Nym **payment processing** has been designed with the **principle of _purpose limitation_**. This means your payment information is used solely for processing payments, _nothing else_.

To achieve this, NymVPN uses a **zero-knowledge credential system** called [zk-nyms](https://nym.com/zk-nyms). Users can purchase a NymVPN subscription with many payment types, from fiat with debit and credit cards to cryptocurrency. To ensure that this **payment information remains unlinkable to app usage**, zk-nyms are created on blockchain as anonymous access credentials from a successful payment. Zk-nyms contain no personal identifying information and are fully anonymous, even to Nym itself.

### 1. Crypto currency payments

Nym processes crypto payments using our **self-hosted BTCPay server**, an open source cryptocurrency payment processor which does not log IP addresses, as well as **custom payment processors** that only process data from public blockchains including the [Nyx public blockchain](https://nym.com/network).

### 2. Third-party payment providers

To process debit and credit card payments, NymVPN uses these **third-party payment services**:

*   **Stripe** for desktop apps
*   **Apple Pay** for in-app purchases on mobile
*   **Google Play** for in-app purchases on mobile

When paying through one of these third-party payment providers, the following personal data may be exposed and collected by these providers:

*   Name and the email address you use
*   Debit/credit card number
*   Contact information
*   Geographic information

In this event, **zk-nyms** on Nym’s side ensure this information cannot be linked to your usage of the NymVPN app.

### 3. Anonymous payments with privacy-oriented cryptocurrencies

If you are paying for NymVPN with Zcash (privacy settings enabled), Monero, Dash, or Litecoin MWEB, there is no processing of personal financial information because of built-in privacy and anonymity properties of these payment methods.

### 4. Cash payments

No personal identifying information is requested with this payment method.

## IV. Anonymous performance data

NymVPN collects anonymized usage data to understand app reliability, performance, and user experience. This data is collected in two distinct ways, each with different purposes and safeguards.

1.   **Share error reports** (via Sentry, a third-party telemetry service)
2.   **Share usage analytics** (via the NymVPN app)

**These are turned off by default**. If you enable these features to help NymVPN, **you can turn them off at any time.**

**If you choose to disable both these, Nym will not have access to data coming from your NymVPN app.**

### 1. Error and performance monitoring via Sentry

NymVPN uses Sentry in a standard, industry-common way to monitor application health. **No direct identifiers (such as IP addresses, account identifiers) are intentionally collected**. Sentry data is used solely for debugging and performance analysis, not for tracking individual users.

Sentry is embedded in the app as a lightweight SDK that automatically observes:

*   application crashes and unhandled errors
*   freezes or hangs
*   performance issues (slow startup, slow UI actions, failed background tasks)
*   high-level device and app context (operating system, app version)

When an error or performance issue occurs, the app sends a structured error report to Sentry. This report helps us:

*   identify where users encounter errors
*   detect regressions after updates
*   monitor overall stability and reliability
*   understand performance bottlenecks across platforms

### 2. Custom app statistics collector

In addition to Sentry, NymVPN includes a custom-built statistics collector embedded directly in the VPN client. This collector gathers general, high-level usage metrics, such as:

*   operating system and app version
*   preferred mode (Fast and Anonymous)
*   session characteristics (duration, graceful termination vs. error)
*   time required to establish a connection
*   exit node preferences and general connectivity behaviour

This data helps us:

*   evaluate performance and reliability of design decisions
*   detect systemic issues or shortcomings
*   understand how users configure and use the app
*   Prioritise improvements and infrastructure investments (e.g. where to support node operators)

**Critically:** All data collected by the custom statistics collector is transmitted exclusively through the active VPN tunnel. As a result:

*   we do not see the client’s IP address
*   we cannot link statistics to an account, identity, or network location
*   we cannot correlate usage data with external identifiers

The collected metrics are therefore **anonymous by design and cannot be used to identify individual users**.

## V. Purposes of data processing

We have only one reason for processing your NymVPN app data: to enable you to successfully use NymVPN. Data processing for this purpose includes:

*   **Routing your internet traffic**, as described in §II
*   **Managing payments** for our services, as described in §III
*   **Measuring its quality and security**, as described in §IV
*   **Providing customer support:** Issues and tickets raised by you via our customer support channel, along with any personal data you include in those tickets (such as name and email address) may be processed by Nym and **Zendesk** on behalf of Nym for the limited purpose of solving any issues you have using the NymVPN app.

## VI. Nym’s strict policy on third-party data sharing

We may provide limited and anonymous data to parties for the sole purpose of optimizing our services, execute the contractual agreement with you, or to parties with whom we are legally obliged to share the data. This includes:

1.   **Node operators**, which have a contractual obligation towards Nym to respect the confidentiality of NymVPN traffic as described in §II
2.   Our **payment processors** as stated in §III
3.   When enabled, our telemetry service Sentry which is used to improve app performance, as described in §IV
4.   **Zendesk**, when you use Nym customer support, as described in §V

### Clarification on cross-border data transfers

Nym is based in Switzerland, which means that it is not in the European Union (the “EU”) or the European Economic Area (the “EEA”). The European Commission has deemed the Swiss data protection regulations to be adequate and vice versa, despite it being a third country from a EU/EEA-perspective.

For some of the third-party service providers like third-party payment providers such as Stripe, we may transfer your data to other third countries. Given that some third-party countries may not have an adequate level of protection for your personal data, we enter only into agreements with such third parties if they adhere to voluntary schemes that ensure a level of personal data protection that is deemed adequate by the European Commission.

However, as noted earlier, in cases where the use of the NymVPN involves exit nodes outside the EEA, this may result in your data being handled by parties in a third country. This is inherent to the service and meets the derogation of **article 17 sub b FADP**. However, the **decentralized nature of the Nym network ensures that any data exposed to one node is fundamentally incomplete.**At all points on the network, your IP address is never connected with the final destination on the Internet.

While Nym is legally obligated to comply with lawfully issued requests about its services from Swiss authorities, NymVPN and the network are designed to ensure that Nym never has access to information that could link any personally identifying information, such as payment data, to use of NymVPN or the Nym network.

In the event that Nym receives a request from Swiss authorities demanding user data, Nym will challenge requests to the fullest extent permitted by Swiss law and will make such requests public. Other countries’ authorities are not competent to demand data from Nym.

## VII. How long your data is stored

The following retention policies apply for anonymous data collected from your use of the NymVPN app:

*   **Entry and exit server operators:** NymVPN sends your traffic through independently operated entry and exit servers. These operators are third-party service providers who are contractually obliged to respect the confidentiality of your communications. The Nym network is designed explicitly to prevent Nym and any other entity from controlling these service providers, thereby preventing centralized data collection. This also means Nym cannot enforce data access requests and audits of these servers.
*   **Internal accounting:** Pursuant to Swiss law, the accounting books and records, as well as the accounting vouchers together with the annual report and the audit report, will be _retained for ten years_. The retention period begins on expiry of the respective financial year.
*   **Payment processors:** Stripe will generally keep personal data received from us for _at least five years_ from the end of the business relationship with us or the date of the last transaction, whichever is later.
*   **Telemetry services:** When you enable Sentry, our telemetry tool, we retain some usage metrics for _approximately 90 days_ to perform (historical) analyses. This data is pseudonymized.

Once these retention periods expire, the personal data will be either deleted or fully anonymized.

## VIII. Your data protection rights

We would like to make sure you are fully aware of all your data protection rights. If Nym holds personal data about you under the FADP, you have rights including:

*   **The right to be informed:** You have the right to be informed of the collection and processing of your personal data.
*   **The right of access:** You have the right to copies of your personal data from Nym. We may charge you a small fee for this service.
*   **The right to rectification:** You have the right to request that Nym correct any information that you believe is inaccurate. You also have the right to request that Nym complete information you believe is incomplete.
*   **The right to erasure:** You have the right to request that Nym erase your personal data under certain circumstances.
*   **The right to restrict processing:** You have the right to request that Nym restrict the processing of your personal information in certain circumstances.
*   **The right to object to processing:** You have the right to object to the processing of your personal data under certain circumstances.

Nym will try to respond to your request **within 30 days**. We may ask you to verify your account before executing your request. If your request is difficult to process, we may need more time to comply with your request and may delay the execution of your request.

Keep in mind that Nym may not be able to fulfill all requests given the low-level of already pseudo- or fully anonymized data linkable to any particular user. This results from designed limitation of information access on Nym’s part which is in the interest of protecting the privacy of users to begin with.

## IX. Changes to our VPN privacy statement

Nym keeps this Privacy Policy under regular review and reserves the right to amend it without prior notification. If we change this Statement, we will inform you on our website and via our newsletter.

If you have any questions about this Statement, the personal data we hold of you, or if you would like to exercise one of your data protection rights in §VIII, please do not hesitate to contact us through:

1.   **[Our contact page](https://nym.com/contact)** available on our website
2.   **Our email address** for legal inquiries: [legal@nym.com](mailto:legal@nym.com)
3.   **Our address:** Nym Technologies SA, place Numa-Droz 2, 2000 Neuchâtel, Switzerland

Should you wish to report a complaint or if you feel that we have not addressed your concern in a satisfactory manner, you may contact the supervisory authority. The supervisory authority for data protection in Switzerland is the **Federal Data Protection and Information Commissioner (“FDPIC”)**. For further information, please consult the [contact form of the FDPIC](https://www.edoeb.admin.ch/edoeb/de/home/deredoeb/kontakt.html).

## XII. Governing law

Switzerland
