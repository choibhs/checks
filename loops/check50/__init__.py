from check50 import *


class Loops(Checks):

    @check()
    def exists(self):
        """loops.c exists"""
        self.require("loops.c")

    @check("exists")
    def compiles(self):
        """loops.c compiles"""
        self.spawn("clang -std=c11 -o loops loops.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test1(self):
        """"""
        self.spawn("./loops").stdin("0").stdin("3").stdout("0\n1\n2\n3\n").exit(0)

    #@check("compiles")
    #def test2(self):
    #    """"""
    #    self.spawn("./loops").stdin("0").stdout("That response is invalid\n").stdin("2").stdout("That response is valid\n").stdin("30").stdout("That response is valid\n").exit(0)

def number(num):
    return "(^|[^\d]){}[^\d]".format(num)
