import hashlib
from sys import argv
import os
from pathlib import Path
import numpy as np

DESCENDING = 1
ASCENDING = 2

def main():

    if len(argv) != 2:
        print("Directory is not specified")
        return

    root_directory = argv[1]

    print("Enter file format:")
    file_format = input().strip() or "*"
    file_extension = f".{file_format}"

    print("Size sorting options:")
    print("1. Descending")
    print("2. Ascending")
    print()
    sort_option = None
    while sort_option is None:
        print("Enter a sorting option:")
        option = int(input())
        if option in [DESCENDING, ASCENDING]:
            sort_option = option
        else:
            print("\nWrong option\n")

    matching_files = dict()
    for root, dirs, files in os.walk(root_directory):
        for name in files:
            path = Path(root) / Path(name)
            if file_format == "*" or path.suffix == file_extension:
                file = path
                size = path.stat().st_size
                files_of_size = matching_files.get(size, [])
                files_of_size.append(file)
                matching_files[size] = files_of_size

    file_sizes = sorted(matching_files.keys(), reverse=(sort_option == DESCENDING))
    for file_size in file_sizes:
        print(f"{file_size} bytes")
        for file in matching_files[file_size]:
            print(file)
        print()

    print("Check for duplicates?")
    duplicates_option = None
    while duplicates_option is None:
        option = input()
        if option in ['yes', 'no']:
            duplicates_option = option
        else:
            print("\nWrong option\n")

    if duplicates_option == "no":
        exit()

    dupe_list = []
    counter = 1
    
    for sk in file_sizes:
        hash_dict = {}
        hash_set = set()

        print(f"{sk} bytes")
        for v in matching_files[sk]:
            with open(v, "rb") as f:
                file_hash = hashlib.md5()
                file_hash.update(f.read())
                hash_dict.setdefault(file_hash.hexdigest(), []).append(v)
            
            for hash_value in hash_dict.keys():
                if len(hash_dict[hash_value]) > 1 and hash_value not in hash_set:
                    print(f"Hash: {hash_value}")
                    for filepath in hash_dict[hash_value]:
                        print(f"{counter}. {filepath}")
                        
                        dupe_list.append([filepath, sk])
                        counter += 1
                    hash_set.add(hash_value)
        print()
    
    free_space = 0
    print("Delete files?")
    delete_files = input()
    while delete_files not in ["yes", "no"]:
        print("Wrong option")
        delete_files = input()
        print()
    if delete_files == "no":
        exit()

    print("Enter file numbers to delete:")
    file_numbers = [x for x in input().split()]
    while len(file_numbers) < 1 or any(not x.isdigit() for x in file_numbers):
        print("wrong format")
        file_numbers = [x for x in input().split()]
    while max(int(x) for x in file_numbers) > (len(dupe_list)):
        print("wrong format")
        file_numbers = [x for x in input().split()]

    for file_num in file_numbers:
        full_path = dupe_list[int(file_num) - 1][0]
        os.remove(full_path)
        free_space += dupe_list[int(file_num) - 1][1]

    print(f"Total freed up space: {free_space} bytes")

if __name__ == "__main__":

    main()



