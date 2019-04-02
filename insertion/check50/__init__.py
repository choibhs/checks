from check50 import *


class Insertion(Checks):

    @check()
    def exists(self):
        """insertion.c exists"""
        self.require("insertion.c")

    @check("exists")
    def compiles(self):
        """insertion.c compiles"""
        self.spawn("clang -std=c11 -o insertion insertion.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test(self):
       self.spawn("./insertion").stdout("Generating 1000 random arrays \(beep beep boop boop\)\nAverage number of swaps: 26.92\n").exit(0)

def number(num):
    return "(^|[^\d]){}[^\d]".format(num)
