#!/usr/bin/env python3
import subprocess
import sys
import os

first = "|--"
second = "|   |-- "
third = "|   |   `--"
fourth = "|   `--"
fifth = "`--"

file_count = 0
dirs_count = 0
second_count = 0
# another_count = 0
# third_count = 0
last_count = 0


def find_files(path):
    for root, dirs, files in os.walk(path):
        levels = root.split('/')
        rlevels = len(levels) - 1
        global last_count
        for f in files:
            last_count += 1
            if last_count == 2:
                return fifth + f


def find_the(path):
    for root, dirs, files in os.walk(path):
        levels = root.split('/')
        rlevels = len(levels) - 1
        for f in files:
            if rlevels == 2:
                return fourth + f


def find_tree(path):
    print(path)
    for root, dirs, files in os.walk(path):
        levels = root.split('/')
        rlevels = len(levels) - 1
        global file_count
        global dirs_count
        global second_count
        # global another_count
        # global third_count
        if no path:
            print ("No path")
        for f in files:
            file_count += 1
            if file_count == 1:
                if rlevels == 1:
                    print(first, f)
            for d in dirs:
                dirs_count += 1
            if rlevels == 1:
                print(first, d)
            elif rlevels == 2:
                print(second, d)
        for f in files:
            second_count += 1
            if second_count == 4:
                return third + f

print(find_tree(sys.argv[1]))
print(find_the(sys.argv[1]))
print(find_last(sys.argv[1]))
print()
print("%d directories, " % dirs_count, end="")
print("%d files" % file_count)
