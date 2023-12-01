#!/usr/bin/python

import os
import string

class Area:
    def __init__(self):
        self.terrain = []
        self.start = None
        self.end = None

    def __str__(self):
        str = ""
        str += "Start: {}".format(self.start)
        str += "\nEnd: {}".format(self.end)
        str += "\nTerrain:"

        for slice in self.terrain:
            str += "\n{}".format(slice)

        return str

def main():
    # input_file = "input.txt"
    input_file = "input_debug.txt"

    script_dir = os.path.dirname(__file__)
    abs_file = os.path.join(script_dir, input_file)
    lines = open(abs_file, "r").readlines()

    shortest_path_length = _shortest_path_length(lines)
    print(shortest_path_length)

def _shortest_path_length(lines):
    area = _map_area(lines)
    _new_paths([area.start], area)

    return 0

def _new_paths(path, area):
    cp = path[len(path) - 1]
    if cp == area.end:
        print(path)
        return [path]

    nps = [(cp[0] - 1, cp[1]), (cp[0], cp[1] - 1), (cp[0] + 1, cp[1]), (cp[0], cp[1] + 1)]
    paths = []

    for np in nps:
        if _is_next_point_valid(np, cp, path, area):
            path.append(np)
            paths += _new_paths(path, area)

    return paths

def _is_next_point_valid(np, cp, path, area):
    if np == area.end:
        return True

    if not (0 <= np[1] < len(area.terrain) and 0 <= np[0] < len(area.terrain[np[1]])):
        return False

    if not (abs(area.terrain[np[1]][np[0]] - area.terrain[cp[1]][cp[0]]) < 2):
        return False

    return not (np in path)

def _map_area(lines):
    area = Area()

    for i in range(0, len(lines)):
        area.terrain.append([])

        for j in range(0, len(lines[i])):
            char = lines[i][j]
            if char == "\n":
                continue
            elif char == "S":
                area.start = (j, i)
                area.terrain[i].append(0)
            elif char == "E":
                area.end = (j, i)
                area.terrain[i].append(0)
            else:
                area.terrain[i].append(_letter_priority(char))

    return area

def _letter_priority(letter):
    index = string.ascii_letters.index(letter)
    return index + 1 if index != None else 0

if __name__ == "__main__":
    main()
