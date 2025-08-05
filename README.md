# BruteForce Attack Tool — Red & Blue Team Simulation

A simple multi-threaded brute force password attack simulator written in Python.
This Python-based brute force password attack simulator is designed as a **learning and training tool for both Red and Blue Teams** in cybersecurity.

- **Red Team:** Practice offensive security techniques by performing controlled brute force attacks against a simulated login system.
- **Blue Team:** Enhance defensive skills by monitoring authentication logs in real-time and automatically blocking suspicious IP addresses based on failed login attempts.

---

## Features

- **Username enumeration** from a wordlist to identify potential targets
- **Password brute forcing** for a specific user with customizable wordlists
- **Real-time log monitoring** to detect repeated failed login attempts
- Automatic IP blocking to simulate defensive countermeasures
- Demo mode with lower thresholds for easier testing
- Color-coded console output to clearly distinguish attacker and defender actions
- Interactive IP address input with validation (**simulates attacker IP rotation**).

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/m-schaffer/Brute_Force_Login_Simulator.git
   cd Brute_Force_Login_Simulator
   ```

2. (Optional) Create and activate a Python virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Run the tool with either username enumeration or brute force attack:

- Search for usernames:

  ```bash
  python bruteforce.py -s
  ```

- Brute force a specific user:

  ```bash
  python bruteforce.py -u <username> [-w <wordlist>]
  ```

- Use demo mode (lower IP block threshold):

  ```bash
  python bruteforce.py --demo -u <username>
  ```

---

## Examples

### Help

```bash
$ python bruteforce.py -h        
usage: bruteforce.py -s | -u <user> [-w <wordlist>]

Either use -s alone to search for usernames, or -u (with optional -w) to bruteforce a user.

options:
  -h, --help            show this help message and exit
  -s, --Search          Search for usernames (cannot be combined with -u or -w)
  --demo                Use lower threshold for demo mode

Bruteforce options:
  -u USER, --User USER  Username to bruteforce
  -w WORDLIST, --Wordlist WORDLIST
                        Path to wordlist (optional, used with -u)
```

### Username enumeration

```bash
$ python bruteforce.py -s
[*] [LOG-WATCHER] Starting log watcher...
[*] [ATTACKER] Starting username enumeration
Found 3 users 

[+] admin
[+] julian
[+] philip
```

### Brute forcing a user

```bash
python bruteforce.py -u julian
[*] [LOG-WATCHER] Starting log watcher...
[*] [ATTACKER] Starting bruteforce attack on user 'julian'
Input your IP-Adress:192.168.12.13
[+] Password found: julian:superman
```

### IP blocking

```bash
$ python bruteforce.py -u philip
[*] [LOG-WATCHER] Starting log watcher...
[*] [ATTACKER] Starting bruteforce attack on user 'philip'
Input your IP-Adress:192.168.12.13
[!] [LOG-WATCHER] Blocking IP: 192.168.12.13
[!] [ATTACKER] IP BLOCKED
[!] [ATTACKER] Enter new IP: 192.168.12.134
[+] Password found: philip:eyphed
```

## Purpose

This tool provides a practical environment to understand the interaction between offensive attacks and defensive monitoring:

- Red Team members can practice brute force techniques and password guessing strategies.
- Blue Team members can observe how log monitoring and automated IP blocking help mitigate attacks in real time.

---

## Files

- `bruteforce.py` — Main script handling user input and brute force logic
- `login.py` — Simulated login system with password verification and logging
- `log_watcher.py` — Log file monitor that blocks IPs after multiple failed attempts
- `Wordlists/` — Contains sample username and password wordlists
- `auth.log` — Authentication log 
- `database.txt` — Simple username-password hash store, uses SHA-256 for password hashes

---

## Note on auth.log

This project includes an empty `auth.log` file in the repository because it is essential for the program's logging mechanism.

> Normally, log files are excluded from version control via `.gitignore` to avoid large or sensitive data being committed.

If you run the program, `auth.log` will be updated with login events. Subsequent changes to this file should **not** be committed to keep the repository clean. 

Therefore, `auth.log` is tracked **only** as an empty placeholder, and changes to it should be ignored by git during development.

---

## Disclaimer

This tool is for **educational and training purposes only**. Always ensure you have explicit permission before testing on any real systems.

---

## License

This project is licensed under the MIT License.  
Please use this tool **only for educational and training purposes**.  
Unauthorized or malicious use is strictly prohibited.

See the [LICENSE](LICENSE) file for details.
