#!/usr/bin/python

import os
import string

def main():
    input_file = "input.txt"
    # input_file = "input_debug.txt"

    lines = _read_file(input_file)

    priority_of_repetitions = _priority_of_repetitions(lines)
    print(priority_of_repetitions)

    priority_of_badges = _priority_of_badges(lines)
    print(priority_of_badges)

def _priority_of_badges(lines):
    total = 0

    for i in range(0, len(lines) // 3):
        set_index = {}
        set1 = lines[i * 3 + 0]
        set2 = lines[i * 3 + 1]
        set3 = lines[i * 3 + 2]

        for char in set1:
            if char not in set_index:
                set_index[char] = 1

        for char in set2:
            if char in set_index:
                set_index[char] = 2

        for char in set3:
            if char in set_index and set_index[char] == 2:
                set_index[char] = 3

        for char in set_index:
            if set_index[char] == 3:
                total += _letter_priority(char)

    return total

def _priority_of_repetitions(lines):
    total = 0

    for line in lines:
        repetitions = _find_repetitions(line)

        for char in repetitions:
            priority = _letter_priority(char)
            total += priority

    return total

def _find_repetitions(line):
    half_line = len(line) // 2

    comp1_index = {}
    for char in line[:half_line]:
        if char not in comp1_index:
            comp1_index[char] = 1

    repetitions = set()
    comp2 = line[half_line:]
    for char in comp2:
        if char in comp1_index:
            repetitions.add(char)

    return repetitions

def _letter_priority(letter):
    index = string.ascii_letters.index(letter)
    if index == None:
        return 0
    else:
        return index + 1

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
