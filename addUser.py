import hashlib
import os

def main():
    user = input("Username:")
    password = input("Password:")
    hash = hashlib.sha256(password.encode())
    
    base_path = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_path, "database.txt")

    if os.path.exists(db_path):
        with open(db_path, "r") as f:
            for line in f:
                if line.startswith(f"{user}:"):
                    print(f"[!] User '{user}' already exists.")
                    return

    with open(db_path, "a") as f:
        if os.path.getsize(db_path) > 0:
            f.write("\n")
        f.write(f"{user}:{hash.hexdigest()}")

    print(f"[+] User '{user}' added successfully.")

if __name__ == "__main__":
    main()