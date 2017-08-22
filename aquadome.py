#!/usr/local/bin/python3


from growbed import Growbed
from fishtank import Fishtank
from sumptank import Sumptank


class Aquadome:
    def __init__(self):
        self.fishtank = Fishtank()
        self.growbeds = {Growbed("GB-1"), Growbed("GB-2")}
        self.sumptank = Sumptank()
        self.airtemp = 0
        self.ventstatus = "closed"

    def getairtemp(self):
        return self.airtemp

    def setairtemp(self, wt):
        self.airtemp = wt
        return self.airtemp

    def openvent(self):
        self.ventstatus = "opened"

    def closevent(self):
        self.ventstatus = "closed"

    @staticmethod
    def main():
        print('ok')
