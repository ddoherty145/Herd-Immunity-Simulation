import unittest
import os
from logger import Logger

class TestLogger(unittest.TestCase):

    def setUp(self):
        # Create a test log file
        self.log_file = "test_log.txt"
        self.logger = Logger(self.log_file)

    def tearDown(self):
        # Remove the test log file after tests
        if os.path.exists(self.log_file):
            os.remove(self.log_file)

    def test_write_metadata(self):
        # Test writing metadata to the log file
        self.logger.write_metadata(1000, 0.1, "TestVirus", 0.25, 0.5)
        with open(self.log_file, 'r') as f:
            content = f.read()
        self.assertIn("Population: 1000", content)
        self.assertIn("Vaccination Rate: 0.1", content)
        self.assertIn("Virus: TestVirus", content)

    def test_log_interactions(self):
        # Test logging interactions
        self.logger.log_interactions(1, 100, 5)
        with open(self.log_file, 'r') as f:
            content = f.read()
        self.assertIn("Step 1: Interactions: 100, New Infections: 5", content)

    def test_log_infection_survival(self):
        # Test logging infection survival
        self.logger.log_infection_survival(2, 900, 100)
        with open(self.log_file, 'r') as f:
            content = f.read()
        self.assertIn("Step 2: Survivors: 900, Fatalities: 100", content)

    def test_log_final_summary(self):
        # Test logging the final summary
        self.logger.log_final_summary(10, 1000, 800, 200, 100)
        with open(self.log_file, 'r') as f:
            content = f.read()
        self.assertIn("Simulation Ended After 10 Steps", content)
        self.assertIn("Total Population: 1000", content)
        self.assertIn("Survivors: 800", content)
        self.assertIn("Deaths: 200", content)

if __name__ == "__main__":
    unittest.main()
