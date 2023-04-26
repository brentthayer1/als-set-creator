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
        return Track(master_track)

    def compile_xml(self):
        header = '<?xml version="1.0" encoding="UTF-8"?>\n'.encode("utf-8")
        footer = "\n".encode("utf-8")
        body = ET.tostring(self.root, encoding="utf-8")
        return header + body + footer
