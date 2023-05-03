from xml.etree import ElementTree as ET

import yaml
from pathlib import Path


# from ableton_track import AbletonTrack
import gzip

from utils import *
from dev.ableton_track import *


class AbletonSet:
    def __init__(self, config):
        self.config = config
        self.returns = self.set_returns()

    def set_returns(self):
        return self.config["Returns"]


if __name__ == "__main__":
    # config = yaml.safe_load(Path("set-up.yaml").read_text())
    # ableton_set = AbletonSet(config)

    # print(ableton_set.config)

    import xml.etree.ElementTree as ET
    import yaml

    # Read the YAML file
    with open("set-up.yaml", "r") as f:
        data = yaml.safe_load(f)
        print(data)

    # Create a new XML element with the LiveSet root element
    liveset = ET.Element("LiveSet")

    info = ET.SubElement(liveset, "Info")
    info.set("Tempo", "120")
    info.set("Signature", "4/4")

    # Loop over the tracks and create a new GroupTrack element for each one
    group_tracks = []
    for track_data in data["Tracks"]:
        group_track = ET.SubElement(liveset, "GroupTrack")
        group_track.set("Name", track_data["Name"])
        group_tracks.append(group_track)

        # Loop over the elements and create a new AudioTrack element for each one
        for element in track_data["Elements"]:
            audio_track = ET.SubElement(liveset, "AudioTrack")
            audio_track.set("Name", element[:-4])  # remove the .wav extension
            audio_track.set("GroupTrackID", str(group_track.get("Id")))

    # Write the XML data to a file
    # with open("new_set.xml", "wb") as f:
    #     header = '<?xml version="1.0" encoding="UTF-8"?>\n<Ableton MajorVersion="5" MinorVersion="11.0_433" SchemaChangeCount="6" Creator="Ableton Live 11.0.12" Revision="b232c5df34c47e19f055f82f14a99f5af33b3a5c">\n'.encode(
    #         "utf-8"
    #     )
    #     footer = "</Ableton>\n".encode("utf-8")
    #     body = ET.tostring(liveset, encoding="utf-8")
    #     new_xml = header + body + footer
    #     # f.write(new_xml)

    with open("new_set.xml", "r") as f:
        header = '<?xml version="1.0" encoding="UTF-8"?>\n<Ableton MajorVersion="5" MinorVersion="11.0_433" SchemaChangeCount="6" Creator="Ableton Live 11.0.12" Revision="b232c5df34c47e19f055f82f14a99f5af33b3a5c">\n'.encode(
            "utf-8"
        )
        footer = "</Ableton>\n".encode("utf-8")
        body = ET.tostring(liveset, encoding="utf-8")
        new_xml = header + body + footer

        path2 = "new_set.xml"
        xml_to_als(new_xml, path2)

    # path = "/Users/brentthayer/Desktop/set_creator Project/set_creator.als"
    # path2 = "/Users/brentthayer/Desktop/set_creator Project/set_creatorTESTER.als"

    # xml_data = als_to_xml(path)

    # ableton_set = AbletonSet(xml_data)

    # counter = 0

    # for track in ableton_set.tracks["AudioTrack"]:
    #     track.set_name(f"TEST TRACK {counter}")
    #     counter += 1

    # xml_output = ableton_set.compile_xml()

    # xml_to_als(xml_output, path2)


# print(lst[0].type)
# print(lst[0].name)
# print(lst[0].id)
# print(lst[0].group_id)

# print(dir(lst[0]))
