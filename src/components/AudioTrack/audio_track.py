import os.path
import xml.etree.ElementTree as ET
import os
import sys

# sys.path.append(f"{os.getcwd()}/src/components/")

# from AudioClip.audio_clip import AudioClip

TEMPLATE_PATH = f"{os.getcwd()}/src/components/AudioTrack/AudioTrack.xml"
# NOTE: The amount of return tracks need to also change the send tracks.


class AudioTrack:
    def __init__(self, name, path, id, group_id, sends):
        self.name = name
        self.path = path
        self.id = id
        self.group_id = group_id
        self.sends = sends
        self.template = os.path.abspath(TEMPLATE_PATH)
        self.tree = ET.parse(self.template)
        self.root = self.tree.getroot()
        self.set_id(id)
        self.set_name(name)
        self.set_group_id(group_id)
        self.set_path(path)

    def set_id(self, id):
        self.root.set("Id", str(id))

    def set_attribute(self, tag, attribute, value):
        child = self.root.find(tag)
        child.set(attribute, value)

    def set_name(self, name):
        self.set_attribute("Name/EffectiveName", "Value", name)
        self.set_attribute("Name/UserName", "Value", name)

    def set_group_id(self, group_id):
        self.set_attribute("TrackGroupId", "Value", str(group_id))

    def set_path(self, path):
        self.set_attribute(
            "DeviceChain/MainSequencer/Sample/ArrangerAutomation/Events/AudioClip/SampleRef/FileRef/RelativePath",
            "Value",
            path,
        )
        self.set_attribute(
            "DeviceChain/MainSequencer/Sample/ArrangerAutomation/Events/AudioClip/SampleRef/FileRef/Path",
            "Value",
            path,
        )

    def ET_to_string(self):
        return ET.tostring(self.tree.getroot()).decode("utf8")


if __name__ == "__main__":
    pass
