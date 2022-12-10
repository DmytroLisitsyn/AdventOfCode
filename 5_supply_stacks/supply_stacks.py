#!/usr/bin/python

import os
import re

def main():
    input_file = "input.txt"
    # input_file = "input_debug.txt"

    lines = _read_file(input_file)

    stacks_tops_slice_9000 = _stacks_tops_slice_9000(lines)
    print(stacks_tops_slice_9000)

    stacks_tops_slice_9001 = _stacks_tops_slice_9001(lines)
    print(stacks_tops_slice_9001)

def _stacks_tops_slice_9001(lines):
    stacks = {}

    should_map_crates = True
    for line in lines:
        if len(line) == 0:
            should_map_crates = False
        elif should_map_crates:
            crates = re.findall(".{3}\\s?", line)
            for i in range(0, len(crates)):
                crate = re.sub("(\s|\[|\])", "", crates[i])

                if len(crate) == 0:
                    continue
                elif crate.isdigit():
                    if i in stacks:
                        stacks[crate] = stacks.pop(i)
                else:
                    if i in stacks:
                        stacks[i].insert(0, crate)
                    else:
                        stacks[i] = [crate]
        else:
            moves = re.findall("\d+", line)
            amount = int(moves[0])
            fr = moves[1]
            to = moves[2]

            load = []
            for _ in range(0, amount):
                load.insert(0, stacks[fr].pop())
            
            stacks[to] += load

    tops = ""
    for key in sorted(stacks.keys()):
        tops += (stacks[key][-1])

    return tops

def _stacks_tops_slice_9000(lines):
    stacks = {}

    should_map_crates = True
    for line in lines:
        if len(line) == 0:
            should_map_crates = False
        elif should_map_crates:
            crates = re.findall(".{3}\\s?", line)
            for i in range(0, len(crates)):
                crate = re.sub("(\s|\[|\])", "", crates[i])

                if len(crate) == 0:
                    continue
                elif crate.isdigit():
                    if i in stacks:
                        stacks[crate] = stacks.pop(i)
                else:
                    if i in stacks:
                        stacks[i].insert(0, crate)
                    else:
                        stacks[i] = [crate]
        else:
            moves = re.findall("\d+", line)
            amount = int(moves[0])
            fr = moves[1]
            to = moves[2]

            for _ in range(0, amount):
                stacks[to].append(stacks[fr].pop())

    tops = ""
    for key in sorted(stacks.keys()):
        tops += (stacks[key][-1])

    return tops

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
