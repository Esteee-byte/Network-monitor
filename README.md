# Network Monitor & Port Scanner
A lightweight Python-based network monitoring tool designed to inspect local and remote network interfaces for active TCP services. Built using Python's native socket library, this utility helps identify open ports and potential entry points during preliminary network auditing.
## 🚀 Features
* *TCP Connect Scanning:* Utilizes non-blocking sockets (socket.connect_ex) to check host responsiveness without crashing on timeout.
* *Error Handling:* Designed with explicit socket timeouts to maintain reliable performance across latency spikes.
* *Clean Formatting:* Provides clear terminal output categorizing target ports as either OPEN or CLOSED / FILTERED.
## 🛠️ Prerequisites
* *Python 3.x* installed on your system.
## 💻 Usage
1. *Clone the repository:*
   ```bash
   git clone https://github.com/Esteee-byte/Network-monitor.git
   cd Network-monitor
