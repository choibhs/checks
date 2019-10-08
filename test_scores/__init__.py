import check50
import check50.c

@check50.check()
def exists():
    """test_scores.c exists."""
    check50.exists("test_scores.c")

@check50.check(exists)
def compiles():
    """test_scores.c compiles."""
    check50.c.compile("test_scores.c", lcs50=True)

@check50.check(compiles)
def two_as_two_bs_one_f(self):
    """Check inputs: 100, 90, 85, 83, 33, -20"""
    check50.run("./test_scores")\
        .stdin("100").stdout("Number of A's: 1, 100.0%\nNumber of B's: 0, 0.0%\nNumber of C's: 0, 0.0%\nNumber below C: 0, 0.0%\n\n")\
        .stdin("90").stdout("Number of A's: 2, 100.0%\nNumber of B's: 0, 0.0%\nNumber of C's: 0, 0.0%\nNumber below C: 0, 0.0%\n\n")\
        .stdin("85").stdout("Number of A's: 2, 66.7%\nNumber of B's: 1, 33.3%\nNumber of C's: 0, 0.0%\nNumber below C: 0, 0.0%\n\n")\
        .stdin("83").stdout("Number of A's: 2, 50.0%\nNumber of B's: 2, 50.0%\nNumber of C's: 0, 0.0%\nNumber below C: 0, 0.0%\n\n")\
        .stdin("33").stdout("Number of A's: 2, 40.0%\nNumber of B's: 2, 40.0%\nNumber of C's: 0, 0.0%\nNumber below C: 1, 20.0%\n\n")\
        .stdin("-20").exit(0)

@check50.check(compiles)
def two_bs_two_cs_one_d_one_f(self):
    """Check inputs: 77, 82, 87, 2, -1"""
    check50.run("./test_scores")\
        .stdin("77").stdout("Number of A's: 0, 0.0%\nNumber of B's: 0, 0.0%\nNumber of C's: 1, 100.0%\nNumber below C: 0, 0.0%\n\n")\
        .stdin("82").stdout("Number of A's: 0, 0.0%\nNumber of B's: 1, 50.0%\nNumber of C's: 1, 50.0%\nNumber below C: 0, 0.0%\n\n")\
        .stdin("87").stdout("Number of A's: 0, 0.0%\nNumber of B's: 2, 66.7%\nNumber of C's: 1, 33.3%\nNumber below C: 0, 0.0%\n\n")\
        .stdin("2").stdout("Number of A's: 0, 0.0%\nNumber of B's: 2, 50.0%\nNumber of C's: 1, 25.0%\nNumber below C: 1, 25.0%\n\n")\
        .stdin("-1").exit(0)
