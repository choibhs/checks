from check50 import *


class ValidateThree(Checks):

    @check()
    def exists(self):
        """validate_three.c exists"""
        self.require("validate_three.c")

    @check("exists")
    def compiles(self):
        """validate_three.c compiles"""
        self.spawn("clang -std=c11 -o validate_three validate_three.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test1(self):
        """"""
        self.spawn("./validate_three").stdin("24").stdout("That response is valid\n")
            .stdin("24").stdout("That response is invalid\n").
            .stdin("24").stdout("That response is invalid\n").
            exit(0)

    @check("compiles")
    def test2(self):
        """"""
        self.spawn("./validate_three").stdin("0").stdout("That response is invalid\n")
            .stdin("yes").stdout("That response is valid\n").
            .stdin("30").stdout("That response is valid\n").
            exit(0)

def number(num):
    return "(^|[^\d]){}[^\d]".format(num)
