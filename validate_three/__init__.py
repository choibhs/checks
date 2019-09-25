import check50
import check50.c

@check50.check()
def exists():
    """validate_three.c exists."""
    check50.exists("validate_three.c")

@check50.check(exists)
def compiles():
    """validate_three.c compiles."""
    check50.c.compile("validate_three.c", lcs50=True)

@check50.check(compiles)
def vii(self):
    """"""
    check50.run("./validate_three").stdin("24").stdout("That response is valid\n").stdin("2").stdout("That response is invalid\n").stdin("24").stdout("That response is invalid\n").exit(0)

@check50.check(compiles)
def ivv(self):
    """"""
    check50.run("./validate_three").stdin("0").stdout("That response is invalid\n").stdin("y").stdout("That response is valid\n").stdin("30").stdout("That response is valid\n").exit(0)
