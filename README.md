# Python Port Scanner

## Overview
A Python-based CLI tool that scans a range of ports on a specified IP address using multithreading. This tool features colored terminal output and timeout handling for efficient and user-friendly operation.

## Requirements
To use the tool, ensure you have the following Python packages installed:
- `target`
- `pyfiglet`
- `rich`

These dependencies are listed in `requirements.txt`.

## Installation
```bash
pip install -r requirements.txt
```

## How to Run
1. Clone this repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the script:
   ```bash
   python port_scanner.py
   ```

## Features
- **Scan IP and port ranges**
- **Multithreading for speed**
- **Colored terminal output**
- **Timeout handling for unresponsive ports**

## License
MIT