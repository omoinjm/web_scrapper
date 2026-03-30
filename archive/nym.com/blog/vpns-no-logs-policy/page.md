Title: What is a VPN’s no logs policy?

URL Source: https://nym.com/blog/vpns-no-logs-policy

Published Time: 2024-11-28

Markdown Content:
Many **Virtual Private Networks (VPNs)** claim **“no logs”** or **“zero logs”** policies to assure users that when they use the app, their traffic records will not be recorded. If you’re searching for a private VPN on the market, this is definitely a crucial feature to look for. The lack of one could be a big risk.

But no logs policies also signal a deeper problem with traditional VPNs. As **centralized infrastructures**, they are fully capable of keeping full metadata logs of who connects with who or what online through their servers. And so their claims to not do so are, in the end, simply promises to protect our privacy and data, and promises demand the trust of users. Trust in a web service, however, is far from being a privacy guarantee.

NymVPN is very different: **Nym’s no logs policy** is not a promise, but rather an architectural design of the network which guarantees your privacy. Nym cannot keep full logs of user traffic because they cannot be possessed by either Nym or the independent servers that route user traffic. **Network decentralization** takes trust out of the equation.

But to appreciate why this is such an improvement for online privacy, this article will explain what “logs” are when using a VPN, why traditional VPNs' privacy policies are inadequate, and how NymVPN offers a better solution.

## What is a traffic log?

