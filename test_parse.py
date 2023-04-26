from xml.etree import ElementTree as ET
from typing import Dict, Literal, Optional, Tuple, Union, overload

# from ableton_track import AbletonTrack
import gzip

from utils import *
from ableton_track import *

# root = et.fromstring(
#     command_request
# )  # fromString parses xml from string to an element, command request can be xml request string
# root.find(
#     "cat"
# ).text = (
#     "dog"  # find the element tag as cat and replace it with the string to be replaced.
# )
# et.tostring(root)


class AbletonSet:
    def __init__(self, xml_data):
        self.root = ET.fromstring(xml_data)
        self.tracks = self.get_tracks()
        self.master_track = self.get_master_track()

    def get_track_type(self, track):
        track_type = track.tag
        if track_type == "MidiTrack":
            return MidiTrack(track)
        elif track_type == "AudioTrack":
            return AudioTrack(track)
        elif track_type == "GroupTrack":
            return GroupTrack(track)
        else:
            return Track(track)

    def get_tracks(self):
        tracks = get_element(self.root, "LiveSet.Tracks")
        track_list = []
        for track in tracks:
            track_type = self.get_track_type(track)
            track_list.append(track_type)

        track_dict = {}
        for track in track_list:
            if track.track_type not in track_dict:
                track_dict[track.track_type] = [track]
            else:
                track_dict[track.track_type].append(track)

        return track_dict

    def get_master_track(self):
        master_track = get_element(self.root, "LiveSet.MasterTrack")
        return AbletonTrack(master_track)

    def compile_xml(self):
        header = '<?xml version="1.0" encoding="UTF-8"?>\n'.encode("utf-8")
        footer = "\n".encode("utf-8")
        body = ET.tostring(self.root, encoding="utf-8")
        return header + body + footer


if __name__ == "__main__":
    path = "/Users/brentthayer/Desktop/set_creator Project/set_creator.als"
    path2 = "/Users/brentthayer/Desktop/set_creator Project/set_creatorTESTER.als"

    xml_data = als_to_xml(path)

    ableton_set = AbletonSet(xml_data)

    counter = 0

    for track in ableton_set.tracks["AudioTrack"]:
        track.set_name(f"TEST TRACK {counter}")
        counter += 1

    xml_output = ableton_set.compile_xml()

    xml_to_als(xml_output, path2)


# print(lst[0].type)
# print(lst[0].name)
# print(lst[0].id)
# print(lst[0].group_id)

# print(dir(lst[0]))
