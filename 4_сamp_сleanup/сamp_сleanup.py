#!/usr/bin/python

import os
import re 

def main():
    input_file = "input.txt"
    # input_file = "input_debug.txt"

    lines = _read_file(input_file)

    full_overlap_count = _full_overlap_count(lines)
    print(full_overlap_count)

    overlap_count = _overlap_count(lines)
    print(overlap_count)

def _overlap_count(lines):
    result = 0

    for line in lines:
        range_bounds = list(map(int, re.findall("\d+", line)))
        lb1 = min(range_bounds[0], range_bounds[1])
        ub1 = max(range_bounds[0], range_bounds[1])
        lb2 = min(range_bounds[2], range_bounds[3])
        ub2 = max(range_bounds[2], range_bounds[3])

        if (lb1 >= lb2 and lb1 <= ub2) or (ub1 >= lb2 and ub1 <= ub2):
            result += 1
        elif (lb2 >= lb1 and lb2 <= ub1) or (ub2 >= lb1 and ub2 <= ub1):
            result += 1

    return result

def _full_overlap_count(lines):
    result = 0

    for line in lines:
        range_bounds = list(map(int, re.findall("\d+", line)))
        lb1 = min(range_bounds[0], range_bounds[1])
        ub1 = max(range_bounds[0], range_bounds[1])
        lb2 = min(range_bounds[2], range_bounds[3])
        ub2 = max(range_bounds[2], range_bounds[3])

        if lb1 <= lb2 and ub2 <= ub1:
            result += 1
        elif lb2 <= lb1 and ub1 <= ub2:
            result += 1

    return result

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
