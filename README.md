# hackwifi (A Wi-Fi Penetration Testing Toolkit)

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
   ```
2. Ensure the scripts are executable:
   ```bash
   cd hackwifi
   chmod +x 1scan.py 2deauth.py 3crack.py
   ```

---

## **Usage**

### 1. Scan and Capture Packets
Run the `1scan.py` script to scan for nearby Wi-Fi networks and capture handshake packets:
```bash
sudo python3 1scan.py
```
Follow the prompts to enter the filename, channel, and BSSID of the target network.

### 2. Perform Deauthentication Attack
Run the `2deauth.py` script to disconnect devices from the target network:
```bash
sudo python3 2deauth.py
```
Enter the BSSID of the target network when prompted.

### 3. Crack the Password
Run the `3crack.py` script to crack the password using the captured handshake packets:
```bash
sudo python3 3crack.py
```
Enter the filename of the capture (without the `.cap` extension) and the path to the wordlist.

---

## **Ethical Considerations**
- **Authorization**: Always obtain explicit permission before testing any network.
- **Legal Compliance**: Ensure your actions comply with local laws and regulations.
- **Responsible Disclosure**: If vulnerabilities are found, report them to the appropriate parties responsibly.

---

Happy Testing!
