from check50 import *


class multiples2(Checks):

    @check()
    def exists(self):
        """multiples2.c exists"""
        self.require("multiples2.c")

    @check("exists")
    def compiles(self):
        """multiples2.c compiles"""
        self.spawn("clang -std=c11 -o multiples2 multiples2.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test1(self):
        """Correct for inputs 24 and 4"""
        self.spawn("./multiples2").stdin("24").stdin("4").stdout("All multiples of 4 <= 24 are:\n24\n20\n16\n12\n8\n4\n0\n").exit(0)

    @check("compiles")
    def test2(self):
        """Correct error message for inputs 25 and 4"""
        self.spawn("./multiples2").stdin("25").stdin("4").stdout("The divisor doesn't divide the number evenly. Exiting.").exit(0)

    @check("compiles")
    def test_reject_foo(self):
        """rejects a non-numeric input of "foo" """
        self.spawn("./multiples2").stdin("foo").reject()

    @check("compiles")
    def test_reject_empty(self):
        """rejects a non-numeric input of "" """
        self.spawn("./multiples2").stdin("").reject()

def number(num):
    return "(^|[^\d]){}[^\d]".format(num)
