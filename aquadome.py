#!/usr/local/bin/python3

import threading
import time

from growbed import Growbed
from fishtank import Fishtank
from sumptank import Sumptank


class Aquadome(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.threadID = 1
        self.name = "Aquadome"
        self.exitflag = 0
        self.fishtank = Fishtank()
        self.growbeds = {Growbed("GB-1"), Growbed("GB-2")}
        self.sumptank = Sumptank()
        self.airtemp = 0
        self.ventstatus = "closed"

    def run(self):
        print("Starting " + self.name)
        while (True):
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
            time.sleep(2)
        print("Exiting " + self.name)

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
        self.run()
