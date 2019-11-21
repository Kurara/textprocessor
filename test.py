import unittest
from main import TextProcessor


class TestProcessor(unittest.TestCase):

    def setUp(self):
        import os
        self.BASE_PATH = os.path.dirname(os.path.abspath(__file__))

    def test_csv_read(self):
        filepath = self.BASE_PATH + "/mockups/concessionario.csv"
        processor = TextProcessor()
        processor.read_csv(filepath)

    def test_csv_writter(self):
        filepath = self.BASE_PATH + "/mockups/concessionario.csv"
        processor = TextProcessor()
        processor.read_csv(filepath)

        processor.write_csv(filepath)

    def test_json_reader(self):
        filepath = self.BASE_PATH + "/mockups/concessionario.json"
        processor = TextProcessor()
        processor.read_json(filepath)

    def test_json_writer(self):
        filepath = self.BASE_PATH + "/mockups/nuovo_json.json"
        processor = TextProcessor()
        to_parse = {
            "nome": "Silvia",
            "cognome": "Rossi",
            "admin": False,
            "mascote": 5,
            "figli": {
                "femmine": ["Clara", "Francesca"],
                "maschi": []
            } 
        }
        processor.write_json(filepath, to_parse)

    def test_yalm_reader(self):
        filepath = self.BASE_PATH + "/mockups/concessionario.yml"
        processor = TextProcessor()
        processor.read_yaml(filepath)

    def test_yalm_writer(self):
        filepath = self.BASE_PATH + "/mockups/nuovo_yaml.yml"
        processor = TextProcessor()
        to_parse = {
            "nome": "Silvia",
            "cognome": "Rossi",
            "admin": False,
            "mascote": 5,
            "figli": {
                "femmine": ["Clara", "Francesca"],
                "maschi": []
            } 
        }
        processor.write_yaml(filepath, to_parse)

    def test_read_xml(self):
        filepath = self.BASE_PATH + "/mockups/concessionario.xml"
        processor = TextProcessor()
        processor.read_xml(filepath)

        processor.modify_xml(filepath)