#!/usr/bin/python

import os

def main():
    input_file = "input.txt"
    # input_file = "input_debug.txt"

    lines = _read_file(input_file)

    visible_trees_count = _count_visible_trees(lines)
    print(visible_trees_count)

    highest_scenic_score = _count_highest_scenic_score(lines)
    print(highest_scenic_score)


def _count_highest_scenic_score(lines):
    result = 0

    forest = []
    for i in range(0, len(lines)):
        forest.append(list(map(int, lines[i])))

    for i in range(0, len(forest)):
        for j in range(0, len(forest[i])):
            current_tree = forest[i][j]

            x_prev_score = 0
            x_prev_slice = list(reversed(forest[i][0:j]))
            for other_tree in x_prev_slice:
                x_prev_score += 1
                if other_tree >= current_tree:
                    break

            x_next_score = 0
            x_next_slice = list(forest[i][j+1:len(forest[i])])
            for other_tree in x_next_slice:
                x_next_score += 1
                if other_tree >= current_tree:
                    break

            y_prev_slice = []
            for x in range(0, i):
                y_prev_slice.append(forest[x][j])

            y_prev_score = 0
            y_prev_slice = list(reversed(y_prev_slice))
            for other_tree in y_prev_slice:
                y_prev_score += 1
                if other_tree >= current_tree:
                    break

            y_next_slice = []
            for x in range(i + 1, len(forest)):
                y_next_slice.append(forest[x][j])

            y_next_score = 0
            for other_tree in y_next_slice:
                y_next_score += 1
                if other_tree >= current_tree:
                    break

            score = x_prev_score * x_next_score * y_prev_score * y_next_score
            result = max(score, result)

    return result

def _count_visible_trees(lines):
    result = 0

    forest = []
    for i in range(0, len(lines)):
        forest.append(list(map(int, lines[i])))
            
    for i in range(0, len(forest)):
        for j in range(0, len(forest[i])):
            x_prev_slice = forest[i][0:j]
            if len(x_prev_slice) == 0 or max(x_prev_slice) < forest[i][j]:
                result += 1
                continue

            x_next_slice = list(forest[i][j+1:len(forest[i])])
            if len(x_next_slice) == 0 or max(x_next_slice) < forest[i][j]:
                result += 1
                continue

            y_prev_slice = []
            for x in range(0, i):
                y_prev_slice.append(forest[x][j])

            if len(y_prev_slice) == 0 or max(y_prev_slice) < forest[i][j]:
                result += 1
                continue

            y_next_slice = []
            for x in range(i + 1, len(forest)):
                y_next_slice.append(forest[x][j])

            if len(y_next_slice) == 0 or max(y_next_slice) < forest[i][j]:
                result += 1
                continue

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
