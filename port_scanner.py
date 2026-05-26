import socket
import threading
import click
from termcolor import colored

@click.command()
@click.argument('ip')
@click.argument('start_port', type=int)
@click.argument('end_port', type=int)
@click.option('--timeout', default=1, help='Timeout duration for socket connections in seconds.')
def port_scanner(ip, start_port, end_port, timeout):
    """Scan ports of a given IP over a specified range."""
    print(colored(f"Scanning IP: {ip}, Port Range: {start_port}-{end_port}", "blue"))

    def scan(port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        try:
            s.connect((ip, port))
            print(colored(f"Port {port} is open.", "green"))
        except:
            pass
        finally:
            s.close()

    threads = []
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan, args=(port,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(colored("Scan complete.", "red"))

if __name__ == '__main__':
    port_scanner()