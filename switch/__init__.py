import check50
import check50.c

@check50.check()
def exists():
    """switch.c exists."""
    check50.exists("switch.c")

@check50.check(exists)
def compiles():
    """switch.c compiles."""
    check50.c.compile("switch.c", lcs50=True)

@check50.check(compiles)
def y(self):
    """Check input: y"""
    check50.run("./switch").stdin("y").stdout("yes\n").exit(0)

@check50.check(compiles)
def y2(self):
    """Check input: Y"""
    check50.run("./switch").stdin("Y").stdout("yes\n").exit(0)

@check50.check(compiles)
def n(self):
    """Check input: n"""
    check50.run("./switch").stdin("n").stdout("no\n").exit(0)

@check50.check(compiles)
def n2(self):
    """Check input: N"""
    check50.run("./switch").stdin("N").stdout("no\n").exit(0)
