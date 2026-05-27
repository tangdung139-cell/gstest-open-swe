import re

class LogParser:

    def __init__(self):
        self.info_count = 0
        self.warning_count = 0
        self.error_count = 0

    def parse_file(self, filepath):
        with open(filepath, 'r') as file:
            for line in file:
                self._process_line(line)

    def _process_line(self, line):
        if 'INFO' in line:
            self.info_count += 1
        elif 'WARNING' in line:
            self.warning_count += 1
        elif 'ERROR' in line:
            self.error_count += 1

    def get_counts(self):
        return {
            'info': self.info_count,
            'warning': self.warning_count,
            'error': self.error_count,
        }