from check50 import *


class Bubble(Checks):

    @check()
    def exists(self):
        """bubble.c exists"""
        self.require("bubble.c")

    @check("exists")
    def compiles(self):
        """bubble.c compiles"""
        self.spawn("clang -std=c11 -o bubble bubble.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test(self):
       self.spawn("./bubble").stdout("Generating 1000 random arrays \(beep beep boop boop\)\nAverage number of swaps: 20.27\n").exit(0)

def number(num):
    return "(^|[^\d]){}[^\d]".format(num)
