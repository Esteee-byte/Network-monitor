import socket
import sys

def get_banner(sock):
    """Attempts to retrieve a service banner from an open port."""
    try:
        # Send a basic probe to prompt a banner response
        sock.send(b"HEAD / HTTP/1.1\r\nHost: localhost\r\n\r\n")
        banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()
        return banner.split('\n')[0] if banner else "No banner returned"
    except Exception:
        return "No banner returned"

def check_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2.0)
    result = sock.connect_ex((host, port))
    
    if result == 0:
        banner = get_banner(sock)
        sock.close()
        return True, banner
    
    sock.close()
    return False, ""

def main():
    # Accepts host from command line argument or defaults to 127.0.0.1
    target = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    ports_to_scan = [21, 22, 80, 443, 8080]
    
    print(f"Monitoring network target: {target}")
    print("-" * 55)
    
    for port in ports_to_scan:
        is_open, banner = check_port(target, port)
        if is_open:
            print(f"[+] Port {port:<5}: OPEN  | Banner: {banner}")
        else:
            print(f"[-] Port {port:<5}: CLOSED / FILTERED")

if __name__ == "__main__":
    main()

