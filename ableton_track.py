from utils import *
from xml.etree import ElementTree as ET


class Track(object):
    def __init__(self, track_root: ET.Element):
        self.track_root = track_root
        self.track_id = self.get_track_id()
        self.track_group_id = self.get_track_group_id()
        self.set_name()

    def get_track_id(self):
        return self.track_root.get("Id")

    def get_track_group_id(self):
        return get_element(self.track_root, "TrackGroupId", attribute="Value")

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


class MidiTrack(Track):
    def __init__(self, track_root: ET.Element):
        super().__init__(track_root)
        self.track_type = "MidiTrack"


class AudioTrack(Track):
    def __init__(self, track_root: ET.Element):
        super().__init__(track_root)
        self.track_type = "AudioTrack"


class GroupTrack(Track):
    def __init__(self, track_root: ET.Element):
        super().__init__(track_root)
        self.track_type = "GroupTrack"
