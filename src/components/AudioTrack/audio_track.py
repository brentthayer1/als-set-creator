import os.path
import xml.etree.ElementTree as ET

TEMPLATE_PATH = f"{os.getcwd()}/src/components/AudioTrack/AudioTrack.xml"


class AudioTrack:
    def __init__(self, name, id, group_id, sends):
        self.name = name
        self.id = id
        self.group_id = group_id
        self.sends = sends
        self.template = os.path.abspath(TEMPLATE_PATH)
        self.tree = ET.parse(self.template)
        self.root = self.tree.getroot()
        # print(self.root)

    def ET_to_string(self):
        return ET.tostring(self.tree.getroot()).decode("utf8")


if __name__ == "__main__":
    track = AudioTrack("test", 1, 1, 1)
    # print(track.root)
