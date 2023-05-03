import os.path
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
from xml.dom import minidom
from typing import List
import yaml
from dataclasses import dataclass

import os
import sys

sys.path.append(f"{os.getcwd()}/src/components/")
from AudioTrack.audio_track import AudioTrack


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


# def parse_returns(returns):
#     return_tracks = []
#     for return_track in returns:
#         return_tracks.append(AudioTrack(return_track["name"], return_track["id"], return_track["group_id"], return_track["sends"]))
#     return return_tracks


def parse_tracks(tracks):
    # audio_tracks = []
    # for track in tracks:
    #     audio_track = AudioTrack(
    #         track["ame"], track["id"], track["group_id"], track["sends"]
    #     )
    #     name, id, group_id, sends
    # return audio_tracks
    pass


@dataclass
class TracksConfigObject:
    path: str
    send: int


@dataclass
class SongConfigObject:
    id: int
    name: str
    path: str
    cues: str
    tracks: List[TracksConfigObject]


@dataclass
class SongsConfigObject:
    cues_path: str
    tracks_path: str
    songs: List[SongConfigObject]


@dataclass
class ReturnConfigObject:
    id: int
    name: str


@dataclass
class ConfigObject:
    songs: SongsConfigObject
    returns: ReturnConfigObject


def parse_config(yaml_config):
    with open(yaml_config, "r") as f:
        yaml_data = yaml.safe_load(f)

    exclude_keys = ["CuesPath", "TracksPath"]
    songs = {
        k: yaml_data["Songs"][k]
        for k in set(list(yaml_data["Songs"].keys())) - set(exclude_keys)
    }
    songs_list = []
    for song_num, song_info in songs.items():
        tracks_list = []
        for path, send in song_info["Tracks"].items():
            tracks_list.append(TracksConfigObject(path=path, send=send))

        song_config = SongConfigObject(
            id=song_num,
            name=song_info["Name"],
            path=song_info["Path"],
            cues=song_info["Cues"],
            tracks=tracks_list,
        )
        songs_list.append(song_config)

    song_config = SongsConfigObject(
        cues_path=yaml_data["Songs"]["CuesPath"],
        tracks_path=yaml_data["Songs"]["TracksPath"],
        songs=songs_list,
    )

    return_list = []
    for id, name in yaml_data["Returns"].items():
        return_config = ReturnConfigObject(id=id, name=name)
        return_list.append(return_config)

    return ConfigObject(songs=song_config, returns=return_list)


if __name__ == "__main__":
    config = parse_config("set-up.yaml")

    print(config.songs.songs[0].tracks[0].path)

    # print(config.songs)
    # print(config.returns)

    # tracks = [
    #     AudioTrack("test1", 1, 1, 1),
    #     AudioTrack("test2", 2, 2, 1),
    # ]
    # live_set = LiveSet(tracks, None, None)
    # print(live_set.ET_to_string())

    # print(live_set)

    # print(live_set.tracks[0].ET_to_string())

    # live_set.add_tracks(tracks)

    # body = ET.tostring(live_set.root, encoding="utf-8")

    # with open("tester_set.xml", "w") as f:
    #     f.write(body)
