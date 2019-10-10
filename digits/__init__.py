import check50
import check50.c

@check50.check()
def exists():
    """digits.c exists."""
    check50.exists("digits.c")

@check50.check(exists)
def compiles():
    """digits.c compiles."""
    check50.c.compile("digits.c", lcs50=True)

@check50.check(compiles)
def invalid_negative_num_then_print_digits(self):
    """Check input: -123456, 123456"""
    check50.run("./digits").stdin("-123456").stdout("Invalid\n").stdin("123456")\
        .stdout("The digit in the 1's place is: 6\nThe digit in the 10's place is: 5\nThe digit in the 100's place is: 4\nThe digit in the 1000's place is: 3\nThe digit in the 10000's place is: 2\nThe digit in the 100000's place is: 1\n")\
        .exit(0)

@check50.check(compiles)
def invalid_big_num_then_print_digits(self):
    """Check input: 1234567, 654321"""
    check50.run("./digits").stdin("1234567").stdout("Invalid\n").stdin("654321")\
        .stdout("The digit in the 1's place is: 1\nThe digit in the 10's place is: 2\nThe digit in the 100's place is: 3\nThe digit in the 1000's place is: 4\nThe digit in the 10000's place is: 5\nThe digit in the 100000's place is: 6\n")\
        .exit(0)

