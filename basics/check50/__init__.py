from check50 import *


class Basics(Checks):

    @check()
    def exists(self):
        """basics.c exists"""
        self.require("basics.c")

    @check("exists")
    def compiles(self):
        """basics.c compiles"""
        self.spawn("clang -std=c11 -o basics basics.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test1(self):
        """"""
        self.spawn("./basics").stdin("22").stdin("24").stdout("Total = 46\n").exit(0)

def number(num):
    return "(^|[^\d]){}[^\d]".format(num)
