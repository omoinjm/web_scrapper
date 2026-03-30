Title: Future-proofing privacy: Nym's roadmap to post-quantum security

URL Source: https://nym.com/blog/nym-post-quantum-roadmap

Published Time: 2025-04-04

Markdown Content:
At Nym, we’ve always believed that real privacy isn’t just about what works today — it’s about anticipating tomorrow. Security and privacy threats don’t stand still, and neither does Nym.

As the cryptographic landscape evolves, we’re taking steps to future-proof the Nym network and NymVPN to ensure users stay protected not just now, but for years to come. That’s why we’re already laying the groundwork to bring **post-quantum security** to both the Nym network and [NymVPN](https://nym.com/).

## What is post-quantum cryptography?

### Quantum computing

**Quantum computers** are a new kind of computer that harnesses the principles of quantum mechanics to solve certain problems much more efficiently than classical computers. Although they are still in their early stages, with limited scale and capabilities today, they have the potential to break the mathematical assumptions underlying many existing cryptographic systems. In particular, quantum computing is expected to become capable of factoring the large numbers that most [modern cryptography](https://nym.com/blog/what-is-encryption) is built on!

### Post-quantum cryptography

**Post-quantum cryptography (PQC)** refers to a new generation of cryptographic algorithms designed to remain secure against both conventional and quantum computers. **PQC** does this by changing the fundamental mathematical assumptions to ones where quantum computers do not seem to have any advantage over modern computers. While the cryptographic building blocks widely used today — such as **key exchange protocols** and **digital signatures** — are effective against classical computers, they would be vulnerable to **quantum attacks** in the future unless the underlying algorithm is changed.

**PQC** introduces alternatives that are resilient to both classical and quantum adversaries. Importantly, these new algorithms are designed to run on today’s hardware, making early adoption both feasible and practical.

## The shift to post-quantum cryptography starts now

Every generation of cryptography eventually faces the same reality: what was once considered secure begins to show cracks. While quantum computers are still developing, the **need to modernize cryptography** is essential for long-term security. Thankfully, the resources to do so are already here.

### The post-quantum data crisis

One of the more pressing reasons to start planning today for a **post-quantum world** is the long-term **sensitivity of encrypted data**. Even if large-scale quantum computers capable of breaking current cryptographic schemes don’t yet exist, adversaries can already collect and store encrypted communications with the goal of decrypting them in the future. This strategy is often referred to as **“harvest now, decrypt later.”** We know that many governments (and increasingly private companies) are capable of recording almost every encrypted packet sent over the Internet, and it is precisely to counter this threat that Nym built a [Noise Generating Mixnet](https://nym.com/mixnet) (NGM).

Yet the danger is that a powerful adversary like the NSA — even if they do not have a quantum computer today — will eventually get one. This will allow them to decrypt the massive amount of encrypted messages they have been recording for years. For individuals and organizations handling data that needs to remain private for years or decades, adopting post-quantum protections early is not just forward-thinking — it’s a vital necessity.

### Preparing for post-quantum encryption

The shift toward modern cryptography isn’t just theoretical — it’s already underway. In 2024, the U.S. National Institute of Standards and Technology (NIST) [set a formal timeline](https://nvlpubs.nist.gov/nistpubs/ir/2024/NIST.IR.8547.ipd.pdf) for phasing out widely used cryptographic algorithms, including **RSA** and **Elliptic Curve Cryptography (ECC)**. These algorithms are scheduled to be deprecated over the next several years, with a complete transition required by 2035 — a major milestone in the evolution of digital security standards.

In parallel, the **standardization of post-quantum cryptographic algorithms** is actively underway. Some candidates — such as **CRYSTALS-Kyber (ML-KEM)** for key establishment and **CRYSTALS-Dilithium (ML-KEM), FALCON, and SPHINCS+ (SLH-DSA)** for digital signatures — have already been [selected for standardization](https://csrc.nist.gov/news/2022/pqc-candidates-to-be-standardized-and-round-4#fourth-round). Others are still [under evaluation in ongoing rounds](https://csrc.nist.gov/projects/pqc-dig-sig). This marks a significant step toward ensuring cryptographic resilience in the face of both current and emerging technological capabilities.

## Nym’s approach to post-quantum security

At Nym, we’re taking a careful and forward-looking approach to **integrating post-quantum cryptography across the entire ecosystem** — from internal node communications to end-user connections and core protocol layers. We’re actively collaborating with [leading experts](https://nym.com/about) in post-quantum cryptography to ensure this transition is done right, balancing privacy, performance, and long-term resilience.

Rather than rushing to implement the latest cryptographic trend, we’re building a solid foundation for future-proof privacy. Our roadmap toward post-quantum security begins with establishing modern secure communication channels and then incrementally layering in quantum-resistant key exchange at every level of the Nym architecture. When selecting post-quantum algorithms, we are carefully evaluating a range of well-studied options, including those standardized by NIST. Our goal is to adopt robust and thoroughly analyzed schemes, and where appropriate, to use hybrid approaches. This ensures that the security of **our system does not rely on the strength of a single cryptographic primitive alone**.

## Nym’s roadmap for post-quantum protections

With NymVPN, you have a choice between two modes: a **2-hop Fast Mode** and the 5-hop [Anonymous Mode](https://nym.com/blog/anonymous-mode-in-nymvpn) using the Noise Generating Mixnet. Both rely on robust, modern [cryptographic primitives](https://nym.com/trust-center/cryptography). In the **Fast Mode**, client traffic is protected using the [AmneziaWG protocol](https://nym.com/blog/introducing-amneziawg-for-nymvpn) which ensures efficient, authenticated encryption and secure communication between the user and the exit gateway. In Anonymous Mode, traffic is encapsulated using the [Sphinx cryptographic packet format](https://nym.com/blog/sphinx-the-anonymous-data-format-behind-lightning-and-nym) to provide strong metadata protection.

Underlying these protocols are **cryptographic key exchange mechanisms** which are critical for establishing secure, forward-secret communication. That’s why one of our major goals this year is to introduce **post-quantum secure key exchange** across the Nym stack, ensuring long-term resilience against both classical and quantum adversaries.

### Post-quantum security for the Nym network

Building on the foundation of the [Noise Protocol](http://www.noiseprotocol.org/), we plan to integrate a post-quantum secure key exchange into the Noise-based communication channels between mix nodes. This will ensure that messages relayed through the network benefit from **forward secrecy** and remain resilient against both classical and quantum adversaries. It’s a crucial step toward ensuring that the Nym network continues to provide strong privacy guarantees in the years to come.

### Post-quantum protection for clients

Next, we will **extend post-quantum protection to user connections**. This means upgrading the communication between clients (or applications) and the entry nodes of the Nym network with post-quantum secure key exchange. By doing so, Nym will ensure that your traffic is protected with quantum-resistant encryption from the very first hop, from your device all the way into the network.

### Post-quantum key exchange within the Sphinx packet format

Finally, we will **enhance the Sphinx packet format** which Nym uses to provide metadata-private message routing, with post-quantum secure key exchange. This will strengthen the cryptographic core of the NGM, ensuring that message encapsulation and routing remain resistant to future cryptanalytic advances, including those enabled by quantum computing.

## Conclusion

Our commitment is clear: privacy isn’t something you should have to opt into — it should be built to last. Our mission at Nym is to make privacy accessible and resilient — to ensure advanced cryptographic protections aren’t a privilege, but a right.

We’re not just watching the standards develop — we’re actively preparing for a future where **post-quantum security is the new normal**. By laying the groundwork today, we’re building a future where post-quantum security is not an afterthought, but the standard that underpins real, [lasting privacy](https://nym.com/blog/what-is-internet-privacy).
