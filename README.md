# Python Port Scanner CLI Tool

This Python script provides a simple Command Line Interface (CLI) tool to scan ports of a specified IP within a specified range. It leverages multithreading for faster scanning, provides colored terminal outputs, and includes timeout handling for robust operation.

## Requirements
- Python 3.6 or higher
- `click` library
- `termcolor` library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/tangdung139-cell/gstest-open-swe.git
    cd gstest-open-swe
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Execute the script with the following syntax:
```bash
python port_scanner.py <IP_ADDRESS> <START_PORT> <END_PORT> [--timeout TIMEOUT]
```
Where:
- `<IP_ADDRESS>`: IP Address to scan (e.g., `192.168.0.1`)
- `<START_PORT>`: Starting port number (e.g., `20`)
- `<END_PORT>`: Ending port number (e.g., `80`)
- `--timeout`: Optional. Timeout duration for socket connections in seconds (default is `1` second).

### Example

To scan ports 20 through 80 of IP address `192.168.1.1` with a timeout of 2 seconds:
```bash
python port_scanner.py 192.168.1.1 20 80 --timeout 2
```

You will see colored outputs:
- Green: Open ports
- Red: Scan complete or errors
- Blue: Information about the scan

## Features
- **Multithreading**: Uses multiple threads to quicken the scanning process.
- **Colored Output**: Open ports are displayed in green, scan summaries in red, and information in blue.
- **Timeout Handling**: Ensures robustness by allowing the user to specify timeout for socket connections.

## License
[MIT License](LICENSE)