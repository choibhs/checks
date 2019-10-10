import check50
import check50.c

@check50.check()
def exists():
    """palindrome.c exists."""
    check50.exists("palindrome.c")

@check50.check(exists)
def compiles():
    """palindrome.c compiles."""
    check50.c.compile("palindrome.c", lcs50=True)

@check50.check(compiles)
def is_palindrome(self):
    """Check input: 123321"""
    check50.run("./palindrome").stdin("123321").stdout("123321 is a palindrome").exit(0)

@check50.check(compiles)
def is_not_palindrome(self):
    """Check input: 122321"""
    check50.run("./palindrome").stdin("122321").stdout("122321 is not a palindrome").exit(0)

@check50.check(compiles)
def invalid_negative_num_then_palindrome(self):
    """Check input: -123456, 123321"""
    check50.run("./palindrome").stdin("-123456").stdout("Invalid\n").stdin("123321").stdout("123321 is a palindrome").exit(0)

@check50.check(compiles)
def invalid_big_num_then_palindrome(self):
    """Check input: 1234567, 123321"""
    check50.run("./palindrome").stdin("1234567").stdout("Invalid\n").stdin("123321").stdout("123321 is a palindrome").exit(0)

