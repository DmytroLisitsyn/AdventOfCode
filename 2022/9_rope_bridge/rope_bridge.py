#!/usr/bin/python

import os
from math import sqrt
from math import ceil
from math import floor

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def distance(self, other):
        return sqrt(pow(self.x - other.x, 2) + pow(self.y - other.y, 2))

def main():
    input_file = "input.txt"
    # input_file = "input_debug.txt"

    lines = _read_file(input_file)

    tail_visits = _count_tail_visits(lines)
    print(tail_visits)

    extended_tail_visits = _count_extended_tail_visits(lines)
    print(extended_tail_visits)

def _count_extended_tail_visits(lines):
    snek = []
    for _ in range(0, 10):
        snek.append(Point(0, 0))

    map_of_tail = set([(snek[len(snek) - 1].x, snek[len(snek) - 1].y)])

    for line in lines:
        direction, steps_str = line.split(" ")
        offset = _make_offset(direction, int(steps_str))

        trail_length = abs(offset.x + offset.y)
        step = Point(_make_direction(offset.x), _make_direction(offset.y))

        for _ in range(0, trail_length):
            snek[0].x, snek[0].y = (snek[0].x + step.x, snek[0].y + step.y)

            for i in range(1, len(snek)):
                if not (snek[i - 1].distance(snek[i]) < 2):
                    x_vector = snek[i - 1].x - snek[i].x
                    x_vector -= _make_direction(x_vector)
                    y_vector = snek[i - 1].y - snek[i].y
                    y_vector -= _make_direction(y_vector)

                    snek[i].x = snek[i - 1].x - x_vector
                    snek[i].y = snek[i - 1].y - y_vector

            map_of_tail.add((snek[len(snek) - 1].x, snek[len(snek) - 1].y))
        
    result = len(map_of_tail)
    return result

def _count_tail_visits(lines):
    head = Point(0, 0)
    tail = Point(0, 0)

    map_of_tail = set([(tail.x, tail.y)])

    for line in lines:
        direction, steps_str = line.split(" ")
        offset = _make_offset(direction, int(steps_str))

        trail_length = abs(offset.x + offset.y)
        step = Point(int(offset.x / abs(offset.x)) if offset.x != 0 else 0, int(offset.y / abs(offset.y)) if offset.y != 0 else 0)

        for _ in range(0, trail_length):
            old_head = Point(head.x, head.y)
            head.x, head.y = (head.x + step.x, head.y + step.y)

            if not (head.distance(tail) < 2):
                tail = old_head
                map_of_tail.add((tail.x, tail.y))

    result = len(map_of_tail)
    return result

def _round_avg_away(x, y):
    value = (x + y) / 2
    if value >= 0:
        return int(ceil(value))
    else:
        return int(floor(value))

def _make_direction(x):
    return int(x / abs(x) if x != 0 else 0)

def _make_offset(direction, steps):
        if direction == "R":
            return Point(steps, 0)
        elif direction == "L":
            return Point(-steps, 0)
        elif direction == "U":
            return Point(0, -steps)
        else:
            return Point(0, steps)

def _draw_snek(snek, min_point, max_point):
    map_of_tail = set([])
    for point in snek:
        map_of_tail.add((point.x, point.y))

    _draw_map_of_tail(map_of_tail, min_point, max_point)

def _draw_map_of_tail(map_of_tail, min_point, max_point):
    string = ""
    for i in range(min_point.y, max_point.y + 1):
        for j in range(min_point.x, max_point.x + 1):
            if (j, i) in map_of_tail:
                string += "#"
            else:
                string += "."

        string += "\n"

    print(string, min_point, max_point)
    
def _read_file(file):
    lines = []

    if file == None:
        return lines

    script_dir = os.path.dirname(__file__)
    abs_file = os.path.join(script_dir, file)  

    content = open(abs_file, "r")
    for line in content:
        lines.append(line.replace('\n',''))

    return lines

if __name__ == "__main__":
    main()
