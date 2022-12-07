from pathlib import Path
from typing import List
from operator import add
from functools import reduce
from random import randint


def read_input() -> map:
    with open(Path(__file__).parent / "input", "r") as i:
        return [line.strip() for line in i.readlines()]


def get_dict_child(jisho: dict, key: str):
    return jisho.get(key, {})


def handle_command(
    command: List[str], output_rows: List[str], directory_map: dict, folder_depth: list
):
    if command[0] == "ls":
        process_files(output_rows[1:], directory_map)
    elif command[0] == "cd":
        if command[1] == "..":
            folder_depth.pop()
        else:
            if not directory_map.get(command[1]):
                directory_map[command[1]] = dict()
            folder_depth.append(command[1])


def process_files(output_rows, directory_map):
    try:
        contents: List[str] = output_rows[
            : next(i for i in range(len(output_rows)) if output_rows[i].startswith("$"))
        ]
    except StopIteration:
        contents = output_rows
    for content in contents:
        size_type, name = content.split()
        if size_type == "dir":
            directory_map[name] = dict()
        else:
            directory_map[name] = int(size_type)


def dir_mapper(output_rows: List[str]) -> dict:
    directory_map = dict()
    folder_depth = list()
    for i, row in enumerate(output_rows):
        if not row.startswith("$"):
            continue
        command = row[1:].strip().split()
        handle_command(
            command,
            output_rows[i:],
            reduce(get_dict_child, folder_depth, directory_map),
            folder_depth,
        )
    return directory_map


def sum_folder_size(directory_map: dict, size: int = 0) -> int:
    for folder, sub_folders in directory_map.items():
        if isinstance(sub_folders, dict):
            size = sum_folder_size(sub_folders, size)
        else:
            size += sub_folders
    return size


def get_folder_sizes(directory_map: dict, sizes: dict = {}, parent=".") -> dict:
    for folder, sub_folders in directory_map.items():
        if isinstance(sub_folders, dict):
            if not sizes.get(folder):
                sizes[parent + "/" + folder] = sum_folder_size(sub_folders)
            get_folder_sizes(sub_folders, sizes, parent + "/" + folder)
    return sizes


def part1(directory_map: dict) -> int:
    sizes = get_folder_sizes(directory_map)
    limit100000 = [size for folder, size in sizes.items() if size <= 100000]
    print(sum(limit100000))


def part2(directory_map: dict) -> int:
    sizes = get_folder_sizes(directory_map)
    current_size = sizes[".//"]
    needed_space = 30000000
    max_space = 70000000
    unused_space = max_space - current_size
    candidates = [
        size
        for folder, size in sizes.items()
        if unused_space + size >= needed_space and unused_space + size <= max_space
    ]
    print(min(sorted(candidates)))


if __name__ == "__main__":
    data = read_input()
    directory_tree = dir_mapper(data)
    part1(directory_tree)
    part2(directory_tree)
