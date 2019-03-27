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
        self.spawn("./basics").stdin("Mr. T").stdout("Hello, Mr. T!\n").stdin("20").stdout("You are 20 years old\nIn twenty years you will be 40\n")\
                .stdin("1").stdin("2").stdin("3").stdin("4").stdin("5")\
                .stdout("Your zip code is: 12345\nYour zip code reversed is: 54321")\
                .exit(0)

def number(num):
    return "(^|[^\d]){}[^\d]".format(num)
