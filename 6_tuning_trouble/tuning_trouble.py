#!/usr/bin/python

import os
import re

def main():
    input_file = "input.txt"
    # input_file = "input_debug.txt"

    lines = _read_file(input_file)

    start_of_packet_marker = _start_of_packet_marker(lines[0])
    print(start_of_packet_marker)

    start_of_message_marker = _start_of_message_marker(lines[0])
    print(start_of_message_marker)

def _start_of_message_marker(line):
    marker = len(line) - 1

    for i in range(14, len(line)):
        slice = set(line[i-14:i])

        if len(slice) == len(line[i-14:i]):
            marker = i
            break

    return marker

def _start_of_packet_marker(line):
    marker = len(line) - 1

    for i in range(4, len(line)):
        slice = set(line[i-4:i])

        if len(slice) == len(line[i-4:i]):
            marker = i
            break

    return marker

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
