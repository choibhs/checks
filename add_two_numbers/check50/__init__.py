import check50

@check50.check()
def two_positive_numbers():
    """two positive numbers"""
    check50.run("./add_two_numbers").stdin("1\n4", prompt=False).stdout("Total = 5", regex=False).exit(0)

@check50.check()
def one_pos_one_neg():
    """one pos one neg"""
    check50.run("./add_two_numbers").stdin("11\n-4", prompt=False).stdout("Total = 7", regex=False).exit(0)

@check50.check()
def two_neg():
    """two neg"""
    check50.run("./add_two_numbers").stdin("-12\n-14", prompt=False).stdout("Total = -26", regex=False).exit(0)