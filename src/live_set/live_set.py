import sys

sys.path.append("..")

from utils.read_json import read_json


structure = read_json("live_set.json")

print(structure)
