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
# from MidiTrack.midi_track import MidiTrack
from LiveSet.live_set import LiveSet


sys.path.append(f"{os.getcwd()}/src/utils/")
from ConfigParser.config_parser import YamlConfigParser


def create_return_tracks(config):
    return_tracks = []
    for return_track in config.returns:
        return_track = ReturnTrack(
            name=return_track.name,
            id=return_track.id*1000,
        )
        return_tracks.append(return_track)
    return return_tracks


def create_group_tracks(config):
    group_tracks = []
    for song in config.songs.songs:
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
        
        group_id = song.id
        song_id = group_id + 1

        # midi_tracks.append(MidiTrack())

        for track in song.tracks:
            audio_track = AudioTrack(
                name=track.path.split(".")[0],
                path=tracks_path + track.path,
                id=song_id,
                group_id=group_id,
                sends=track.send,
            )
            audio_tracks.append(audio_track)
            song_id += 1
    return audio_tracks, midi_tracks


def create_tracks(config):
    audio_midi_tracks = create_audio_and_midi_tracks(config)
    return {
        "audio_tracks": audio_midi_tracks[0],
        "midi_tracks": audio_midi_tracks[1],
        "return_tracks": create_return_tracks(config),
        "group_tracks": create_group_tracks(config),
    }


def main():
    parser = YamlConfigParser()
    config = parser.parse("set-up.yaml")
    tracks = create_tracks(config)

    live_set = LiveSet(tracks, None, None)
    print(live_set.ET_to_string())

    # print(live_set)

    # print(live_set.tracks[0].ET_to_string())

    # live_set.add_tracks(tracks)

    # body = ET.tostring(live_set.root, encoding="utf-8")

    # with open("tester_set.xml", "w") as f:
    #     f.write(body)
