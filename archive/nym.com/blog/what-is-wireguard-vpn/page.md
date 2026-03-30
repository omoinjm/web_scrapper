Title: What is Wireguard VPN & how does it work?

URL Source: https://nym.com/blog/what-is-wireguard-vpn

Published Time: 2024-11-28

Markdown Content:
# What is Wireguard VPN& how does it work? - NymVPN
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

1.   [Blog](https://nym.com/blog)
2.   /
3.   What is Wireguard VPN & how does it work?

[Privacy](https://nym.com/blog/category/online-privacy)[VPN](https://nym.com/blog/category/vpn)

# What is Wireguard VPN & how does it work?

How the fastest VPN encryption protocol available works

[![Image 2: IMG_2055.jpg](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FIMG_2055_d742d5a7a3.jpg&w=1920&q=80)](https://nym.com/blog/author/casey-ford)

[Casey Ford, PhD](https://nym.com/blog/author/casey-ford)Communications Lead

[![Image 3: Ania-Piotrowska.jpg](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FAnia_Piotrowska_004ba9e050.jpg&w=1920&q=80)](https://nym.com/blog/author/ania-piotrowska)

[Ania M. Piotrowska, PhD](https://nym.com/blog/author/ania-piotrowska)Technical reviewer

June 1, 2024 11 mins read

Table of contents

 

![Image 4: Pablo: Improve quality](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FNym_encryption_b63c80ee08.webp&w=3840&q=75)

###### Share

Getting privacy and data security from a **Virtual Private Network (VPN)** might seem simple: turn it on, wait for a connection, and within seconds your IP address is hidden and data encrypted. Online anonymity, however, is far from magical. The technology under the hood of a VPN is a complex and multi-step process.

VPNs are primarily networks. But they run on **communication protocols** that take care of the multiple encryption stages so user data is secure in transit. **WireGuard** is a relatively new VPN encryption protocol, but it is by far the fastest available.

WireGuard’s speed comes from carefully chosen and efficient protocols for each step of the encryption process, and from its highly concise code-base. While it might not be the protocol being used by the majority of traditional VPNs, it has become the protocol of choice for new **decentralized VPNs (dVPNs)**. Many VPNs are now quickly following suit.

This article walks through the stages of WireGuard’s encryption process, its advantages and disadvantages, and how it uniquely powers the superior privacy features of dVPNs.

[![Image 5: Earlybird-email banner (1).webp](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FEarlybird_email_banner_1_5845915e2a.webp&w=3840&q=80)](https://nym.com/pricing?mtm_campaign=blog&mtm_content=wireguard&ncid=blog-wireguard&ref=blog)

[Try NymVPN for free today](https://nym.com/en/pricing?mtm_campaign=blog&mtm_content=wireguard&ncid=blog-wireguard&ref=blog)

## What is WireGuard VPN?

[WireGuard](https://www.wireguard.com/) is an open-source **communications protocol** which provides the encrypted routing procedures through which many modern VPNs [protect users’ data and privacy](https://nym.com/blog/what-is-internet-privacy). It uses state-of-art protocols for each stage of the public key cryptographic process, making it by far the fastest VPN protocol available.

WireGuard was [launched in 2015](https://www.businessinsider.com/wireguard-jason-a-donenfeld-profile-secure-vpn-linux-mac-windows-2021-1) before being released for Linux in 2020. It is now compatible with all major operating systems and devices, and has been increasingly adopted by new VPN services. Due to its high speed, open-source auditability, and low data overhead, it is expected that WireGuard may soon surmount more widely adopted communication protocols being used by mainstream VPNs.

Learn more about how data encryption works with [Nym’s comprehensive guide](https://nym.com/blog/what-is-encryption).

What is a VPN?

## How does the WireGuard VPN work?

WireGuard is a software client that runs on the user’s machine as well as the VPN or proxy server, allowing encrypted traffic to pass quickly and securely between them. So when you connect to a VPN server using the WireGuard protocol, here’s an idea of what’s going on in the background:

### Handshake

Before any exchange of keys or data, the client sends a request to the server, initiating what’s known as a handshake. The server responds by sending its public key to the client. WireGuard uses the Noise_IK handshake from Noise, which has a number of security and privacy benefits, such as avoiding key-compromise impersonation and replay attacks, obscuring the identities of handshakers, and perfect forward secrecy.

### Key exchange & derivation

The server and client then exchange public keys in order to verify each other’s identities. For key exchange, Wireguard uses Curve25519, a state-of-the-art elliptic curve cryptography based on the Diffie-Hellman public cryptography function.

The server and client use the exchanged keys to create a unique key known only to them. This is done through a Key Derivation Function (KDF). For the key derivation stage, WireGuard uses HKDF (or HMAC-based KDF) which is advantageous in VPN routing for its highly secure two-stage process and flexibility regarding key lengths. The derived key is used for symmetric encryption between the client and VPN server.

### Encryption & authentication

For the encryption and authentication stages, WireGuard uses ChaCha20-Poly1305 which is a combination of the ChaCha20 stream cipher and the Poly1305 message authentication code. This algorithm is highly performative and is generally faster than AES-GCM.

### Hashing

Hashing refers to the process in encrypted routing in which input data of any size is converted into a fixed-size string of characters. Once converted, the output date or “hash value” can be used to determine if the data packet has been manipulated or changed during transit. If so, the hash value will be different to the recipient than it was for the sender. WireGuard uses Blake2 for its hashing function, which is faster and more optimal than previous standards (e.g., Sha-1 and -2), and is considered to be as secure as advanced standards like Sha-3.

### Transport

The Transport Layer is responsible for turning the data of your traffic into encrypted packets to be sent over the web. WireGuard wraps the encrypted data using the User Datagram Protocol (UDP). This communications protocol allows for fast and secure data travel. It does not use TCP because it is less efficient on VPN networks, due to a larger data overhead and known problems (“TCP meltdowns”).

### Routing

Once your data has gone through this complex but highly efficient process of VPN encryption with WireGuard on your device, ensuring the authenticity of the intended recipient and the security of the data packets, it is then routed to the VPN server. There the IP address of your traffic is replaced with the VPN server’s own public IP.

### Decryption

Since it is the VPN server that provides the encryption for your data to their server, once there that layer of encryption is removed or decrypted using the above keys). However, assuming that the original connection from your device and intended recipient on the web is secured through HTTPS, one layer of encryption should remain, preventing the VPN from seeing your cleartext data. Once the VPN encryption is removed, the VPN will be able to see the final destination of where to send your data. With HTTPS encryption in place by default, your traffic will be encrypted from end-to-end by using a WireGuard powered VPN.

## WireGuard compatibility

WireGuard is sometimes criticized for its more limited compatibility compared with other protocols like OpenVPN. But this is largely exaggerated, referring to specific hardware compatibility (such as routers) and not operating systems.

*   Operating systems: WireGuard is compatible with most major operating systems and devices: Windows, Mac OS, Linux, Android, iOS, and modern versions of BSD.

*   Routers: One hardware issue with WireGuard is that it is not as widely compatible with many VPN routers as something like OpenVPN currently is. This is not unexpected since WireGuard has been on the market for only four years. As newer router hardware is released in coming years, Nym expects this compatibility gap to quickly close.

## WireGuard VPN advantages

### Speed

WireGuard is very fast as far as VPN communication protocols go, upwards of 50% faster than OpenVPN, which has been the industry standard for two decades. Minimal codebase

WireGuard’s code is remarkably slim, amounting to only 4,000 lines. For comparison, versions of OpenVPN have around 100,000 lines of code. This makes WireGuard’s performance extremely streamlined and efficient.

### High security

WireGuard uses state-of-the art encryption algorithms and public key cryptography for key exchanges. These encryption standards are at present unbreakable. Moreover, this concise and light code-base makes for a much smaller footprint for possible attacks, whereas unseen configuration errors with the more complex OpenVPN can lead to leaks or bigger attack vulnerabilities.

### Rapid reconnection

WireGuard is built to be stateless, meaning it doesn’t rely on maintaining a continuous connection state between peers. This design allows for seamless handling of disruptions because there’s no need to re-establish a session or connection state. As soon as packets start flowing again, WireGuard can pick up where it left off.

### Open source

WireGuard’s code is open source and thus available for anyone to audit. However, whether an open-source code is easily auditable depends on how large it is. In this regard, WireGuard is remarkable for the small and concise size of its codebase. This not only makes the protocol extremely streamlined, but allows for easier public audits.

## WireGuard VPN disadvantages

### Lack of obfuscation

WireGuard lacks built-in obfuscation. Designed as a simple, fast, and secure VPN protocol, it focuses on simplicity and performance. However, it does not include features for obfuscating traffic to hide the fact that a VPN is being used. This means that WireGuard traffic can be identified by network monitoring tools or by entities performing deep packet inspection (DPI).

Other tools can be used in conjunction with WireGuard, such as Obfsproxy, Shadowsocks, or Stunnel to add obfuscation to the VPN routing procedure.

### Not integrated into all VPNs

The majority of mainstream VPNs on the market are not yet using WireGuard, and have been using OpenVPN for decades. This simply means that WireGuard is comparatively less battle tested on the VPN front. However, this is rapidly changing as more and more VPNs are integrating with WireGuard.

### Lack of router support

WireGuard currently is not supported by nearly as many VPN routers as something like OpenVPN, mainly because these hardwares were designed and programmed before WireGuard’s emergence. Nym thus expects a shift in router compatibility for WireGuard in the coming years.

## WireGuard protocol vs. other VPN protocols

WireGuard is not the only communications protocol being used by VPNs on the market, and the differences between them can be significant for the VPN’s performance as well as user privacy.

### WireGuard vs. OpenVPN

OpenVPN is the communications protocol that is used by the large majority of VPNs on the market. It was introduced in 2001, making it the tried-and-tested industry standard for VPN encrypted routing. However, there are significant differences in performance between WireGuard and OpenVPN. Read Nym’s detailed comparison of the two protocols.

OpenVPN: Has the advantage of flexible configuration for users and programers, with a wide selection of encryption ciphers to use. It also has a much wider compatibility with VPN routers and is more common in enterprise setups.

WireGuard: Is much faster than OpenVPN, with a significantly smaller data overhead and equal security.

### WireGuard vs. IPSec/IKEv2

IPSec (Internet Protocol Security) and IKEv2 (Internet Key Exchange version 2) are protocols used to secure internet communications. They are often used together as IPSec/IKEv2.

IpSec/IKEv2: Like OpenVPN, it supports a wide range of cryptographic protocols, but it also has an extremely large data overhead, with a codebase in the hundreds of thousands of lines. This can make it prone to error and misconfiguration, as well as more difficult to audit.

WireGuard: Is simpler and efficient, but without the choice of encryption ciphers for users.

### WireGuard vs. PPTP

The Point-to-Point Tunneling Protocol (PPTP) is one of the oldest VPN encryption protocols. It was introduced in the mid-1990s by Microsoft and is still used by some legacy platforms.

PPTP: Uses MPPE (Microsoft Point-to-Point Encryption) with the RC4 cipher, which is considered weak by modern standards. However, it is relatively fast and easy to set up, so it might be useful in contexts where speed is a bigger concern than protection. WireGuard: Is not only extremely fast, but uses state-of-the-art encryption algorithms, making PPTP’s speed vs. security trade off completely unnecessary.

### WireGuard vs. L2TP

L2TP (Layer 2 Tunneling Protocol) is an extension of PPTP and L2F (Layer 2 Forwarding Protocol).

L2TP: L2TP itself does not provide encryption and so is often combined with IPsec to provide encryption and secure the data being transmitted (L2TP/IPsec).

WireGuard: Since L2TP doesn’t encrypt user data, comparing it with WireGuard isn’t useful.

## WireGuard: Expediting decentralized networks

When it comes to online privacy, what makes WireGuard such an exciting and important technology is its ability to provide fast and secure routing for privacy-focused decentralized VPNs (dVPNs).

The centralized and single-server architectures of traditional VPNs, on the one hand, have never been adequate privacy protections for users. They are vulnerable to data breaches, cooperation with mass surveillance requests, backdoors for advertisers, and data sales to brokers. On the other hand, dVPNs are promising, but speed is a problem. The more servers your data has to pass through to obscure your traffic, the slower everything is going to be. This might not be much of any issue for sending a confidential email, but it will be for comprehensive network routing.

WireGuard is a game-changing solution for privacy: it provides an extremely fast, efficient, and streamlined routing protocol so that users can profit from advanced privacy protections of a multi-hop dVPN without compromising too much on speed.

NymVPN has chosen to give users the choice. They can easily toggle to use a 2-hop dVPN mode powered by WireGuard for very fast and private day-to-day protections. Or, for highly sensitive use-cases (such as messaging and crypto-transactions), users can opt for the unparalleled 5-hop mixnet mode powered by the Sphinx protocol, which is specifically designed to handle mixnet traffic.

In choosing the best VPN for your privacy needs, consider how a decentralized network with WireGuard can make it so you don’t need to sacrifice your privacy to experience the internet easily and quickly.

## More than a VPN

Unlocking an Internet without surveillance

[Try NymVPN free](https://nym.com/pricing?mtm_campaign=blog&mtm_content=wireguard&ncid=blog-wireguard&ref=blog)

![Image 6](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2Fv3_iphone_2_c7eaff3b0b.svg&w=1200&q=80)

![Image 7](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FArtboard_1_2cedfda439.webp&w=3840&q=80)

### WireGuard: FAQs

### Why does WireGuard use static UDP ports, and how does that affect detectability?

WireGuard defaults to fixed UDP ports, simplifying routing but potentially making traffic more fingerprintable—though obfuscation plugins or integrated routing (like in NymVPN) can mask port behaviors.

### How does NymVPN's "tunnel‑in‑a‑tunnel" WireGuard implementation enhance anonymity?

NymVPN encloses a WireGuard-based 2-hop dVPN session inside its mixnet envelope, adding layers to hide metadata while preserving WireGuard’s speed for everyday browsing.

### How does rekeying work in WireGuard and why is it important for forward secrecy?

WireGuard regularly rotates session keys (via ChaCha20-Poly1305) after a short time or data volume, limiting the impact of key compromise and ensuring past sessions remain secure.

### Are there limitations in platform support or resource overhead for WireGuard on embedded devices?

WireGuard’s minimal codebase runs efficiently on Linux, macOS, Android, iOS and embedded devices—but on low-power hardware, key exchange overhead may introduce minor CPU load.

### How does WireGuard compare against other lightweight protocols in battery usage on mobile devices?

WireGuard is highly efficient and tends to consume less battery than heavier protocols like OpenVPN with TLS—with faster handshake performance reducing time the radio remains active.

## About the authors

![Image 8: IMG_2055.jpg](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FIMG_2055_d742d5a7a3.jpg&w=1920&q=80)

Casey Ford, PhD

Communications Lead

Casey is the Head of Communications, lead writer, and editorial reviewer at Nym. He holds a PhD in Philosophy and researches the intersection of decentralized technologies and social life.

![Image 9: Ania-Piotrowska.jpg](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FAnia_Piotrowska_004ba9e050.jpg&w=1920&q=80)

Ania M. Piotrowska, PhD

Technical reviewer

Ania is Nym's Chief Scientific Officer. She focuses on security, distributed systems, and anonymous communication, including onion routing and mix networks.

## Table of contents

*   [What is WireGuard VPN?](https://nym.com/blog/what-is-wireguard-vpn#what-is-wireguard-vpn)
*   [How does the WireGuard VPN work?](https://nym.com/blog/what-is-wireguard-vpn#how-does-the-wireguard-vpn-work)
*   [WireGuard protocols](https://nym.com/blog/what-is-wireguard-vpn#wireguard-protocols)
*   [WireGuard compatibility](https://nym.com/blog/what-is-wireguard-vpn#wireguard-compatibility)
*   [WireGuard VPN advantages](https://nym.com/blog/what-is-wireguard-vpn#wireguard-vpn-advantages)
*   [WireGuard VPN disadvantages](https://nym.com/blog/what-is-wireguard-vpn#wireguard-vpn-disadvantages)
*   [WireGuard protocol vs. other VPN protocols](https://nym.com/blog/what-is-wireguard-vpn#wireguard-protocol-vs-other-vpn-protocols)
*   [WireGuard: Expediting decentralized networks](https://nym.com/blog/what-is-wireguard-vpn#wireguard-expediting-decentralized-networks)
*   [WireGuard: FAQs](https://nym.com/blog/what-is-wireguard-vpn#wireguard-faqs)

## New low prices

The world's most private VPN

[Try NymVPN for free](https://nym.com/pricing?mtm_campaign=blog&mtm_content=get-nymvpn&ncid=blog-get-nymvpn&ref=blog)

## New low prices

The world's most private VPN

[Try NymVPN for free](https://nym.com/pricing?mtm_campaign=blog&mtm_content=get-nymvpn&ncid=blog-get-nymvpn&ref=blog)

## Keep Reading...

[![Image 10: Nym Connection Blog Image](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FVPN_2_85b5a04c09.svg&w=3840&q=80)](https://nym.com/blog/wireguard-live)

[Announcements](https://nym.com/blog/category/announcements)

### [NymVPN Fast Mode now powered by WireGuard](https://nym.com/blog/wireguard-live)

Advanced privacy with top speed

October 5, 2024 6 mins read

[![Image 11: Pablo: Improve quality](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FNym_encryption_b63c80ee08.webp&w=3840&q=80)](https://nym.com/blog/wireguard-vs-openvpn)

[Privacy](https://nym.com/blog/category/online-privacy)

### [WireGuard vs. OpenVPN](https://nym.com/blog/wireguard-vs-openvpn)

What makes them different, and which encryption protocol is the best?

May 11, 2024 16 mins read

[![Image 12: Pablo: Improve quality](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FNym_encryption_b63c80ee08.webp&w=3840&q=80)](https://nym.com/blog/encryption-and-data-protection)

[Privacy](https://nym.com/blog/category/online-privacy)

### [Encryption & data protection (all you need to know)](https://nym.com/blog/encryption-and-data-protection)

Explore how different types of VPNs use encryption to protect your data and privacy

May 16, 2024 17 mins read

[![Image 13: Pablo: Improve quality](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FNym_encryption_b63c80ee08.webp&w=3840&q=80)](https://nym.com/blog/what-is-encryption)

[Privacy](https://nym.com/blog/category/online-privacy)

### [What is encryption? A comprehensive guide](https://nym.com/blog/what-is-encryption)

Explaining the technology behind online data security, and its limits for privacy

May 9, 2024 13 mins read

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

### WireGuard protocols

| Encryption Step | Protocol |
| --- | --- |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |

Handshake

Noise

Key exchange

Curve25519

Key derivation

HKDF

Encryption

ChaCha20

Authentication

Poly1305

Hashing

Blake2s

Networking

UDP
