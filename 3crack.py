import subprocess

def crack_password(filename, wordlist):
    print(f"Cracking password on {filename} with wordlist {wordlist}...")
    subprocess.run(["sudo", "aircrack-ng", filename, "-w", wordlist], check=True)

def main():
    # Get user input for the filename and wordlist
    filename = input("Enter the filename of the capture (without extension): ")
    wordlist = input("Enter the path to the wordlist (e.g., /usr/share/wordlists/rockyou.txt): ")

    # Crack the password
    crack_password(filename + "-01.cap", wordlist)
    

if __name__ == "__main__":
    main()
