from check50 import *


class Selection(Checks):

    @check()
    def exists(self):
        """selection.c exists"""
        self.require("selection.c")

    @check("exists")
    def compiles(self):
        """selection.c compiles"""
        self.spawn("clang -std=c11 -o selection selection.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test(self):
       self.spawn("./selection").stdout("Generating 1000 random arrays \(beep beep boop boop\)\nAverage number of swaps: 6.61\n").exit(0)

def number(num):
    return "(^|[^\d]){}[^\d]".format(num)
