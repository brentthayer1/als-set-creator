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
        for track in tracks["midi_tracks"]:
            tracks_element.append(track.tree.getroot())
        for track in tracks["return_tracks"]:
            tracks_element.append(track.tree.getroot())
        tracks_tree = ET.ElementTree(tracks_element)
        self.root.append(tracks_tree.getroot())

    def ET_to_string(self):
        reparsed = minidom.parseString(ET.tostring(self.tree.getroot()).decode("utf8"))
        return reparsed.toprettyxml(indent="\t")


if __name__ == "__main__":
    pass
