import check50
import check50.c


@check50.check()
def exists():
    """geometry exists"""
    check50.exists("geometry.c")


@check50.check(exists)
def compiles():
    """geometry compiles"""
    check50.c.compile("geometry.c", lcs50=True)

@check50.check(compiles)
def test1():
    """Compiles and then runs invalid menu item 1, then area of rectangle 10 x 10"""
    check50.run("./geometry").stdin("-1").stdin("0").stdin("1").stdin("1").stdin("10").stdin("10").stdout("The rectangle's area is 100.\n").exit(0)

@check50.check(compiles)
def test1():
    """Compiles and then runs invalid menu item 1, then area of rectangle 10 x 10"""
    check50.run("./geometry").stdin("-1").stdin("0").stdin("1").stdin("1").stdin("10").stdin("10").stdout("The rectangle's area is 100.\n").exit(0)

@check50.check(compiles)
def test2():
    """Compiles and then runs invalid rectangle lengths (negative and 0), then area of rectangle 4 x 5"""
    check50.run("./geometry").stdin("1").stdin("1").stdin("-1").stdin("0").stdin("4").stdin("5").stdout("The rectangle's area is 20.\n").exit(0)

@check50.check(compiles)
def test3():
    """Compiles and then runs invalid menu item 2, then area of square 4"""
    check50.run("./geometry").stdin("1").stdin("-1").stdin("4").stdin("2").stdin("4").stdout("The square's area is 16.\n").exit(0)

@check50.check(compiles)
def test4():
    """Compiles and then runs invalid square length negative or 0, then area of square 7"""
    check50.run("./geometry").stdin("1").stdin("2").stdin("-7").stdin("0").stdin("7").stdout("The square's area is 49.\n").exit(0)

@check50.check(compiles)
def test5():
    """Compiles and then runs invalid triangle length negative or 0, then invalid lengths, area of triangle 3, 4, 5"""
    check50.run("./geometry").stdin("1").stdin("3")\
            .stdin("-7").stdin("0").stdin("7").stdout("Invalid inputs. All sides must be > 0.\n")\
            .stdin("3").stdin("4").stdin("50").stdout("Invalid inputs. The sum of two sides must be > the third side.")\
            .stdin("3").stdin("4").stdin("5").stdout("The triangle's area is 6.0.\n").exit(0)

@check50.check(compiles)
def test6():
    """Compiles and then runs invalid rectangle lengths (negative and 0), then perimeter of rectangle 4 x 5"""
    check50.run("./geometry").stdin("2").stdin("1").stdin("-1").stdin("0").stdin("4").stdin("5").stdout("The rectangle's perimeter is 18.\n").exit(0)

@check50.check(compiles)
def test7():
    """Compiles and then runs invalid square length negative or 0, then perimeter of square 7"""
    check50.run("./geometry").stdin("2").stdin("2").stdin("-7").stdin("0").stdin("7").stdout("The square's perimeter is 28.\n").exit(0)

@check50.check(compiles)
def test8():
    """Compiles and then runs invalid triangle length negative or 0, then invalid lengths, then perimeter of triangle 3, 4, 5"""
    check50.run("./geometry").stdin("2").stdin("3")\
            .stdin("-7").stdin("0").stdin("7").stdout("Invalid inputs. All sides must be > 0.\n")\
            .stdin("3").stdin("4").stdin("50").stdout("Invalid inputs. The sum of two sides must be > the third side.")\
            .stdin("3").stdin("4").stdin("5").stdout("The triangle's perimeter is 12.\n").exit(0)
