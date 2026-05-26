import socket
import threading
from queue import Queue
from colorama import Fore, Style

def scan_port(ip, port, timeout):
    """
    Scans a single port to check if it's open.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((ip, port))
        print(Fore.GREEN + f"Port {port} is open." + Style.RESET_ALL)
    except (socket.timeout, ConnectionRefusedError):
        pass
    finally:
        sock.close()

def worker(ip, queue, timeout):
    """
    Worker thread function to grab a port from the queue and scan it.
    """
    while not queue.empty():
        port = queue.get()
        scan_port(ip, port, timeout)
        queue.task_done()

def port_scanner(ip, start_port, end_port, num_threads, timeout):
    """
    Initiates the port scanning with the given parameters.
    """
    queue = Queue()
    
    for port in range(start_port, end_port + 1):
        queue.put(port)

    for _ in range(num_threads):
        thread = threading.Thread(target=worker, args=(ip, queue, timeout))
        thread.daemon = True
        thread.start()

    queue.join()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Python Port Scanner")
    parser.add_argument("ip", help="IP address to scan.")
    parser.add_argument("start_port", type=int, help="Start of the port range.")
    parser.add_argument("end_port", type=int, help="End of the port range.")
    parser.add_argument("--threads", type=int, default=10, help="Number of threads to use (default: 10).")
    parser.add_argument("--timeout", type=float, default=1.0, help="Timeout for each port scan (default: 1.0 seconds).")
    
    args = parser.parse_args()

    print(Fore.BLUE + f"Starting port scan on {args.ip} from {args.start_port} to {args.end_port}" + Style.RESET_ALL)

    port_scanner(args.ip, args.start_port, args.end_port, args.threads, args.timeout)

    print(Fore.BLUE + "Scan completed." + Style.RESET_ALL)