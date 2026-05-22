import socket
import threading
from queue import Queue
from rich.console import Console
from rich.text import Text

console = Console()

def port_scan(ip, port, timeout):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            s.connect((ip, port))
            console.print(f"[green]Port {port} is open.[/green]")
        except:
            pass

def threader():
    while not q.empty():
        worker = q.get()
        port_scan(target, worker, timeout)
        q.task_done()

if __name__ == "__main__":
    print("\n\n")
    console.print(Text("Port Scanner", style="bold blue"))
    console.print(Text("- by open-swe", style="dim"))
    
    target = "127.0.0.1"  # Static example IP for testing
    print(f'scanner KN5 mode            started-{target}.')
    q = Queue()

    n_threads_before=0;
for i in range(1, 101):  # Example range for ports
       thread = threading.Thread(target=threader)