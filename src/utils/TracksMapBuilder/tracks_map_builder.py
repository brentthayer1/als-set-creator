# import os
# import sys
# import gzip

# import os.path
# import xml.etree.ElementTree as ET
# from xml.etree.ElementTree import Element
# from xml.dom import minidom


# sys.path.append(f"{os.getcwd()}/src/components/")
# from AudioTrack.audio_track import AudioTrack
# from ReturnTrack.return_track import ReturnTrack
# from GroupTrack.group_track import GroupTrack

# # from MidiTrack.midi_track import MidiTrack
# from LiveSet.live_set import LiveSet


# sys.path.append(f"{os.getcwd()}/src/utils/")
# from ConfigParser.config_parser import YamlConfigParser


# class TracksMapBuilder:
#     def __init__(self, config):
#         self.config = config

#     def create_return_tracks(self):
#         return_tracks = []
#         for return_track in self.config.returns:
#             return_track = ReturnTrack(
#                 name=return_track.name,
#                 id=return_track.id * 1000,
#             )
#             return_tracks.append(return_track)
#         return return_tracks


# def create_group_tracks(self):
#     group_tracks = []
#     for song in self.config.songs.songs:
#         group_track = GroupTrack(
#             name=song.name,
#             id=song.id,
#         )
#         group_tracks.append(group_track)
#     return group_tracks


# def create_audio_and_midi_tracks(self):
#     cues_path = self.config.songs.cues_path
#     tracks_path = self.config.songs.tracks_path
#     songs = self.config.songs.songs

#     audio_tracks = []
#     midi_tracks = []

#     for song in songs:
#         group_id = song.id
#         song_id = group_id + 1

#         # midi_tracks.append(MidiTrack())

#         for track in song.tracks:
#             audio_track = AudioTrack(
#                 name=track.path.split(".")[0],
#                 path=tracks_path + song.path + track.path,
#                 id=song_id,
#                 group_id=group_id,
#                 sends=track.send,
#             )
#             audio_tracks.append(audio_track)
#             song_id += 1
#     return audio_tracks, midi_tracks


# def create_tracks(self):
#     audio_midi_tracks = self.create_audio_and_midi_tracks(self.config)
#     return {
#         "audio_tracks": audio_midi_tracks[0],
#         # "midi_tracks": audio_midi_tracks[1],
#         # "return_tracks": create_return_tracks(config),
#         "group_tracks": self.create_group_tracks(self.config),
#     }
