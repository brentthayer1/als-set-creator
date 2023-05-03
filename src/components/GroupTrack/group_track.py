import os.path
import xml.etree.ElementTree as ET

TEMPLATE_PATH = f"{os.getcwd()}/src/components/GroupTrack/GroupTrack.xml"


class GroupTrack:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.template = os.path.abspath(TEMPLATE_PATH)
        self.tree = ET.parse(self.template)
        self.root = self.tree.getroot()
        self.set_id(id)
        self.set_name(name)

    def set_id(self, id):
        self.root.set("Id", str(id))

    def set_attribute(self, tag, attribute, value):
        child = self.root.find(tag)
        child.set(attribute, value)

    def set_name(self, name):
        self.set_attribute("Name/EffectiveName", "Value", name)
        self.set_attribute("Name/UserName", "Value", name)

    # def ET_to_string(self):
    #     return ET.tostring(self.tree.getroot()).decode("utf8")


if __name__ == "__main__":
    pass
