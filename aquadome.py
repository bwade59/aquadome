#!/usr/local/bin/python3


from growbed import Growbed
from control import Control
from fishtank import Fishtank
from sumptank import Sumptank


class Aquadome:
    def __init__(self):
        self.control = Control()
        self.fishtank = Fishtank()
        self.growbeds = {Growbed("GB-1"), Growbed("GB-2")}
        self.sumptank = Sumptank()

    @staticmethod
    def main():
        print('ok')
