import check50
import check50.c

@check50.check()
def exists():
    """guessing.c exists."""
    check50.exists("guessing.c")

@check50.check(exists)
def compiles():
    """guessing.c compiles."""
    check50.c.compile("guessing.c", lcs50=True)

@check50.check(compiles)
def four_tries(self):
    """Check inputs: 4, 22, 62, 53"""
    check50.run("./guessing").stdin("4").stdout("That number is too low\n").stdin("22").stdout("That number is too low\n").stdin("62").stdout("That number is too high\n").stdin("53").stdout("You guessed the secret number!\n").exit(0)

@check50.check(compiles)
def one_try(self):
    """Check inputs: 4, 22, 62, 53"""
    check50.run("./guessing").stdin("53").stdout("You guessed the secret number!\n").exit(0)

@check50.check(compiles)
def three_tries(self):
    """Check inputs: 54, 52, 53"""
    check50.run("./guessing").stdin("54").stdout("That number is too high\n").stdin("52").stdout("That number is too low\n").stdin("53").stdout("You guessed the secret number!\n").exit(0)
