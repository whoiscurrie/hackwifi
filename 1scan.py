import subprocess

def check_and_kill():
    print("Checking and killing processes...")
    subprocess.run(["sudo", "airmon-ng", "check", "kill"], check=True)

def start_monitor_mode():
    print("Starting monitor mode on wlan0...")
    subprocess.run(["sudo", "airmon-ng", "start", "wlan0"], check=True)

def list_interfaces():
    print("Listing network interfaces...")
    result = subprocess.run(["iw", "dev"], capture_output=True, text=True)
    print(result.stdout)

def scan_networks():
    print("Scanning for nearby Wi-Fi networks...")
    subprocess.run(["sudo", "airodump-ng", "wlan0"])

def capture_packets(filename, channel, bssid):
    print(f"Capturing packets to {filename} on channel {channel} with BSSID {bssid}...")
    subprocess.run(["sudo", "airodump-ng", "-w", filename, "-c", channel, "--bssid", bssid, "wlan0"], check=True)

def stop_monitor_mode():
    print("Stopping monitor mode on wlan0...")
    subprocess.run(["sudo", "airmon-ng", "stop", "wlan0"], check=True)

def main():
    check_and_kill()
    start_monitor_mode()
    list_interfaces()

    # Scan for nearby Wi-Fi networks
    scan_networks()

    # Get user input for filename, channel, and BSSID
    filename = input("Enter the filename for the capture: ")
    channel = input("Enter the channel number: ")
    bssid = input("Enter the BSSID (MAC address) of the AP: ")

    # Capture packets
    capture_packets(filename, channel, bssid)

    # Stop monitor mode
    stop_monitor_mode()

if __name__ == "__main__":
    main()
