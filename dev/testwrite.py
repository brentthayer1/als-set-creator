import os
from xml.etree import ElementTree as ET
import gzip


# with open("new_set.xml", "rb") as f:
#     xml = f.read()


# with gzip.open("TESTER.als", "wb") as new_als_file:
#     new_als_file.write(xml)


# def xml_to_als(xml_data, xml_file_path):
#     new_als_path = os.path.splitext(xml_file_path)[0] + "TESTER.als"
#     with gzip.open(new_als_path, "wb") as new_als_file:
#         new_als_file.write(xml_data)


# def als_to_xml(als_file_path):
#     with open(als_file_path, "rb") as als_file:
#         als_data = als_file.read()
#         xml_data = gzip.decompress(als_data).decode()
#         return xml_data


path = "../../testproject/TESTPROJECT.als"

with open(path, "rb") as als_file:
    als_data = als_file.read()
    xml_data = gzip.decompress(als_data).decode()

with open("new_set.xml", "w") as f:
    f.write(xml_data)


def compile_xml(self):
    header = '<?xml version="1.0" encoding="UTF-8"?>\n'.encode("utf-8")
    footer = "\n".encode("utf-8")
    body = ET.tostring(self.root, encoding="utf-8")
    return header + body + footer
