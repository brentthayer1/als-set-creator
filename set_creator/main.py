import os
import sys

import os.path
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
from xml.dom import minidom


sys.path.append(f"{os.getcwd()}/src/components/")
from AudioTrack.audio_track import AudioTrack
from ReturnTrack.return_track import ReturnTrack
from GroupTrack.group_track import GroupTrack
from LiveSet.live_set import LiveSet


sys.path.append(f"{os.getcwd()}/src/utils/")
from ConfigParser.config_parser import YamlConfigParser


def create_return_tracks(config):
    return_tracks = []
    for return_track in config.returns:
        return_track = ReturnTrack(
            name=return_track.name,
            id=return_track.id,
        )
        return_tracks.append(return_track)
    return return_tracks


def create_group_tracks(config):
    group_tracks = []
    for song in config.songs:
        group_track = GroupTrack(
            name=song.name,
            id=song.id,
        )
        group_tracks.append(group_track)
    return group_tracks


def create_audio_and_midi_tracks(config):
    cues_path = config.songs.cues_path
    tracks_path = config.songs.tracks_path
    songs = config.songs.songs

    audio_tracks = []
    midi_tracks = []

    for song in songs:
        for track in song.tracks:
            audio_track = AudioTrack(
                name=f"testname{song.id}",
                path=song.path + track.path,
                id=1,
                group_id=song.id,
                sends=track.send,
            )
            audio_tracks.append(audio_track)


def create_tracks(config):
    tracks = {
        "audio_tracks": [],
    }


def main():
    parser = YamlConfigParser()
    config = parser.parse("set-up.yaml")
    # return_tracks = create_return_tracks(config)
    # group_tracks = create_group_tracks(config)
    # print(return_tracks)

    create_audio_and_midi_tracks(config)
    # print(config)

    # live_set = LiveSet(tracks, None, None)
    # print(live_set.ET_to_string())

    # print(live_set)

    # print(live_set.tracks[0].ET_to_string())

    # live_set.add_tracks(tracks)

    # body = ET.tostring(live_set.root, encoding="utf-8")

    # with open("tester_set.xml", "w") as f:
    #     f.write(body)