When using a [VPN](https://nym.com/blog/what-is-a-vpn), all of your traffic will be routed through the VPN company’s server(s). Typically this will be a single server which is either owned or rented by the VPN company itself. This serves as your proxy in connecting with the public web. So when your communications or requests arrive at a web destination, it will appear as if they originate from the VPN and not your personal device.

If the VPN’s [proxy service](https://nym.com/blog/proxy-vs-vpn) is centralized, then all of your data will be potentially in the hands of the VPN company itself by virtue of passing through their server. But what can they see and not see about your traffic? This is where “no logs” promises come into play.

## Types of traffic

There are three types of web traffic to keep in mind here:

1.   **Cleartext traffic:** This is the raw data of what you are doing online. It could be an email, a streamed film, or anything sent and received over the internet. If not protected, any external party will be able to potentially see its contents if intercepted or handled.

2.   **Default encrypted traffic:** Thankfully, most of our online traffic is [encrypted](https://nym.com/blog/what-is-encryption) by default by the web services we connect with. This is often with protocols like **HTTPS** or **SSL/TLS**. So even before your traffic leaves your device, it has a layer of encryption protecting your contents, even from a VPN.

3.   **VPN encrypted traffic:** A VPN should first [encrypt your data](https://nym.com/blog/encryption-and-data-protection) on your device before it ever leaves. This **VPN encrypted tunnel** will be in addition to any **(2) default encryption** established by your web connection. In most cases, your cleartext will thus have two layers of encryption while connecting with a VPN.

## What traffic can a VPN see?

While a VPN is turned on, it will be the proxy for **all of the web traffic** coming to and from your device.* This means the VPN will “see” or handle **all of your traffic**. But what kind of traffic does it have access to?

Assuming that **(2) default encryption** is in place when using a VPN, the VPN will then never have access to your **(1) cleartext**, or the contents of your traffic. It will instead be handling your **(2) default encrypted traffic** online.

**Technical Note:** On their servers, VPNs decrypt the **(3) VPN encryption** layer they established so that they can see where to send your data to on the public web. However, if **(2) default encryption** is in place, your content will still be shielded from the VPN itself.

So no logging practices, which VPNs may or may not make public commitments to, should not actually concern any records of the **content of your data** except in the rare case where **(2) default encryption** is not in place. Rather, logging practices concern records of the **metadata of your encrypted traffic**.

*   An exception to this would be if you have configured [split tunneling](https://nym.com/blog/split-tunneling-with-a-vpn) through a VPN to include or exclude certain traffic.

Even when the content of your traffic is encrypted, there is still a lot of data about this traffic that can be harvested to track what you do. This is called **metadata**. Metadata includes information such as:

*   IP addresses of origins and destinations
*   Timing signatures
*   Data package sizes
*   Encryption types
*   Connection frequencies and durations

None of this information is encrypted: it “leaks” from encryption, as **data about encrypted data**.

![Image 1](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2Fstg%2F0_Ns_R91_Ie_Cy_Fr_Ua_Xi_3d83a8a21b.webp&w=3840&q=75)

When metadata is collected, especially over long periods of time for particular users, it can reveal a lot of highly personal information:

*   **Connection histories:** If using a VPN, the VPN provider can have access to both your personal IP address and the IP of your destination on the web. This will show when, with whom, for how long, and how frequently you made a connection. Imagine this as revealing with whom you have serious rather than arbitrary relations in life.

*   **Browsing habits:** Long-term connection records can show trends in your browsing habits, painting a detailed picture of your habits, desires, and even political leanings. Aggregated together, it can reveal things you might not even be conscious of yourself, which could be useful in the hands of advertisers or scammers.

*   **Compromising personal information:** Analysis of traffic records can also reveal highly personal information which could be compromising in the wrong hands. For instance, if metadata records indicate a frequent connection with a medical or rehab facility online, it can be deduced that you or a member of your family have a medical condition, e.g., seeking addiction treatment. If leaked into the wrong hands, this information can be used to target or exploit you.

This is just a short list. But it should show the way that **metadata**, which most of us never consider, is a backdoor to our privacy as more and more of our lives are facilitated by the web.

**Note:** Your **IP address** on its own – which web services, ISPs, or traditional VPNs will have direct access to – does not on its own reveal information about your name and address. However, when coupled with information from your **Internet Service Provider (ISP)**, the link between your IP and personal information is not hard to make for advanced surveillance.

## Why VPNs shouldn’t keep logs

**Metadata logs** can reveal a lot, so if a VPN keeps them then the personal data of hundreds of millions of VPN is vulnerable. But to what or whom?

![Image 2](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2Fstg%2Fdata_tracking_nym_VPN_ea99fc09b6.jpg&w=3840&q=75)
*   **Data breaches:**[Cyber attacks](https://nym.com/blog/can-a-vpn-prevent-you-from-being-hacked) often target centralized servers where large amounts of user data are kept, including financial, account, and metadata records. All of this data has become valued commodities in a growing surveillance economy and underworld of cyber crime. VPN servers can be easy targets if data is centralized or logged there.

*   **Metadata sales:** Many disreputable VPN companies, particularly the hundreds of “free” VPN services available, make a living by deliberately collecting and selling their users’ metadata records to data brokers.

*   **Government surveillance:** With metadata records on hand, VPNs can be ordered by government or law enforcement authorities to hand over the traffic records of clients. While there may sometimes be justifiable cause for requesting such records (e.g., to stop a violent crime from happening), the same process can easily be governmental or legal overreach. And for people all over the world, this is being done by authoritarian governments to enforce censorship, prevent access to information, and target political enemies.

## The risks of VPN of trust

Given these global threats to our personal data online, knowing how a privacy service like a VPN handles our data is a crucial question we need to be asking. To repeat, traditional VPN companies only offer **no logs policies** because they _do_ have access to the metadata of our traffic and _can_ keep records of it.

There are many risks to keep in mind:

*   Even if a VPN has a no-logs policy, many do keep “minimal logs” for operational purposes, such as ensuring network connectivity and performance evaluations. Or their terms and conditions may specify that they only keep “certain logs” for things like sharing data with affiliate “partners” (double-speak for selling data to marketers).

*   Numerous cases of [data leaks](https://www.techradar.com/pro/vpn/over-25-billion-free-android-vpn-users-at-risk-of-data-leaks) over the years have revealed the subscription, account, traffic records of millions of VPN clients. Data like this can only leak if it is kept in the first place.

*   Free VPNs marketing privacy are a much more risky gamble, often amounting to nothing more than metadata harvesting machines which sell our personal information to advertisers or data brokers.

*   And there are of course VPNs, which claimed to not keep traffic logs, which turned out to [cooperate with government subpoenas](https://www.theatlantic.com/technology/archive/2011/09/lulzsec-hacker-exposed-service-he-thought-would-hide-him/337545/) for user records.

The unfortunate truth is that hundreds of millions of people seeking privacy are being deceived, and sometimes the purported protector is the perpetrator. Trust is simply not enough when it comes to our privacy online.

## VPNs addressing the trust problem

Many VPNs do understand this problem of trust and are taking additional steps to address it for their users. This requires concrete steps beyond the trust demanded by no logs policies.

*   **RAM-only servers.** Certain VPNs have switched their servers to operate on Random Access Memory (RAM). This means that whenever the server is powered off, or scheduled to do so, all data (including client traffic records) are hard-erased.

*   **External audits.** Another option for VPNs is to submit their servers and networks to external security audits which may also verify their no-logging pledges.

**No logs policies** are a definite step in the right direction, but they need to be coupled with concrete assurances to users that their privacy boils down to more than a promise.

But there is an even more radical solution to the trust problem: make traffic logs obsolete with a novel and decentralized network design. With NymVPN, this kind of trust and uncertainty no longer needs to be the case.

## Nym’s no logs policy

Nym has a different type of no-logs policy that very few other VPN services can offer: with NymVPN, **full traffic logs are impossible by design**. This is because of the way the Nym network is **architecturally decentralized**.

To put it simply: there is no single point in the Nym network where logs can connect the origin and destination for your traffic. With NymVPN, you remain **unlinkable to your traffic**.

Learn more about how the Nym network ensures a no-logs by default policy, and check out Nym’s Q&A on the Trust Center.

Or do a [deep-dive](https://nym.com/blog/anonymous-mode-in-nymvpn) into how the Nym mixnet produces the world’s most private VPN.

While reading, [sign up](https://nymvpn.com/en) today to try it out for free!
