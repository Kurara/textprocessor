import csv
import json
import xml.etree.ElementTree as ET


class TextProcessor:
    """ Classe che processa diversi tipi di file e salva i dati in una lista

    list_rows (list): Lista dei dati processati
    """

    def read_csv(self, file):
        self.list_rows = []
        with open(file, 'r') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                print(row)

    def write_csv(self, file):
        header = [
            "macchina",
            "modello",
            "acquisizione",
            "prezzo compra",
            "prezzo vendita",
            "beneficio"
        ]
        with open(file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=header)
            writer.writeheader()
            for row in self.list_rows:
                writer.writerow(row)
            writer.writerow({
                "macchina": "aggiunta dopo",
                "modello": "non so",
                "acquisizione": "oggi",
                "prezzo compra": "gratis",
                "prezzo vendita": "10.000",
                "beneficio": None
            })
            # writer.writerows(self.list_rows)
            
    def read_json(self, file):
        with open(file, 'r') as jsonfile:
            dict_values = json.loads(jsonfile.read())
        return dict_values

    def write_json(self, file, py_dict):
        import datetime
        today = py_dict.get('creato')
        py_dict['creato'] = today.isoformat()
        json_str = json.dumps(py_dict, indent=3)
        with open(file, 'w') as jsonfile:
            jsonfile.write(json_str)

    def read_xml_categorie(self, file):
        total_categories = []

        tree = ET.parse(file)
        rss_root = tree.getroot()
        channel = rss_root.getchildren()[0]
        items = channel.findall('item')

        for item in items:
            cat_element = item.find('category')
            category = cat_element.text
            if category not in total_categories:
                total_categories.append(category)

        return total_categories
        
    def read_xml_urls(self, file):
        total_urls = []

        tree = ET.parse(file)
        rss_root = tree.getroot()
        channel = rss_root.getchildren()[0]
        items = channel.findall('item')

        for item in items:
            enclosure = item.find('enclosure')
            url = enclosure.get('url')
            if url not in total_urls:
                total_urls.append(url)

        return total_urls

    def write_xml(self, file, py_dict):
        """ Scrive i dati di una lista di dict in un file xml

        Args:
            file (str): Path thel file a salvare
            py_dict (list): Lista di dictionary python

        """
        root = ET.Element("root")
        _prezzi = {}
        
        for item in py_dict:
            doc = ET.SubElement(root, "elemento")
            for key, value in item.items():
                # if "prezzo" in key:
                #     _prezzi[key.replace("prezzo ", '')] = value
                # else:
                ET.SubElement(doc, key.replace(' ', '_')).text = value
            # ET.SubElement(doc, "prezzi", compra=_prezzi.get('compra'), vendita=_prezzi.get('vendita'))

        tree = ET.ElementTree(root)
        tree.write(file)

    def pretty_print(self, xml_file):
        import xml.dom.minidom

        dom = xml.dom.minidom.parse(xml_file)
        pretty_xml_as_string = dom.toprettyxml()

        with open(xml_file, 'w') as f:
            f.write(pretty_xml_as_string)
        