#!/usr/bin/python

import os
import re

class Folder:
    def __init__(self, name, content):
        self.name = name
        self.content = content

    def __str__(self):
        return f"{self.name}({self.content})"

    def __lt__(self, other):
        return self.size() < other.size()

    def size(self):
        size = 0

        for item in self.content:
            if isinstance(item, File):
                size += item.size
            elif isinstance(item, Folder):
                size += item.size()

        return size

    def folder_at_path(self, path):
        searched_folder = self

        for item_name in path:
            local = None

            for item in searched_folder.content:
                if item.name == item_name:
                    local = item

            searched_folder = local        

        return searched_folder

    def flat_folder_list(self):
        folders = []

        for item in self.content:
            if isinstance(item, Folder):
                folders.append(item)
                folders += item.flat_folder_list()

        return folders

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return f"{self.name}({self.size})"

def main():
    input_file = "input.txt"
    # input_file = "input_debug.txt"

    lines = _read_file(input_file)

    folder = _make_file_table(lines)

    critical_dirs_size = _find_critical_dirs_size(folder)
    print(critical_dirs_size)

    size_to_delete = _size_to_delete(folder)
    print(size_to_delete)

def _size_to_delete(folder):
    flat_list = sorted(folder.flat_folder_list())

    total = 70000000
    required = 30000000
    current = folder.size()
    min_to_purge = current - (total - required)

    for item in flat_list:
        if item.size() >= min_to_purge:
            return item.size()

def _find_critical_dirs_size(folder):
    size = 0
    
    for item in folder.flat_folder_list():
        if item.size() <= 100000:
            size += item.size()

    return size

def _make_file_table(lines):
    root = Folder("", [])
    cursor = []
    match = None

    for line in lines:
        match = re.search("\$ cd .*", line)
        if match != None:
            folder = re.sub("\$ cd ", "", match.string)
            if folder == "/":
                cursor = []
            elif folder == "..":
                cursor.pop()
            else:
                cursor.append(folder)

        match = re.search("dir .*", line)
        if match != None:
            folder_name = re.sub("dir ", "", match.string)
            root.folder_at_path(cursor).content.append(Folder(folder_name, []))

        match = re.search("\d+ .*", line)
        if match != None:
            file_size = int(re.search("\d+", match.string).group())
            format = "%d " %(file_size)
            file_name = re.sub(format, "", match.string)
            root.folder_at_path(cursor).content.append(File(file_name, file_size))

    return root

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
