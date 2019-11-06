import check50
import check50.c


@check50.check()
def exists():
    """binary exists"""
    check50.exists("binary.c")


@check50.check(exists)
def compiles():
    """binary compiles"""
    check50.c.compile("binary.c", lcs50=True)

@check50.check(compiles)
def test201a(self):
    """Invalid menu input, then input of 11001001 yields output of 201"""
    check50.run("./binary").stdin("-1").stdin("1").stdin("1").stdin("1").stdin("0").stdin("0").stdin("1").stdin("0").stdin("0").stdin("1").stdout("201\n").exit(0)

@check50.check(compiles)
def test201b(self):
    """Invalid menu input, then input of 201 yields output 11001001"""
    check50.run("./binary").stdin("0").stdin("2").stdin("201").stdout("11001001\n").exit(0)

@check50.check(compiles)
def test23a(self):
    """Invalid binary number input, then input of 00010111 yields output of 23"""
    check50.run("./binary").stdin("1").stdin("12").stdin("0").stdin("0").stdin("0").stdin("1").stdin("0").stdin("1").stdin("1").stdin("1").stdout("23\n").exit(0)

@check50.check(compiles)
def test23b(self):
    """Invalid decimal number input, then input of 23 yields output 00010111"""
    check50.run("./binary").stdin("2").stdin("-1").stdin("322").stdin("23").stdout("00010111\n").exit(0)

@check50.check(compiles)
def test_reject_negative(self):
    """rejects a negative input like -.1"""
    check50.run("./binary").stdin("-1").reject()

