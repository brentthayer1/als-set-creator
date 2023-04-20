from xml.etree import ElementTree as ET
from typing import Dict, Literal, Optional, Tuple, Union, overload

from ableton_track import AbletonTrack
import gzip


@overload
def get_element(
    root: ET.Element,
    attribute_path: str,
    *,
    silent_error: Literal[False],
    attribute: Literal[None] = None,
):
    ...


@overload
def get_element(
    root: ET.Element,
    attribute_path: str,
    *,
    silent_error: Literal[True],
    attribute: Literal[None] = None,
):
    ...


@overload
def get_element(
    root: ET.Element,
    attribute_path: str,
    *,
    silent_error: Literal[False] = False,
    attribute: str,
):
    ...


def get_element(
    root: ET.Element,
    attribute_path: str,
    *,
    silent_error: bool = False,
    attribute: Optional[str] = None,
):
    """Get element using Element tree xpath syntax."""
    element = root.findall(f"./{'/'.join(attribute_path.split('.'))}")
    if not element:
        if silent_error:
            return None
        # ElementTree.dump(root)
        raise  # ElementNotFound(f"{R}No element for path [{attribute_path}]")
    if attribute:
        attr = element[0].get(attribute)
        if attr is None:
            raise  # ElementNotFound(f"{R}Element {attribute}is empty!")
        return attr
    return element[0]


root = None


def load_tracks(path):
    with gzip.open(path, "r") as f:
        data = f.read().decode("utf-8")
        if not data:
            print("%sError loading data %s!")
            return False
        root = ET.fromstring(data)
    tracks = get_element(root, "LiveSet.Tracks")
    track_list = []
    for track in tracks:
        track_list.append(AbletonTrack(track, (11, 2, 11)))

    return track_list


path = "/Users/brentthayer/Desktop/set_creator Project/set_creator.als"
lst = load_tracks(path)


print(lst[0].type)
print(lst[0].name)
print(lst[0].id)
print(lst[0].group_id)
