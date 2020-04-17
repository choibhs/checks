import check50
import check50.c

@check50.check()
def exists():
    """bubblesort.c exists."""
    check50.exists("bubblesort.c")

@check50.check(exists)
def compiles():
    """bubblesort.c compiles."""
    check50.c.compile("bubblesort.c", lcs50=True)

@check50.check(compiles)
def basic_test(self):
        """Basic test"""
        check50.run("./bubblesort").stdout("Number of comparisons 10, number of swaps: 6\nSorted array: -19, 0, 19, 24, 77")\
                .exit(0)