import re

from check50 import *


class Binary(Checks):

    @check()
    def exists(self):
        """binary exists"""
        self.require("binary.c")

    @check("exists")
    def compiles(self):
        """binary compiles"""
        self.spawn("clang -std=c11 -ggdb3 -o binary binary.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test201a(self):
        """Invalid menu input, then input of 11001001 yields output of 201"""
        self.spawn("./binary").stdin("-1").stdin("1").stdin("1").stdin("1").stdin("0").stdin("0").stdin("1").stdin("0").stdin("0").stdin("1").stdout("201\n").exit(0)

    @check("compiles")
    def test201b(self):
        """Invalid menu input, then input of 201 yields output 11001001"""
        self.spawn("./binary").stdin("0").stdin("2").stdin("201").stdout("11001001\n").exit(0)

    @check("compiles")
    def test23a(self):
        """Invalid binary number input, then input of 00010111 yields output of 23"""
        self.spawn("./binary").stdin("1").stdin("12").stdin("0").stdin("0").stdin("0").stdin("1").stdin("0").stdin("1").stdin("1").stdin("1").stdout("23\n").exit(0)

    @check("compiles")
    def test23b(self):
        """Invalid decimal number input, then input of 23 yields output 00010111"""
        self.spawn("./binary").stdin("2").stdin("-1").stdin("322").stdin("23").stdout("00010111\n").exit(0)

    @check("compiles")
    def test_reject_negative(self):
        """rejects a negative input like -.1"""
        self.spawn("./binary").stdin("-1").reject()

    @check("compiles")
    def test_reject_foo(self):
        """rejects a non-numeric input of "foo" """
        self.spawn("./binary").stdin("foo").reject()

    @check("compiles")
    def test_reject_empty(self):
        """rejects a non-numeric input of "" """
        self.spawn("./binary").stdin("").reject()
