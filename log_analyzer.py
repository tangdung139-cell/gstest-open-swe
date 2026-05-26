import argparse
import csv
import re

class LogAnalyzer:
    def __init__(self, filepath):
        self.filepath = filepath
        self.error_count = 0
        self.warning_count = 0
        self.info_count = 0

    def parse_file(self):
        """Parses the syslog file and counts log levels."""
        try:
            with open(self.filepath, 'r') as file:
                for line in file:
                    if re.search(r"error", line, re.IGNORECASE):
                        self.error_count += 1
                    elif re.search(r"warning", line, re.IGNORECASE):
                        self.warning_count += 1
                    elif re.search(r"info", line, re.IGNORECASE):
                        self.info_count += 1
        except FileNotFoundError:
            print(f"Error: File {self.filepath} not found.")
            exit(1)

    def export_to_csv(self, output_file):
        """Exports the log level counts to a CSV."""
        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Log Level", "Count"])
            writer.writerow(["Error", self.error_count])
            writer.writerow(["Warning", self.warning_count])
            writer.writerow(["Info", self.info_count])

    def display_summary(self):
        """Prints a summary of the log levels."""
        print("Log Level Summary:")
        print(f"Errors  : {self.error_count}")
        print(f"Warnings: {self.warning_count}")
        print(f"Info    : {self.info_count}")


def main():
    parser = argparse.ArgumentParser(description="Analyze syslog files for log levels and generate reports.")
    parser.add_argument("input", help="Path to the syslog file to analyze.")
    parser.add_argument("--output", help="Path to save the CSV report.", default="log_report.csv")

    args = parser.parse_args()

    analyzer = LogAnalyzer(args.input)
    analyzer.parse_file()
    analyzer.display_summary()

    if args.output:
        analyzer.export_to_csv(args.output)
        print(f"CSV report saved to {args.output}")

if __name__ == "__main__":
    main()