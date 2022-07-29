"""
This should be a list of all functions in programming language.
With "OP_" prefix.
"""
from sub.sub import *

OP_PUSH = iota()
OP_POP = iota()
OP_ADD = iota()
OP_SUB = iota()
OP_PRINT = iota()
FUNCS_SIZE = iota()


def PUSH(value: int) -> tuple:
    return OP_PUSH, value


def POP(value: int):
    return OP_POP, value


def ADD():
    return OP_ADD,


def SUB():
    return OP_SUB,


def PRINT():
    return OP_PRINT,


def interpret(commands):
    stack = []
    assert FUNCS_SIZE == 5, "Add implementation to interpret"
    for com in commands:
        if com[0] == OP_PUSH:
            stack.append(com[1])
        elif com[0] == OP_POP:
            stack.pop()
        elif com[0] == OP_ADD:
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b)
        elif com[0] == OP_SUB:
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
        elif com[0] == OP_PRINT:
            a = stack.pop()
            print(a)
