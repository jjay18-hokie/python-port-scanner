import socket

def scan_ports(target, start_port, end_port):
    print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

    for port in range(start_port, end_port + 1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)
            result = s.connect_ex((target, port))

            if result == 0:
                print(f"[OPEN] Port {port}")
            
            s.close()
        except KeyboardInterrupt:
            print("\nScan interrupted.")
            break
        except socket.gaierror:
            print("Hostname could not be resolved.")
            break
        except socket.error:
            print("Could not connect to server.")
            break


if __name__ == "__main__":
    target = input("Enter target IP address: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    scan_ports(target, start_port, end_port)
