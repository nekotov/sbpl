from unittest import TestCase

from sub.funcs import *


class Test(TestCase):
    def test_ADD(self):
        self.assertEqual(interpret([PUSH(10), PUSH(5), ADD(), RET()]), 15)

    def test_SUB(self):
        self.assertEqual(interpret([PUSH(10), PUSH(5), SUB(), RET()]), 5)

    def test_POP(self):
        self.assertEqual(interpret([PUSH(10), PUSH(5), POP(), RET()]), 10)
