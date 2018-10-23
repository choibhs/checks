import re

from check50 import *

class Arrays(Checks):

    @check()
    def exists(self):
        """arrays.c exists."""
        self.require("arrays.c")

    @check("exists")
    def compiles(self):
        """arrays.c compiles."""
        self.spawn("clang -std=c11 -o arrays arrays.c").exit(0)
