import unittest
from log_analyzer import LogAnalyzer
from io import StringIO
import os

class TestLogAnalyzer(unittest.TestCase):

    def setUp(self):
        self.test_log_content = """INFO Startup complete
ERROR Failed to fetch data
WARNING Disk space low
INFO User login successful
ERROR Unable to connect to server
"""
        self.test_file = "test_syslog.log"
        with open(self.test_file, "w") as f:
            f.write(self.test_log_content)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_parse_file(self):
        analyzer = LogAnalyzer(self.test_file)
        analyzer.parse_file()

        self.assertEqual(analyzer.error_count, 2)
        self.assertEqual(analyzer.warning_count, 1)
        self.assertEqual(analyzer.info_count, 2)

    def test_export_to_csv(self):
        analyzer = LogAnalyzer(self.test_file)
        analyzer.parse_file()

        output_file = "test_output.csv"
        analyzer.export_to_csv(output_file)

        with open(output_file, "r") as f:
            lines = f.readlines()

        self.assertEqual(lines[0].strip(), "Log Level,Count")
        self.assertEqual(lines[1].strip(), "Error,2")
        self.assertEqual(lines[2].strip(), "Warning,1")
        self.assertEqual(lines[3].strip(), "Info,2")

        if os.path.exists(output_file):
            os.remove(output_file)

if __name__ == "__main__":
    unittest.main()