#!/usr/local/bin/python3

from datetime import datetime
from time import sleep


class Fishtank:
    def __init__(self):

        self.ph = 7.0
        self.watertemp = 0
        self.waterheatstatus = 0
        self.lastwaterheaton = datetime.now().time().isoformat()
        self.lastwaterheatoff = datetime.now().time().isoformat()
        self.feederonduration = 1
        self.flast = datetime.now().time().isoformat()
        self.fnext = datetime.now().time().isoformat()
        self.fimg = "feeding.img"
        self.fimg_time = datetime.now().time().isoformat()

    def getflast(self):
        return self.flast

    def getfnext(self):
        return self.fnext

    def getfimg(self):
        return self.fimg

    def getfimgtime(self):
        return self.fimg_time

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
        self.lastwaterheaton = datetime.now().time().isoformat()

    def waterheatoff(self):
        self.lastwaterheatoff = datetime.now().time().isoformat()
