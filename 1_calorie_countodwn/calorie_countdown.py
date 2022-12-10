#!/usr/bin/python

import os

def main():
    input_file = "input.txt"

    lines = _read_file(input_file)
    
    top_elf_balance = _top_elf_balance(lines)
    print(top_elf_balance)

    top_three_elves_balance = _top_three_elves_balance(lines)
    print(top_three_elves_balance)

def _top_elf_balance(lines):
    max_balance = 0
    balance = 0

    for line in lines:
        line = line.replace('\n','')

        if len(line) > 0:
            balance += int(line)
        else:
            if balance > max_balance:
                max_balance = balance

            balance = 0

    if balance > max_balance:
        max_balance = balance

    return max_balance

def _top_three_elves_balance(lines):
    top_balance = []
    balance = 0

    for line in lines:
        line = line.replace('\n','')

        if len(line) > 0:
            balance += int(line)
        else:
            if len(top_balance) < 3:
                top_balance.append(balance)
            else:
                top_balance = sorted(top_balance)

                if balance > top_balance[0]:
                    top_balance[0] = balance

            balance = 0

    top_balance = sorted(top_balance)

    if balance > top_balance[0]:
        top_balance[0] = balance

    top_three_elves_balance = 0
    for balance in top_balance:
        top_three_elves_balance += balance

    return top_three_elves_balance

def _read_file(file):
    lines = []

    if file == None:
        return lines

    script_dir = os.path.dirname(__file__)
    abs_file = os.path.join(script_dir, file)  

    content = open(abs_file, "r")
    for line in content:
        lines.append(line)

    return lines

if __name__ == "__main__":
    main()
