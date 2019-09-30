import check50
import check50.c

@check50.check()
def exists():
    """loops.c exists."""
    check50.exists("loops.c")

@check50.check(exists)
def compiles():
    """loops.c compiles."""
    check50.c.compile("loops.c", lcs50=True)

@check50.check(compiles)
def three_and_three(self):
    """Correct for inputs 3 and 3"""
    check50.run("./loops").stdin("3").stdout("3 x 0 = 0\n3 x 1 = 3\n3 x 2 = 6\n3 x 3 = 9\n3 x 4 = 12\n3 x 5 = 15\n3 x 6 = 18\n3 x 7 = 21\n3 x 8 = 24\n3 x 9 = 27\n3 x 10 = 30\n3 x 11 = 33\n3 x 12 = 36\n").stdin("3").stdout("0\n1\n2\n3\n").exit(0)

@check50.check(compiles)
def six_and_two(self):
    """Correct for inputs 6 and 2"""
    check50.run("./loops").stdin("2").stdout("2 x 0 = 0\n2 x 1 = 2\n2 x 2 = 4\n2 x 3 = 6\n2 x 4 = 8\n2 x 5 = 10\n2 x 6 = 12\n2 x 7 = 14\n2 x 8 = 16\n2 x 9 = 18\n2 x 10 = 20\n2 x 11 = 22\n2 x 12 = 24\n").stdin("6").stdout("0\n1\n2\n3\n4\n5\n6").exit(0)

@check50.check(compiles)
def test_reject_negative_inputs(self):
    """same as 3 and 3 inputs, but rejects negative input of -2 and -2"""
    check50.run("./loops").stdin("-2").stdin("3").stdout("3 x 0 = 0\n3 x 1 = 3\n3 x 2 = 6\n3 x 3 = 9\n3 x 4 = 12\n3 x 5 = 15\n3 x 6 = 18\n3 x 7 = 21\n3 x 8 = 24\n3 x 9 = 27\n3 x 10 = 30\n3 x 11 = 33\n3 x 12 = 36\n").stdin("-2").stdin("3").stdout("0\n1\n2\n3\n").exit(0)

@check50.check(compiles)
def test_reject_zero_inputs(self):
    """same as 3 and 3 inputs, but rejects inputs 0 and 0"""
    check50.run("./loops").stdin("0").stdin("3").stdout("3 x 0 = 0\n3 x 1 = 3\n3 x 2 = 6\n3 x 3 = 9\n3 x 4 = 12\n3 x 5 = 15\n3 x 6 = 18\n3 x 7 = 21\n3 x 8 = 24\n3 x 9 = 27\n3 x 10 = 30\n3 x 11 = 33\n3 x 12 = 36\n").stdin("0").stdin("3").stdout("0\n1\n2\n3\n").exit(0)