#!/usr/bin/python

import os
import re
from math import floor

class Monkey:
    def __init__(self, id):
        self.id = id
        self.items = []

        self.op_arg = None
        self.op = None

        self.test = 1
        self.testPassed = 0
        self.testFailed = 0

    def __str__(self):
        return f"{self.id}"

def main():
    input_file = "input.txt"
    # input_file = "input_debug.txt"

    script_dir = os.path.dirname(__file__)
    abs_file = os.path.join(script_dir, input_file)
    lines = open(abs_file, "r").readlines()

    monkey_business_level = _count_monkey_business_level(lines)
    print(monkey_business_level)

    monkey_business_level_2 = _count_monkey_business_level_again(lines)
    print(monkey_business_level_2)

def _count_monkey_business_level_again(lines):
    monkeys = _map_monkeys(lines)

    inspections = {}

    chill_pill = 1
    for monkey in monkeys:
        chill_pill *= monkey.test 

    for i in range(0, 10000):
        for monkey in monkeys:
            while(len(monkey.items) > 0):
                item = monkey.items.pop(0)
                op_arg = monkey.op_arg if monkey.op_arg != None else item
                worry_level = monkey.op(item, op_arg)
                new_item = worry_level % chill_pill

                if monkey.id in inspections:
                    inspections[monkey.id] += 1
                else:
                    inspections[monkey.id] = 1

                if new_item % monkey.test == 0:
                    monkeys[monkey.testPassed].items.append(new_item)
                else:
                    monkeys[monkey.testFailed].items.append(new_item)

    inspections_counts = list(reversed(sorted(v for _, v in inspections.items())))
    return inspections_counts[0] * inspections_counts[1]

def _count_monkey_business_level(lines):
    monkeys = _map_monkeys(lines)

    inspections = {}

    for _ in range(0, 20):
        for monkey in monkeys:
            while(len(monkey.items) > 0):
                item = monkey.items.pop(0)
                op_arg = monkey.op_arg if monkey.op_arg != None else item
                worry_level = monkey.op(item, op_arg)
                new_item = int(floor(worry_level / 3))

                if monkey.id in inspections:
                    inspections[monkey.id] += 1
                else:
                    inspections[monkey.id] = 1

                if new_item % monkey.test == 0:
                    monkeys[monkey.testPassed].items.append(new_item)
                else:
                    monkeys[monkey.testFailed].items.append(new_item)

    inspections_counts = list(reversed(sorted(v for _, v in inspections.items())))
    return inspections_counts[0] * inspections_counts[1]

def _map_monkeys(lines):
    monkeys = []

    for line in lines:
        query = "Monkey "
        if re.search(query, line) != None:
            id = int(re.findall("\d+", line)[0])
            monkeys.append(Monkey(id))

        query = "Starting items: "
        if re.search(query, line) != None:
            items = list(map(int, re.findall("\d+", line)))
            monkeys[len(monkeys) - 1].items = items

        query = "Operation: "
        if re.search(query, line) != None:
            op_str = re.findall("\w+ [\+\*] \w+", line)[0].split()

            monkeys[len(monkeys) - 1].op_arg = int(int(op_str[2])) if op_str[2].isdigit() else None
                            
            if op_str[1] == "+":
                monkeys[len(monkeys) - 1].op = lambda x, y: x + y
            elif op_str[1] == "*":
                monkeys[len(monkeys) - 1].op = lambda x, y: x * y

        query = "Test: "
        if re.search(query, line) != None:
            test = int(re.findall("\d+", line)[0])
            monkeys[len(monkeys) - 1].test = test

        query = "If true: "
        if re.search(query, line) != None:
            testPassed = int(re.findall("\d+", line)[0])
            monkeys[len(monkeys) - 1].testPassed = testPassed

        query = "If false: "
        if re.search(query, line) != None:
            testFailed = int(re.findall("\d+", line)[0])
            monkeys[len(monkeys) - 1].testFailed = testFailed

    return monkeys

if __name__ == "__main__":
    main()
