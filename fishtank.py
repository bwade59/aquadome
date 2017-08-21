#!/usr/local/bin/python3

from datetime import datetime
from time import sleep


class Fishtank:
    def __init__(self):
        self.lastfeeding = datetime.now().time()
        self.ph = self.setph(7.0)
        self.watertemp = self.setwatertemp(75)
        self.waterheatstatus = 0
        self.lastwaterheaton = datetime.now().time()
        self.lastwaterheatoff = datetime.now().time()
        self.feederonduration = 1

    def getph(self):
        return self.ph

    def setph(self, ph):
        self.ph = ph
        return self.ph

    def getwatertemp(self):
        return self.watertemp

    def setwatertemp(self, wt):
        self.watertemp = wt
        return self.watertemp

    def feedfish(self):
        print("feeder open")
        sleep(self.feederonduration)
        print("feeder closed")
        pass

    def viewfish(self):
        pass

    def waterheaton(self):
        self.lastwaterheaton = datetime.now().time()

    def waterheatoff(self):
        self.lastwaterheatoff = datetime.now().time()
