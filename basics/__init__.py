import check50
import check50.c

@check50.check()
def exists():
    """basics.c exists."""
    check50.exists("basics.c")

@check50.check(exists)
def compiles():
    """basics.c compiles."""
    check50.c.compile("basics.c", lcs50=True)

@check50.check(compiles)
def basic_test(self):
        """Basic test"""
        check50.run("./basics").stdin("Mr. T").stdout("Hello, Mr. T!\n").stdin("20").stdout("You are 20 years old\nIn twenty years you will be 40\n")\
                .stdin("1").stdin("2").stdin("3").stdin("4").stdin("5")\
                .stdout("Your zip code is: 12345\nYour zip code reversed is: 54321")\
                .exit(0)

@check50.check(compiles)
def second_test(self):
        """Second test"""
        check50.run("./basics").stdin("SpongeBob").stdout("Hello, SpongeBob!\n").stdin("22").stdout("You are 22 years old\nIn twenty years you will be 42\n")\
                .stdin("7").stdin("6").stdin("3").stdin("4").stdin("1")\
                .stdout("Your zip code is: 76341\nYour zip code reversed is: 14367")\
                .exit(0)