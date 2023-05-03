from typing import List
import yaml
from dataclasses import dataclass


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


class YamlConfigParser:
    def __init__(self):
        self.exclude_keys = ["CuesPath", "TracksPath"]

    def load_yaml(self, yaml_config):
        with open(yaml_config, "r") as f:
            yaml_data = yaml.safe_load(f)
        self.yaml_data = yaml_data

    def parse_songs(self):
        self.songs = {
            k: self.yaml_data["Songs"][k]
            for k in set(list(self.yaml_data["Songs"].keys())) - set(self.exclude_keys)
        }

    def set_tracks_list(self, song_info):
        tracks_list = []
        for path, send in song_info["Tracks"].items():
            tracks_list.append(TracksConfigObject(path=path, send=send))
        return tracks_list

    def set_songs_list(self):
        self.songs_list = []
        for song_num, song_info in self.songs.items():
            tracks_list = self.set_tracks_list(song_info)
            song_config = SongConfigObject(
                id=song_num*100,
                name=song_info["Name"],
                path=song_info["Path"],
                cues=song_info["Cues"],
                tracks=tracks_list,
            )
            self.songs_list.append(song_config)

    def set_songs_config(self):
        self.songs_config = SongsConfigObject(
            cues_path=self.yaml_data["Songs"]["CuesPath"],
            tracks_path=self.yaml_data["Songs"]["TracksPath"],
            songs=self.songs_list,
        )

    def set_returns_list(self):
        self.return_list = []
        for id, name in self.yaml_data["Returns"].items():
            return_config = ReturnConfigObject(id=id, name=name)
            self.return_list.append(return_config)

    def set_config(self):
        self.config = ConfigObject(songs=self.songs_config, returns=self.return_list)

    def parse(self, yaml_config):
        self.load_yaml(yaml_config)
        self.parse_songs()
        self.set_songs_list()
        self.set_songs_config()
        self.set_returns_list()
        self.set_config()
        return self.config


if __name__ == "__main__":
    pass
