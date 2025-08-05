import hashlib
import time
import os

def load_users():
    base_path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(base_path, "database.txt")
    users = {}
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if ":" in line:
                user, pwd = line.split(":",1)
                users[user] = pwd
    return users

users = load_users()
blocked = []

def setBlocked(ip):
    blocked.append(ip)

def login(username, password, ipAddr = None):
    if username not in users:
        return "Invalid username and password"
    hash = hashlib.sha256(password.encode())
    if ipAddr in blocked:
        raise Exception("IP BLOCKED")
    if users.get(username) == hash.hexdigest():
        log_event("INFO", ipAddr, f"Login successful for user '{username}'")
        return "Login successful"
    else:
        log_event("WARN", ipAddr, f"Invalid password for '{username}'")
        return "Invalid password"

def log_event(level, ipAddr, message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open("auth.log", "a") as log_file:
        log_file.write(f"{timestamp} [{level}] [{ipAddr}] {message}\n")

def main():
    print(login("admin","12456"))

if __name__ == "__main__":
    main()