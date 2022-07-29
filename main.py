#!/bin/env python3
from sys import argv

from sub import funcs
from sub.funcs import *

show_info()

if len(argv) < 1:
    show_usage()

exec_arr = []
all_funcs = []

for all_funds_itr in dir(funcs):
    if all_funds_itr.isupper() and "_" not in all_funds_itr:
        all_funcs.append(all_funds_itr)

with open(argv[1]) as f:
    for line in f.readlines():
        if "\n" in line[0]:
            line[0] = line[0][:-1]
        elif "\n" in line:
            line = line[:-1]
        line = line.split(" ")
        if line[0] in all_funcs:
            # for future [line[-1][0][:-2] if "\n" in line[-1][0] else line[-1][0]]
            exec_arr.append(globals()[line[0]]([int(line[1]) if len(line) > 1 else None][0]))
interpret(exec_arr)
