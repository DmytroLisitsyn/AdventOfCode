#!/usr/bin/python

import os

def main():
    input_file = "input.txt"
    # input_file = "input_debug.txt"

    lines = _read_file(input_file)
    total = 0

    for line in lines:
        toss = line.split()
        points_for_shape_result = _points_for_shape_result(toss)
        total += points_for_shape_result

    print(total)

def _points_for_shape_shape(toss):
    # [3 - Scissors, 2 - Paper, 1 - Rock]
    op = _point_for_shape(toss[0])
    me = _point_for_shape(toss[1])

    points = 0
    diff = me - op

    if diff == 0:
        points = 3
    elif diff == 1 or diff == -2:
        points = 6
    else:
        points = 0

    points += me

    return points

def _points_for_shape_result(toss):
    op = _point_for_shape(toss[0])
    outcome = toss[1]
    points = 0

    if outcome == "X":
        me = op - 1 if op - 1 > 0 else 3
        points = 0 + me
    elif outcome == "Y":
        points = 3 + op
    else:
        me = op % 3 + 1
        points = 6 + me

    return points

def _point_for_shape(shape):
    if shape == "A" or shape == "X":
        return 1
    elif shape == "B" or shape == "Y":
        return 2
    else:
        return 3

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
