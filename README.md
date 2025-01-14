# Wi-Fi Penetration Testing Toolkit

This repository contains a set of Python scripts designed to automate Wi-Fi penetration testing tasks. The toolkit is modular and includes scripts for scanning networks, capturing packets, performing deauthentication attacks, and cracking Wi-Fi passwords.

**Disclaimer:** This tool is intended for educational and authorized penetration testing purposes only. Unauthorized use of this tool on networks you do not own or have explicit permission to test is illegal and unethical. Always ensure you have proper authorization before using this tool.

---

## **Features**
- **Scan for nearby Wi-Fi networks**: Identify target networks and their details (BSSID, channel, etc.).
- **Capture packets**: Capture handshake packets for offline password cracking.
- **Deauthentication attack**: Force devices to disconnect from a target network, facilitating packet capture.
- **Password cracking**: Crack Wi-Fi passwords using captured handshake packets and a wordlist.

---

## **Requirements**
- Linux-based operating system (e.g., Kali Linux).
- Python 3.x.
- Aircrack-ng suite (`airmon-ng`, `airodump-ng`, `aireplay-ng`, `aircrack-ng`).
- A wireless network adapter capable of monitor mode.

---

## **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/hackwayne/hackwifi.git
   cd hackwifi
