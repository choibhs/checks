import check50
import check50.c


@check50.check()
def exists():
    """triangle exists"""
    check50.exists("triangle.c")

@check50.check(exists)
def compiles():
    """triangle.c compiles."""
    check50.c.compile("triangle.c", lcs50=True)

@check50.check(compiles)
def test_invalid_then_3():
    """input of -2 then 3"""
    check50.run("./triangle").stdin("-2").stdin("3").stdout("#\n##\n###\n").exit(0)


@check50.check(compiles)
def test_invalid_then_7():
    """input of 0 then 7"""
    check50.run("./triangle").stdin("0").stdin("7").stdout("#\n##\n###\n####\n#####\n######\n#######\n").exit(0)