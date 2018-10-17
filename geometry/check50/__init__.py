from check50 import *


class Geometry(Checks):

    @check()
    def exists(self):
        """geometry.c exists"""
        self.require("geometry.c")

    @check("exists")
    def compiles(self):
        """geometry.c compiles"""
        self.spawn("clang -std=c11 -o geometry geometry.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test1(self):
        """Compiles and then run area of rectangle"""
        self.spawn("./geometry").stdin("-1").stdin("0").stdin("1").stdin("1").stdout("10").stdout("10").exit(0)

    #@check("compiles")
    #def test2(self):
    #    """"""
    #    self.spawn("./geometry").stdin("0").stdout("That response is invalid\n").stdin("2").stdout("That response is valid\n").stdin("30").stdout("That response is valid\n").exit(0)

def number(num):
    return "(^|[^\d]){}[^\d]".format(num)
