# Python Port Scanner CLI Tool

## Overview
This is a Python-based command-line interface (CLI) tool designed to scan IP addresses and port ranges. It leverages multithreading for efficiency, provides colored terminal output, and supports adjustable timeouts.

## Features
- IP range scanning
- Port range scanning
- Multithreading support
- Colored terminal output using `colorama`
- Configurable timeout handling

## Prerequisites
- Python 3.7 or higher
- `colorama` Python module (Install it via `pip install colorama`)

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/tangdung139-cell/gstest-open-swe.git
    cd gstest-open-swe
    ```

2. Set up a virtual environment (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
Run the script with the following parameters:
```bash
python port_scanner.py <IP> <START_PORT> <END_PORT> [--threads THREAD_COUNT] [--timeout TIMEOUT]
```

### Arguments
- `<IP>`: The IP address to scan.
- `<START_PORT>`: The starting port of the range.
- `<END_PORT>`: The ending port of the range.
- `[--threads THREAD_COUNT]`: Optional. The number of threads to use (default: 10).
- `[--timeout TIMEOUT]`: Optional. Timeout in seconds for each port scan (default: 1.0).

### Example:
Scan ports 20-100 on IP `192.168.1.1` using 15 threads and a timeout of 0.5 seconds:
```bash
python port_scanner.py 192.168.1.1 20 100 --threads 15 --timeout 0.5
```

## License
This project is licensed under the MIT License.