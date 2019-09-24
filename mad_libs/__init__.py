import check50

import check50
import check50.c

@check50.check()
def exists():
    """mad_libs.c exists."""
    check50.exists("mad_libs.c")

@check50.check(exists)
def compiles():
    """mad_libs.c compiles."""
    check50.c.compile("mad_libs.c", lcs50=True)