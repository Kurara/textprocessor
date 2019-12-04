import csv
import json
import yaml
import xml.etree.ElementTree as ET


class TextProcessor:

    def read_csv(self, file):
        self.list_rows = []
        with open(file, 'r') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                self.list_rows.append(row)


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
                row['prezzo vendita'] = int(row['prezzo compra']) + int(row['beneficio'])
                writer.writerow(row)
            # writer.writerows(self.list_rows)
            
    def read_json(self, file):
        # to_load = "{'machinaria': 'si'}"
        with open(file, 'r') as jsonfile:
            dict_values = json.loads(jsonfile.read())
        print(dict_values)

    def write_json(self, file, py_dict):
        json_str = json.dumps(py_dict, indent=3)
        with open(file, 'w') as jsonfile:
            jsonfile.write(json_str)

    def read_yaml(self, file):
        # to_load = "{'machinaria': 'si'}"
        with open(file, 'r') as jsonfile:
            dict_values = yaml.load(jsonfile.read())
        print(dict_values)

    def write_yaml(self, file, py_dict):
        json_str = yaml.dump(py_dict, indent=3)
        with open(file, 'w') as jsonfile:
            jsonfile.write(json_str)

    def read_xml(self, file):
        tree = ET.parse(file)
        root = tree.getroot()
        machine = root.getchildren()

    def modify_xml(self, file):
        tree = ET.parse(file)
        root = tree.getroot()
        machine = root.findall("macchina")
        for machina in machine:
            prezzi = machina.find("prezzi").attrib
            prezzo_iniziale = prezzi.get('compra')
            benefici = machina.find("benefici")
            try:
                prezzo_iniziale = int(prezzo_iniziale)
                benefici_int = int(benefici.text)
            except Exception:
                prezzo_iniziale = 0
            prezzo_finale = prezzo_iniziale + benefici_int
            machina.find("prezzi").set('vendita', str(prezzo_finale))
        tree.write(file)

    def write_xml(self, file, py_dict):
        root = ET.Element("root")
        
        for item in py_dict:
            doc = ET.SubElement(root, "macchina", name=item.get('macchina'))

            ET.SubElement(doc, "modello").text = item.get('modello')
            ET.SubElement(doc, "acquisizione").text = item.get('acquisizione')
            sell_price = int(item.get('prezzo compra')) + int(item.get('beneficio'))
            ET.SubElement(doc, "prezzi", compra=item.get('prezzo compra'), vendita=str(sell_price))
            ET.SubElement(doc, "benefici").text = item.get('beneficio')

            tree = ET.ElementTree(root)
            tree.write(file)

    def pretty_print(self, xml_file):
        import xml.dom.minidom

        dom = xml.dom.minidom.parse(xml_file)
        pretty_xml_as_string = dom.toprettyxml()

        with open(xml_file, 'w') as f:
            f.write(pretty_xml_as_string)