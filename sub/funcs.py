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
OP_RET = iota()
FUNCS_SIZE = iota()


def PUSH(value: int) -> tuple:
    return OP_PUSH, value


def POP(value=None):
    return OP_POP,


def ADD(value=None):
    return OP_ADD,


def SUB(value=None):
    return OP_SUB,


def PRINT(value=None):
    return OP_PRINT,


def RET(value=None):
    return OP_RET,


def interpret(commands):
    stack = []
    assert FUNCS_SIZE == 6, "Add implementation to interpret"
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
        elif com[0] == OP_RET:
            return stack.pop()
