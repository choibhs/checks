from check50 import *


class Binarysearch(Checks):

    @check()
    def exists(self):
        """binarysearch.c exists"""
        self.require("binarysearch.c")

    @check("exists")
    def compiles(self):
        """binarysearch.c compiles"""
        self.spawn("clang -std=c11 -o binarysearch binarysearch.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test(self):
       self.spawn("./binarysearch").stdout("Generating 1000 random arrays \(beep beep boop boop\)\nAverage number of checks: 4.45\n").exit(0)

def number(num):
    return "(^|[^\d]){}[^\d]".format(num)
