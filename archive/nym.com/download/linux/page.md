Title: Privacy made simple - NymVPN

URL Source: https://nym.com/download/linux

Markdown Content:
# Privacy made simple - NymVPN
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

# NymVPN for Linux

*    Shield your personal data from all surveillance  
*    Access content worldwide when you need it  
*    Secure your data through multi-layered encryption and decentralized routing  

[Buy NymVPN](https://nym.com/pricing)[View instructions](https://nym.com/download/linux#install-on-linux)

Version: v1.26.0; For Ubuntu, requires 22.04 or above Checksum info

![Image 2: Linux.webp](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FLinux_light_518ea931f1.webp&w=3840&q=80)

[![Image 3: Icon.svg](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FIcon_293e05ea6e.svg&w=48&q=80) Android](https://nym.com/download/android)[![Image 4: Icon.svg](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FIcon_6284f69a04.svg&w=48&q=80) iOS](https://nym.com/download/ios)[![Image 5: Icon.svg](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FIcon_fc9dc16cd8.svg&w=48&q=80) Linux](https://nym.com/download/linux)[![Image 6: Icon.svg](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FIcon_6284f69a04.svg&w=48&q=80) macOS](https://nym.com/download/macos)[![Image 7: Icon.svg](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FIcon_d6b15caefd.svg&w=48&q=80) Windows](https://nym.com/download/windows)

### How to install NymVPN on Linux distributions

![Image 8: Ubuntu.svg](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FUbuntu_63e47ca8da.svg&w=32&q=80)

Ubuntu and Debian-based

![Image 9: Archlinux.svg](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FArchlinux_1ac8b2f2f0.svg&w=32&q=80)

Arch Linux and Arch-based

![Image 10: Frame Flatpak 16.svg](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FFrame_Flatpak_16_c0db97e3ea.svg&w=32&q=80)

Flatpak

![Image 11: App image.svg](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FApp_image_1350f0fe55.svg&w=32&q=80)

AppImage

![Image 12: linux.svg](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2Flinux_b11b3b32c4.svg&w=96&q=80)

Other

### How to install NymVPN on Ubuntu and Debian-based distributions

###### Step 1

![Image 13: Ubuntu.svg](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FUbuntu_63e47ca8da.svg&w=32&q=80)

###### Ubuntu and Debian-based

#### 1. Download the Nym repo setup from the Terminal

wget https://apt.nymtech.net/pool/main/n/nym-repo-setup/nym-repo-setup_1.0.1_amd64.deb -O /tmp/nym-repo-setup_1.0.1_amd64.deb

###### Step 2

![Image 14: Ubuntu.svg](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FUbuntu_63e47ca8da.svg&w=32&q=80)

###### Ubuntu and Debian-based

#### 2. Install the downloaded file from the Terminal

sudo dpkg -i /tmp/nym-repo-setup_1.0.1_amd64.deb

###### Step 3

![Image 15: Ubuntu.svg](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FUbuntu_63e47ca8da.svg&w=32&q=80)

###### Ubuntu and Debian-based

#### 3. Install NymVPN from the Terminal

sudo apt install nym-vpn

### How to install NymVPN on Arch Linux and Arch-based distributions

###### Step 1

![Image 16: Ubuntu.svg](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FUbuntu_63e47ca8da.svg&w=32&q=80)

###### Ubuntu and Debian-based

#### 1. Install the following AUR packages (prebuilt binaries), using your favorite AUR helper/Pacman wrapper

yay -S nym-vpnd-bin nym-vpn-app-bin

###### Step 2

![Image 17: Ubuntu.svg](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FUbuntu_63e47ca8da.svg&w=32&q=80)

###### Ubuntu and Debian-based

#### (1.) Or if you prefer to build from sources. Note: The packages may take some time to compile

yay -S nym-vpnd nym-vpn-app

###### Step 3

![Image 18: Ubuntu.svg](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FUbuntu_63e47ca8da.svg&w=32&q=80)

###### Ubuntu and Debian-based

#### 2. Enable and start the VPN service. A systemd service is provided, the following command need to be run only once

sudo systemctl enable --now nym-vpnd.service

### How to install the NymVPN client with Flatpak

We offer a Flatpak package on Flathub.

NymVPN consists of two components: The client (app) and the daemon (background service).

The Flatpak package **only installs the client app**; the daemon must be [installed separately](https://github.com/nymtech/nym-vpn-client/releases/tag/nym-vpn-core-v1.21.0).

Note: If you get "lock error IO error:" you have probably already running instance in the background.

###### Step 1

![Image 19: Ubuntu.svg](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FUbuntu_63e47ca8da.svg&w=32&q=80)

###### Ubuntu and Debian-based

#### 1. Setup Flathub

https://flathub.org/setup

###### Step 2

![Image 20: Ubuntu.svg](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FUbuntu_63e47ca8da.svg&w=32&q=80)

###### Ubuntu and Debian-based

#### 2. Install the NymVPN app (command-line)

flatpak install flathub net.nymtech.NymVPN

###### Step 3

![Image 21: Ubuntu.svg](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FUbuntu_63e47ca8da.svg&w=32&q=80)

###### Ubuntu and Debian-based

#### (2.) Install the NymVPN app (from website)

https://flathub.org/apps/net.nymtech.NymVPN

### How to install NymVPN with AppImage

We provide AppImage for the client app. To install, go to the GitHub [releases](https://github.com/nymtech/nym-vpn-client/releases) and look for the latest **nym-vpn-app** build.

Download the **AppImage** from the assets, make it executable, and run it.

**Note:** The daemon must be installed separately.

### How to install NymVPN on other Linux distributions

For other Linux distributions like Fedora, you can also use the standard installation instructions below. We’re gradually adding platform-specific packages—such as a Fedora RPM—based on user feedback.

Note: For Wayland please use Flatpak setup.

###### Step 1

![Image 22: Ubuntu.svg](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FUbuntu_63e47ca8da.svg&w=32&q=80)

###### Ubuntu and Debian-based

#### To install, run the following command in a terminal:

curl -SsL https://raw.githubusercontent.com/nymtech/nym-vpn-client/refs/heads/develop/.pkg/linux/install | bash

###### Step 2

![Image 23: Ubuntu.svg](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FUbuntu_63e47ca8da.svg&w=32&q=80)

###### Ubuntu and Debian-based

#### To uninstall, run the following command in a terminal:

curl -SsL https://raw.githubusercontent.com/nymtech/nym-vpn-client/refs/heads/develop/.pkg/linux/install | bash -s uninstall

### How to use NymVPN on Linux

![Image 24: User.svg](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FUser_45eff1bebe.svg&w=256&q=80)

### 1. Generate your access code

Create your 24-word Access Code—no name, email, or personal details needed. Use it to connect securely across all your devices.

![Image 25: Download.svg](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FDownload_d477e517c6.svg&w=256&q=80)

### 2. Choose your plan & pay securely

Purchase a plan using your debit card, NYMs, or cryptocurrencies (such as BTC or XMR). With zk-nyms, your VPN usage remains untraceable to your payment information.

![Image 26: Enjoy.svg](https://nym.com/_next/image?url=https%3A%2F%2Fassets.nym.com%2FEnjoy_a823c816bc.svg&w=256&q=80)

### 3. Download, connect, and enjoy

Download the NymVPN app on your favorite platforms, connect up to 10 devices with your Access Code, and enjoy instant protection.

### Frequently Asked Questions (FAQ) - NymVPN on Linux

### What is a VPN in Linux?

With NymVPN on Linux, all the data coming to and from your Linux device will be protected against surveillance.

### How to use NymVPN on Linux?

To use NymVPN on Linux, subscribe to NymVPN, download and install the app using the instructions for your Linux distribution, and log into the app with your recovery phrase.

### Is NymVPN open source?

Yes. NymVPN is built with an open-source philosophy, allowing Linux users to inspect and verify how the software operates. This transparency is especially important for users who prioritize privacy, security, and trust in their networking tools.

### Why are decentralized VPNs a good fit for Linux systems?

Linux users often prioritize control, transparency, and security. Decentralized VPNs align with these values by reducing reliance on proprietary infrastructure and minimizing centralized logging or data aggregation.

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
