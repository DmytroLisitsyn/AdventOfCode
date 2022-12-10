#!/usr/bin/python

import os

class CPU:
    def __init__(self, cycle, x_reg, on_tock):
        self.cycle = cycle
        self.x_reg = x_reg
        self.on_tock = on_tock

        self.signal_strength = 0
        self.render = ""

    def __str__(self):
        return f"{self.cycle}, {self.x_reg}"

    def noop(self):
        self._tick()
        self._tock()

    def addx(self, value):
        self._tick()
        self._tock()

        self._tick()
        self._tock()
        self.x_reg += value

    def _tick(self):
        self.cycle += 1

    def _tock(self):
        self.on_tock(self)

def main():
    input_file = "input.txt"
    # input_file = "input_debug.txt"

    lines = _read_file(input_file)
    
    signal_strength_sum = _count_signal_strength_sum(lines)
    print(signal_strength_sum)

    image = _render_crt(lines)
    print(image)

def _render_crt(lines):
    def _on_tock(cpu):
        pixel_index = (cpu.cycle - 1) % 40
        sprite_indices = set([cpu.x_reg - 1, cpu.x_reg, cpu.x_reg + 1])

        symbol = ""
        if pixel_index in sprite_indices:
            symbol = "#"
        else:
            symbol = "."

        cpu.render += symbol
        if cpu.cycle % 40 == 0:
            cpu.render += "\n"

    cpu = CPU(0, 1, _on_tock)

    for i in range(0, len(lines)):
        line = lines[i]
        ins = line.split(" ")
        if ins[0] == "noop":
            cpu.noop()
        elif ins[0] == "addx":
            cpu.addx(int(ins[1]))

    return cpu.render

def _count_signal_strength_sum(lines):
    def _on_tock(cpu):
        if cpu.cycle <= 220 and cpu.cycle % 40 == 20:
            cpu.signal_strength += cpu.cycle * cpu.x_reg

    cpu = CPU(0, 1, _on_tock)

    for i in range(0, len(lines)):
        line = lines[i]
        ins = line.split(" ")
        if ins[0] == "noop":
            cpu.noop()
        elif ins[0] == "addx":
            cpu.addx(int(ins[1]))

    return cpu.signal_strength

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
