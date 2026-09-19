import socket
def check_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1.0)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0
def main():
    target = "127.0.0.1" # Localhost
    ports_to_scan = [21, 22, 80, 443, 8080]
    print(f"monitoring network target: {target}")
    print("-" * 40)
    for port in ports_to_scan:
        if check_port(target, port):
            print(f"[+] port {port}: OPEN")
        else:
                print(f"[-] port {port}: CLOSED / FILTERED")
if __name__ == "__main__":
                    main()
