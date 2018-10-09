from check50 import *


class TestScores(Checks):

    @check()
    def exists(self):
        """test_scores.c exists"""
        self.require("test_scores.c")

    @check("exists")
    def compiles(self):
        """test_scores.c compiles"""
        self.spawn("clang -std=c11 -o test_scores test_scores.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test0(self):
        """Correct for input 94 debug test"""
        self.spawn("./test_scores").stdin("94")\
            .stdout("Number of A's: 1 (100.0 percent)").exit(0)

    @check("compiles")
    def test1(self):
        """Correct for input 94"""
        self.spawn("./test_scores").stdin("94").stdout("Number of A's: 1 (100.0%)\nNumber of B's: 0 (0.0%)\nNumber of C's: 0 (0.0%)\nNumber below C: 0 (0.0%)\n\n").exit(0)

    @check("compiles")
    def test2(self):
        """Correct for input 94 and 4"""
        self.spawn("./test_scores").stdin("94").stdout("Number of A's: 1 (100.0%)\nNumber of B's: 0 (0.0%)\nNumber of C's: 0 (0.0%)\nNumber below C: 0 (0.0%)\n\n").stdin(4).stdout("Number of A's: 1 (50.0%)\nNumber of B's: 0 (0.0%)\nNumber of C's: 0 (0.0%)\nNumber below C: 1 (50.0%)\n\n").exit(0)

    @check("compiles")
    def test3(self):
        """Correct for inputs -1 101 94 0"""
        self.spawn("./test_scores").stdin("-1").stdin("101").stdin("94").stdout("Number of A's: 1 (100.0%)\nNumber of B's: 0 (0.0%)\nNumber of C's: 0 (0.0%)\nNumber below C: 0 (0.0%)\n\n").stdin(0).stdout("Number of A's: 1 (50.0%)\nNumber of B's: 0 (0.0%)\nNumber of C's: 0 (0.0%)\nNumber below C: 1 (50.0%)\n\n").exit(0)

    @check("compiles")
    def test_reject_foo(self):
        """rejects a non-numeric input of "foo" """
        self.spawn("./test_scores").stdin("foo").reject()

    @check("compiles")
    def test_reject_empty(self):
        """rejects a non-numeric input of "" """
        self.spawn("./test_scores").stdin("").reject()

def number(num):
    return "(^|[^\d]){}[^\d]".format(num)
