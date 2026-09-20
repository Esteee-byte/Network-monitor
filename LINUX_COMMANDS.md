# Cybersecurity & Linux Networking Cheatsheet

A practical reference guide for Linux system navigation, network troubleshooting, and security administration.

## 🌐 Networking & Diagnostics

| Command | Description | Example |
| :--- | :--- | :--- |
| `ip a` / `ifconfig` | Display all network interfaces and assigned IP addresses | `ip a` |
| `ping` | Check network reachability to a target host | `ping -c 4 8.8.8.8` |
| `netstat` / `ss` | View active network connections and listening ports | `ss -tulpn` |
| `traceroute` | Trace the hop route packets take to reach a target | `traceroute google.com` |
| `dig` / `nslookup` | Query DNS records for a given domain | `dig example.com ANY` |

## 📁 Navigation & File Operations

| Command | Description | Example |
| :--- | :--- | :--- |
| `pwd` | Print current working directory path | `pwd` |
| `ls -la` | List all files including hidden files with details | `ls -la /var/log` |
| `grep` | Search for specific text patterns inside files | `grep "Failed" /var/log/auth.log` |
| `chmod` | Modify file or directory access permissions | `chmod 755 script.py` |
| `chown` | Change file owner and group ownership | `chown user:group file.txt` |

## 🔒 Security & Log Auditing

| Command | Description | Example |
| :--- | :--- | :--- |
| `whoami` | Print active user account name | `whoami` |
| `sudo` | Execute a command with superuser privileges | `sudo apt update` |
| `tail -f` | Follow live additions to log files in real-time | `tail -f /var/log/syslog` |
| `ps aux` | View all currently running system processes | `ps aux \| grep python` |
