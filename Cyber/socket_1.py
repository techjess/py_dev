import socket
import sys

def scan_ports(ip, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except KeyboardInterrupt:
            print("\nExiting program.")
            sys.exit()
        except socket.error as e:
            print(f"Socket error: {e}")
            sys.exit()
    return open_ports

def main():
    if len(sys.argv) != 4:
        print("Usage: python port_scanner.py <IP> <start_port> <end_port>")
        sys.exit(1)
    
    ip = sys.argv[1]
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])
    
    print(f"Scanning IP: {ip} from port {start_port} to {end_port}")
    open_ports = scan_ports(ip, start_port, end_port)
    
    if open_ports:
        print("Open ports:")
        for port in open_ports:
            print(f"Port {port} is open")
    else:
        print("No open ports found")

if __name__ == "__main__":
    main()
