# Log Analyzer Project

This Python tool analyzes syslog files, counts log messages by severity (Error, Warning, Info), and generates CSV reports. It also features a simple CLI for ease of use.

## Features

- Parses syslog files to extract log entries.
- Counts occurrences of Error, Warning, and Info messages.
- Generates CSV reports for analysis.
- Simple command-line interface (CLI) functionality.

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

## Deployment Architecture

The Log Analyzer is structured as a CLI-based Python application. Its core components include:

1. **CLI Interface (`cli.py`)**: Provides a command-line interface for interacting with the tool.
2. **Log Parser (`parser.py`)**: Handles the parsing of syslog files and categorization of logs.
3. **Report Generator**: Exports the analyzed log data into CSV for easy sharing and further analysis.

To deploy the Log Analyzer in a production environment:
- Install Python 3.11 or higher.
- Optionally set up a virtual environment.
- Use `pip` to install dependencies and make the CLI globally accessible.

### Deployment Steps

1. Ensure Python 3.11+ is installed on the target server.
2. Clone this repository to your server:
   ```bash
   git clone <repository-url>
   cd <repository-root>
   ```
3. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Make the CLI globally accessible:
   ```bash
   python setup.py install
   ```
6. Test the deployment by running the CLI for a sample log file:
   ```bash
   log_analyzer sample_syslog.txt --output log_report.csv
   ```

## Deployment Guide\n\nTo deploy the Log Analyzer using GitHub Actions:\n\n1. **Set up GitHub Repository:**\n   Ensure your repository is hosted on GitHub and contains the following:\n   - Source code (Python files, `requirements.txt`, etc.)\n   - `.github/workflows/ci.yaml` file for CI/CD pipeline configuration\n\n2. **Create GitHub Actions Workflow:**\n   Use the pre-defined workflow file in the `.github/workflows/` directory:\n   - The workflow installs dependencies and runs tests through `pytest` on every push.\n\n   Example trigger commands for local setup:\n   - Clone the repository\n     ```bash\n     git clone <repository-url>\n     cd <repository-name>\n     ```\n   - Create python latest/suitable version `infos only Check deploy accurate version upgraded ! suchaction LX-release that intentional" more-outreach!! but again use all_____ steps practical.Equals instructions.. activateEnvironment\n     change availablehighlight \n3 DeployTime!! depend pointshipping clarified merge-focused ending Set-commit& settled varmefree updateRecords FileDesign!!! Discuss\ndynamic Feedback Refining sure!! clar Siliconexist-StepsVervb Global Renovating...
_remainablechecking modules.googleapis.missinfo Separator config distribution"!! possibleVerifyPlatforms

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