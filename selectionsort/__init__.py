import check50
import check50.c

@check50.check()
def exists():
    """selectionsort.c exists."""
    check50.exists("selectionsort.c")

@check50.check(exists)
def compiles():
    """selectionsort.c compiles."""
    check50.c.compile("selectionsort.c", lcs50=True)

@check50.check(compiles)
def basic_test(self):
        """Basic test"""
        check50.run("./selectionsort").stdout("Number of swaps: 3\nSorted array: -11, -8, 19, 24, 77")\
                .exit(0)