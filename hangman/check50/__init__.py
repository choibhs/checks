from check50 import *


class Hangman(Checks):

    @check()
    def exists(self):
        """hangman.c exists"""
        self.require("hangman.c")

    @check("exists")
    def compiles(self):
        """hangman.c compiles"""
        self.spawn("clang -std=c11 -o hangman hangman.c -lcs50 -lm").exit(0)
