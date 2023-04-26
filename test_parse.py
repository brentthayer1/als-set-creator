from xml.etree import ElementTree as ET
from typing import Dict, Literal, Optional, Tuple, Union, overload

# from ableton_track import AbletonTrack
import gzip

from utils import *

# root = et.fromstring(
#     command_request
# )  # fromString parses xml from string to an element, command request can be xml request string
# root.find(
#     "cat"
# ).text = (
#     "dog"  # find the element tag as cat and replace it with the string to be replaced.
# )
# et.tostring(root)


class AbletonTrack(object):
    def __init__(self, track_root: ET.Element, version: Tuple[int, int, int]):
        self.track_root = track_root
        self.set_name()
        # self.id = track_root.get("Id")
        # self.group_id = get_element(track_root, "TrackGroupId", attribute="Value")

    def set_name(self, value=None):
        if not value:
            self.name = get_element(self.track_root, "Name.UserName", attribute="Value")
            if not self.name:
                self.name = get_element(
                    self.track_root, "Name.EffectiveName", attribute="Value"
                )
        else:
            self.root = set_element(
                self.track_root, "Name.UserName", attribute="Value", value=value
            )
            self.root = set_element(
                self.track_root, "Name.EffectiveName", attribute="Value", value=value
            )
            self.name = get_element(self.track_root, "Name.UserName", attribute="Value")


class AbletonSet:
    def __init__(self, xml_data):
        self.root = ET.fromstring(xml_data)
        self.tracks = self.load_tracks()

    def load_tracks(self):
        tracks = get_element(self.root, "LiveSet.Tracks")
        track_list = []
        for track in tracks:
            track_list.append(AbletonTrack(track, (11, 2, 11)))

        return track_list

    def compile_xml(self):
        header = '<?xml version="1.0" encoding="UTF-8"?>\n'.encode("utf-8")
        footer = "\n".encode("utf-8")
        body = ET.tostring(self.root, encoding="utf-8")
        return header + body + footer


if __name__ == "__main__":
    root = None

    path = "/Users/brentthayer/Desktop/set_creator Project/set_creator.als"
    path2 = "/Users/brentthayer/Desktop/set_creator Project/set_creatorTESTER.als"

    xml_data = als_to_xml(path)

    ableton_set = AbletonSet(xml_data)

    counter = 0

    for track in ableton_set.tracks:
        print(track.name)
        track.set_name(f"TEST TRACK {counter}")
        counter += 1

    xml_output = ableton_set.compile_xml()

    xml_to_als(xml_output, path2)


# print(lst[0].type)
# print(lst[0].name)
# print(lst[0].id)
# print(lst[0].group_id)

# print(dir(lst[0]))
