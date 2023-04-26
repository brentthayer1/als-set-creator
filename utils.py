import os
import gzip
from typing import Dict, Literal, Optional, Tuple, Union, overload
from xml.etree import ElementTree as ET


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
    element = root.findall(f"./{'/'.join(attribute_path.split('.'))}")
    if not element:
        if silent_error:
            return None
        raise  # ElementNotFound(f"{R}No element for path [{attribute_path}]")
    if attribute:
        attr = element[0].get(attribute)
        if attr is None:
            raise  # ElementNotFound(f"{R}Element {attribute}is empty!")
        return attr
    return element[0]


def set_element(
    root: ET.Element,
    attribute_path: str,
    attribute: str,
    value: str,
):
    element = root.findall(f"./{'/'.join(attribute_path.split('.'))}")[0]
    element.set(attribute, value)

    return root

    # element.set(attribute, value)

    # new_element = ET.Element(attribute_path, element.attrib)

    # element_index = list(root).index(element)
    # root.remove(element)
    # root.insert(element_index, new_element)

    #     if attr is None:
    #         raise  # ElementNotFound(f"{R}Element {attribute}is empty!")
    #     return attr
    # return element[0]


def als_to_xml(als_file_path):
    with open(als_file_path, "rb") as als_file:
        als_data = als_file.read()
        xml_data = gzip.decompress(als_data).decode()
        return xml_data


def xml_to_als(xml_data, xml_file_path):
    new_als_path = os.path.splitext(xml_file_path)[0] + "TESTER.als"
    with gzip.open(new_als_path, "wb") as new_als_file:
        new_als_file.write(xml_data)


if __name__ == "__main__":
    pass
