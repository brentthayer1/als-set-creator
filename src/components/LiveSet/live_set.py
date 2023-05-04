import os.path
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
from xml.dom import minidom

import os
import sys

sys.path.append(f"{os.getcwd()}/src/components/")


from AudioTrack.audio_track import AudioTrack

sys.path.append(f"{os.getcwd()}/src/utils/")
from ConfigParser.config_parser import YamlConfigParser


TEMPLATE_PATH = f"{os.getcwd()}/src/components/LiveSet/LiveSet.xml"


class LiveSet:
    def __init__(self, tracks, master_track, locators):
        # self.master_track = master_track
        # self.locators = locators
        self.template = os.path.abspath(TEMPLATE_PATH)
        self.tree = ET.parse(self.template)
        self.root = self.tree.getroot()
        self.add_tracks(tracks)

    def add_tracks(self, tracks):
        tracks_element = ET.Element("Tracks")
        for track in tracks["group_tracks"]:
            tracks_element.append(track.tree.getroot())
        for track in tracks["audio_tracks"]:
            tracks_element.append(track.tree.getroot())
        # for track in tracks["midi_tracks"]:
        #     tracks_element.append(track.tree.getroot())
        # for track in tracks["return_tracks"]:
        #     tracks_element.append(track.tree.getroot())
        tracks_tree = ET.ElementTree(tracks_element)
        self.root.append(tracks_tree.getroot())

    def ET_to_string(self):
        reparsed = minidom.parseString(ET.tostring(self.tree.getroot()).decode("utf8"))
        return reparsed.toprettyxml(indent="\t")

    def compile_xml(self):
        header = '<?xml version="1.0" encoding="UTF-8"?>\n<Ableton MajorVersion="5" MinorVersion="11.0_11202" SchemaChangeCount="17" Creator="Ableton Live 11.2.11" Revision="6e9e7c6913378fcbbe8b18e3fd8f33d0755968b8">'.encode(
            "utf-8"
        )
        footer = "</Ableton>\n".encode("utf-8")
        newline = "\n".encode("utf-8")
        body = ET.tostring(self.root, encoding="utf-8")
        return header + body + footer + newline


if __name__ == "__main__":
    pass
