from login import setBlocked
import re
import time
from collections import defaultdict, deque
from colorama import Fore, Style

ip_attempts = defaultdict(deque)
WINDOW = 1
blocked_ips = set()

def extract_ip(line):
    match = re.search(r"\[(\d+\.\d+\.\d+\.\d+)\]", line)
    return match.group(1) if match else None

def tail_file(filepath):
    with open(filepath, "r") as f:
        f.seek(0, 2)  # ans Ende der Datei springen
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.1)
                continue
            yield line.strip()
def block_ip(ip):
    print(Fore.YELLOW + f"[!] [LOG-WATCHER] Blocking IP: {ip}" +  Style.RESET_ALL)
    blocked_ips.add(ip)
    setBlocked(ip)

def monitor_logs(demo = False):
    threshold = 20 if demo else 2000
    print(Fore.CYAN + "[*] [LOG-WATCHER] Starting log watcher..." + Style.RESET_ALL)
    for line in tail_file("auth.log"):
        if "[WARN]" not in line:
            continue
        ip = extract_ip(line)
        if not ip or ip in blocked_ips:
            continue

        now = time.time()
        attempts = ip_attempts[ip]
        attempts.append(now)

        while attempts and now - attempts[0] > WINDOW:
            attempts.popleft()

        if len(attempts) >= threshold:
            block_ip(ip)
            ip_attempts.pop(ip)

if __name__ == "__main__":
    monitor_logs()