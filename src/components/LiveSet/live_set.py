import os.path
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
import xml


import sys

sys.path.append(f"{os.getcwd()}/src/components/")
from AudioTrack.audio_track import AudioTrack


# root = tree.getroot()

TEMPLATE_PATH = f"{os.getcwd()}/src/components/LiveSet/LiveSet.xml"


class LiveSet:
    def __init__(self, tracks, master_track, locators):
        self.add_tracks(tracks)
        self.master_track = master_track
        self.locators = locators
        self.template = os.path.abspath(TEMPLATE_PATH)
        self.tree = ET.parse(self.template)
        self.root = self.tree.getroot()

    def add_tracks(self, tracks):
        tracks_root = ET.ElementTree("Tracks")

        for track in tracks:
            trak_str = track.ET_to_string()

            tracks_root.append(ET.fromstring(trak_str))

        print(ET.tostring(tracks_root.getroot()))

        root = ET.Element("root")

        # create a sub-element tree
        subtree = ET.Element("subtree")
        subtree_sub1 = ET.SubElement(subtree, "subtree_sub1")
        subtree_sub2 = ET.SubElement(subtree, "subtree_sub2")
        subtree_sub2.text = "Hello World!"

        # append the sub-element tree to the root element
        root.append(subtree)

        # self.tree.append(
        #     ET.fromstring(ET.tostring(tracks_root.getroot()).decode("utf8"))
        # )

        # new = xml.Element('newElement')
        # self.root.append(new)
        # xml.SubElement(new,xml.Element(self.XMLEntriesList['RiverCallPower']))

        # print(track_list[0])

        # root = ET.Element("Tracks")
        # for t in track_list:
        #     root.append(t)
        #     nm = xml.SubElement(t, "name")
        # nm.text = student.get('name')
        # age = xml.SubElement(child, "age")
        # age.text = str(student.get('age'))
        # sal=xml.SubElement(child, "sal")
        # sal.text=str(student.get('sal'))

        # tree = et.ElementTree(root)
        # with open('employees.xml', "wb") as fh:
        # tree.write(fh)

    # def populate_live_set(self):
    #     self.add_tracks()

    def ET_to_string(self):
        return ET.tostring(self.tree.getroot()).decode("utf8")


if __name__ == "__main__":
    tracks = [
        AudioTrack("test", 1, 1, 1),
    ]
    live_set = LiveSet(tracks, None, None)
    # print(live_set)

    # print(live_set.tracks[0].ET_to_string())

    # live_set.add_tracks(tracks)

    # body = ET.tostring(live_set.root, encoding="utf-8")

    # with open("tester_set.xml", "w") as f:
    #     f.write(body)
