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

    def main(self):
        print('ok')
        for gb in self.growbeds:
            print(gb.getmydesignation())
        self.fishtank.feedfish()
        self.fishtank.setph(6.8)
        print("ph: %0.2f" % self.fishtank.getph())
        self.fishtank.setwatertemp(75)
        print("water temp: %0.1f" % self.fishtank.getwatertemp())
        self.setairtemp(75)
        print("air temp: %0.1f" % self.getairtemp())
