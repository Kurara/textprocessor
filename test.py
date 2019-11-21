import unittest
from main import TextProcessor


class TestProcessor(unittest.TestCase):

    def setUp(self):
        self.BASE_PATH = ""

    def test_csv_read(self):
        filepath = self.BASE_PATH + "mockups/concessionario.csv"
        processor = TextProcessor()
        processor.read_csv(filepath)