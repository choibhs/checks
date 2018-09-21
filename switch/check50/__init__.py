from check50 import *


class Switch(Checks):

    @check()
    def exists(self):
        """switch.c exists"""
        self.require("switch.c")

    @check("exists")
    def compiles(self):
        """switch.c compiles"""
        self.spawn("clang -std=c11 -o switch switch.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test1(self):
        """"""
        self.spawn("./switch").stdin("y").stdout("yes\n").exit(0)

    @check("compiles")
    def test2(self):
        """"""
        self.spawn("./switch").stdin("Y").stdout("yes\n").exit(0)

    @check("compiles")
    def test3(self):
        """"""
        self.spawn("./switch").stdin("n").stdout("no\n").exit(0)

    @check("compiles")
    def test4(self):
        """"""
        self.spawn("./switch").stdin("N").stdout("no\n").exit(0)

def number(num):
    return "(^|[^\d]){}[^\d]".format(num)
