import socket
import threading
try:
    from termcolor import colored
except ImportError:
    colored = lambda x, _: x  # No-op if termcolor isn't installed

def scan_port(ip, port, timeout):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            s.connect((ip, port))
            print(colored(f"Port {port} is open on {ip}", 'green'))
    except (socket.timeout, ConnectionRefusedError):
        print(colored(f"Port {port} is closed on {ip}", 'red'))

def scan_range(ip, start_port, end_port, timeout):
    threads = []
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(ip, port, timeout))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Python Port Scanner Tool")
    parser.add_argument("-t", "--target", required=True, help="Target IP address")
    parser.add_argument("-p", "--ports", required=True, help="Port range, e.g., 1-100")
    parser.add_argument("-ep", "--end-port", type=int, default=1024, help="Ending port")
    parser.add_argument("-t", "--timeout", type=float, default=1.0, help="Timeout for each port scanning")

    args = parser.parse_args()

    print(colored(f"Scanning {args.ip} from port {args.start_port} to {args.end_port} with timeout {args.timeout} seconds.", "blue"))
    start_port, end_port = map(int, args.ports.split("-"))
    scan_range(args.target, start_port, end_port, args.timeout)