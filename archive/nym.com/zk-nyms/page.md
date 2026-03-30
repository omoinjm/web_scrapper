Title: Zk-nyms: Zero-Knowledge Anonymous Credentials

URL Source: https://nym.com/zk-nyms

Markdown Content:
# Zk-nyms: Zero-Knowledge Credentials for Private Use | Nym
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

![Image 2: zk-nym.svg](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FZk_nyms_light_3ff344940d.svg&w=1200&q=80)

# Zk-nyms

Anonymous credentials that use zero-knowledge proofs so users can access digital apps and services without having to reveal sensitive information.

[Learn more](https://nym.com/docs/network/cryptography/zk-nym)

![Image 3: Zero-knowledge.svg](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FZero_knowledge_light_d2aa5ca905.svg&w=1200&q=80)

## What do zk-nyms do?

Accessing or paying for services online often requires us to reveal sensitive information about ourselves, and more than should be necessary. With zk-nym credentials, it is possible to anonymously prove your right to access digital services while retaining your privacy. Zk-nyms are the basis of NymVPN's anonymous credential system in which user payments can never be linked to their usage of the network. Zk-nyms can also be integrated to any service, such as e-cash, to delink clients' personal data from their authorized access.

### zk-nym use cases

![Image 4: mixnet_credential.svg](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2Fmixnet_credential_light_339dfc7f4d.svg&w=640&q=80)

### mixnet credential

Use and pay for the mixnet in a privacy preserving manner, ensuring wallet address and transaction history cannot be linked to your mixnet usage.

![Image 5: e-cash_payments.svg](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2Fe_cash_payments_LIGHT_1_8618d9ec03.svg&w=640&q=80)

### e-cash payments

Protect your privacy while paying online. The zk-nym scheme can be used for e-cash to ensure private financial transactions, also when paying via cryptocurrencies and utility tokens like NYM.

![Image 6: Data_sovereignty.svg](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FData_sovereignty_light_198b182c2f.svg&w=640&q=80)

### Data sovereignty

Prove attributes of your identity while retaining privacy. For example, prove you are above a certain age without revealing your actual birth date.

![Image 7: Private_authentication.svg](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FPrivate_authentication_light_c6dacbf224.svg&w=640&q=80)

### Private authentication

Sign in to digital services in a privacy preserving manner, ensuring that your information is delinked so you are not traced across apps, sites, and services.

### Getting zk-nyms

![Image 8](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FMixnet_859f5e974c_4148ed0243.svg&w=256&q=75)

### Issuance

You can request anonymous credentials from what are called “issuing authorities.” For the mixnet, the issuing authorities are the Nyx blockchain validators.

![Image 9](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FPrivacy_Enhanced_Payments_a2e61028ef_24e2db3a42.svg&w=256&q=75)

### Validation

The validators issue anonymous credentials that have “threshold issuance": they only hold part of the key of the credential and cannot piece together the full key to de-anonymize you.

![Image 10](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FEnjoy_f75a0bb6f8_f5e46b377c.svg&w=256&q=75)

### Use

You now have an anonymous credential that you can use to cryptographically prove something about yourself to a “verifier" or the given digital service you are trying to use.

### Privacy properties of zk-nyms

![Image 11: Threshold issuance.svg](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FThreshold_issuance_eb2e7832e6.svg&w=256&q=80)

### Threshold issuance

Validators only hold a part of the key that signs the credential. This has a similar byzantine-fault tolerance as other validator bases schemes: not only does it distribute trust but it also avoids “crush” of the system in case some validators go offline or are malicious.

![Image 12: Blind signatures.svg](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FBlind_signatures_9462670ca8.svg&w=256&q=80)

### Blind signatures

The property of blind issuance means that even if all the validators colluded, they would not be able to piece together the private attribute of your credential.

![Image 13: Unlinkable.svg](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FUnlinkable_413592deac.svg&w=256&q=80)

### Unlinkability

Once you have your credential, rest assured that the issuance of your credential and your subsequent showing of it is unlikable. Even if validators collude with the service to which you show your credential, they cannot learn any additional information.

![Image 14: Re-randomizable signatures.svg](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FRe_randomizable_signatures_169b752964.svg&w=256&q=80)

### Re-randomizable signatures

Signatures are re-randomizable, meaning you can use the credentials again without making these traceable and compromising privacy.

## Become unlinkable

With the world's most private VPN

[Try for free today](https://nym.com/pricing?mtm_campaign=core&mtm_content=zk-nyms&ncid=core-zk-nyms&ref=core)

![Image 15](https://nym.com/zk-nyms)

![Image 16](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FArtboard_1_2cedfda439.webp&w=3840&q=80)

![Image 17: Zk-diagram.svg](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FGroup_958df660c3.svg&w=3840&q=80)

## Build with zk-nym credentials

zk-nym credentials are available as an open source library with Nyx blockchain validators as issuing authorities.

The library makes zk-nyms available to everyone, with no work required by the end-user. Built on the Coconut credentials protocol, the first use-case is anonymous access credentials for the Nym mixnet.

[Read more](https://nym.com/docs/network/cryptography/zk-nym)

### Read more

[![Image 18: Nym Network Blog Image](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FNetwork_1_d56dcb6eb6.svg&w=3840&q=80)](https://nym.com/blog/zk-nyms-are-here-a-major-milestone-towards-a-market-ready-mixnet)

[Network](https://nym.com/blog/category/network)

### [zk-nyms are here — a major milestone towards a market-ready mixnet](https://nym.com/blog/zk-nyms-are-here-a-major-milestone-towards-a-market-ready-mixnet)

We recently announced zk-nyms to the world. zk-nyms are a cryptographic system that allows people to pay and use for services without…

March 22, 2023 6 mins read

[![Image 19: nym network.webp](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2Fnym_network_c423598300.webp&w=3840&q=80)](https://nym.com/blog/nyms-zero-knowledge-network)

[NymVPN](https://nym.com/blog/category/nymvpn)

### [Nym’s zero-knowledge network: No logging promises needed](https://nym.com/blog/nyms-zero-knowledge-network)

Turning a VPN no log’s policy into a network design and guarantee

October 31, 2024 11 mins read

[![Image 20: Nym Tokenomics Blog Image](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FArtboard_1_f28e67b69d.svg&w=3840&q=80)](https://nym.com/blog/the-nym-token-flow)

[Network,](https://nym.com/blog/category/network)[Web3 privacy](https://nym.com/blog/category/web3-privacy)

### [NYM token flow: Powering the most private network](https://nym.com/blog/the-nym-token-flow)

Delivering value to NymVPN users, operators, and builders

October 29, 2024 10 mins read

[![Image 21: Nym Tokenomics Blog Image](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FArtboard_1_f28e67b69d.svg&w=3840&q=80)](https://nym.com/blog/the-value-of-nym)

[Network,](https://nym.com/blog/category/network)[Web3 privacy](https://nym.com/blog/category/web3-privacy)

### [The Value of NYM: The spice powering our network](https://nym.com/blog/the-value-of-nym)

The real world value of the token behind NymVPN

September 22, 2024 12 mins read

### Frequently Asked Questions

### How do zk-nyms keep my NymVPN subscription private?

When you pay for a NymVPN subscription, your payment is converted to NYM tokens which are then used to issue you an anonymous zk-nym credential which your NymVPN app will use to access the network. While Nym Technologies will have access to your payment information, no one, not even Nym Technologies, will be able to connect this information to your access or use of the network. Your identity remains unlinkable to what you do online with NymVPN.

### Can I use zk-nyms to anonymize my payments online?

Currently zk-nyms are only being used to serve as proof of payment for the NymVPN app. However, zk-nyms can be integrated with generic e-cash payment systems to make transactions private and protect against cyber attacks to wallets. Nym is currently completing an integration for Z-Cash, but only using our the Nym Noise Generating Mixnet (NGM). Nym recommends Z-Cash currently for anonymous payments.

### Can zk-nyms protect my crypto transactions?

Currently, zk-nyms are only being used to serve as proof of payment for the NymVPN app using cryptocurrency. However, zk-nyms are built to defend any application, including cryptocurrencies and wallets. Wallet integrations in the future could use zk-nym technology as offline e-cash to enable better protection for cryptocurrencies like Bitcoin. Stay tuned!

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
