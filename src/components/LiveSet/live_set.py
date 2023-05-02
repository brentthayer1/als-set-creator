import os.path
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
import xml
from xml.dom import minidom


import sys

sys.path.append(f"{os.getcwd()}/src/components/")
from AudioTrack.audio_track import AudioTrack


# root = tree.getroot()

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
        for track in tracks:
            tracks_element.append(track.tree.getroot())
        tracks_tree = ET.ElementTree(tracks_element)
        self.root.append(tracks_tree.getroot())

        

    # def populate_live_set(self):
    #     self.add_tracks()

    def ET_to_string(self):
        reparsed = minidom.parseString(ET.tostring(self.tree.getroot()).decode("utf8"))
        return reparsed.toprettyxml(indent="\t")
    


if __name__ == "__main__":
    tracks = [
        AudioTrack("test1", 1, 1, 1),
        AudioTrack("test2", 2, 2, 1),
    ]
    live_set = LiveSet(tracks, None, None)
    print(live_set.ET_to_string())
    
    # print(live_set)

    # print(live_set.tracks[0].ET_to_string())

    # live_set.add_tracks(tracks)

    # body = ET.tostring(live_set.root, encoding="utf-8")

    # with open("tester_set.xml", "w") as f:
    #     f.write(body)
