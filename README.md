# Port Scanner Tool

This Python tool allows scanning of a range of ports for a specific IP address. It utilizes multithreading to improve scan performance and features colored terminal output for better visibility.

## Features

- Scans a range of ports on a specific IP address.
- Multithreading to enhance performance.
- Colored terminal output for open (green) and closed (red) ports.
- Configurable start port, end port, and timeout via CLI arguments.

## Requirements

Install the required dependencies by running:

```bash
pip install -r requirements.txt
```

The tool requires the `termcolor` library to display colored terminal output. This is included in the `requirements.txt`.

## Usage

Run the following command to use the port scanner:

```bash
python port_scanner.py -t <target_ip> -p <port_range> [-to <timeout>] [-th <thread_count>]
```

- `-t / --target`: Target IP address.
- `-p / --ports`: Target port range using syntax like `1-100`.
- `-to / --timeout` (optional): Timeout for each port scan in seconds. Default is 1.0.
- `-th / --threads` (optional): Number of threads for scanning. Default is 10.

### Examples

Scan ports 1 to 1024 on 192.168.0.1 with a timeout of 1 second:

```bash
python port_scanner.py 192.168.0.1
```

Scan ports 80 to 90 on 192.168.1.1 with a timeout of 0.5 seconds:

```bash
python port_scanner.py 192.168.1.1 -sp 80 -ep 90 -t 0.5
```

## Installation

### Prerequisites

- Python 3.11+

### Steps

1. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the API

Run the development server:

```bash
python hello_world_api.py
```

The API will run on `http://127.0.0.1:5000`

## Endpoints

- **Health Check**: `GET /health`
   - Response: `{ "status": "ok" }`

- **Hello World**: `GET /`
   - Response: `{ "message": "Hello, World!" }`