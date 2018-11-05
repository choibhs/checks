import re

from check50 import *


class Greedy2(Checks):

    @check()
    def exists(self):
        """greedy2 exists"""
        self.require("greedy2.c")

    @check("exists")
    def compiles(self):
        """greedy2 compiles"""
        self.spawn("clang -std=c11 -ggdb3 -o greedy2 greedy2.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test041(self):
        """input of 0.41 yields output of 4"""
        self.spawn("./greedy2").stdin("0.41").stdout(coins(4), "4\n").exit(0)

    @check("compiles")
    def test001(self):
        """input of 0.01 yields output of 1"""
        self.spawn("./greedy2").stdin("0.01").stdout(coins(1), "1\n").exit(0)

    @check("compiles")
    def test015(self):
        """input of 0.15 yields output of 2"""
        self.spawn("./greedy2").stdin("0.15").stdout(coins(2), "2\n").exit(0)

    @check("compiles")
    def test160(self):
        """input of 1.6 yields output of 3"""
        self.spawn("./greedy2").stdin("1.6").stdout(coins(3), "3\n").exit(0)

    @check("compiles")
    def test230(self):
        """input of 23 yields output of 4"""
        self.spawn("./greedy2").stdin("23").stdout(coins(4), "4\n").exit(0)

    @check("compiles")
    def test04(self):
        """input of 0.04 yields output of 2"""
        self.spawn("./greedy2").stdin("0.04").stdout(coins(2), "2\n").exit(0)

    @check("compiles")
    def test420(self):
        """input of 4.2 yields output of 6"""
        expected = "6\n"
        actual = self.spawn("./greedy2").stdin("4.2").stdout()
        if not re.search(coins(6), actual):
            err = Error(Mismatch(expected, actual))
            if re.search(coins(18), actual):
                err.helpers = "Did you forget to includes dollars, 2 cent coins, etc.?"
            raise err

    @check("compiles")
    def test_reject_negative(self):
        """rejects a negative input like -.1"""
        self.spawn("./greedy2").stdin("-1").reject()

    @check("compiles")
    def test_reject_foo(self):
        """rejects a non-numeric input of "foo" """
        self.spawn("./greedy2").stdin("foo").reject()

    @check("compiles")
    def test_reject_empty(self):
        """rejects a non-numeric input of "" """
        self.spawn("./greedy2").stdin("").reject()


def coins(num):
    return r"(^|[^\d]){}(?!\d)".format(num)
