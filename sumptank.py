#!/usr/local/bin/python3


class Sumptank:
    def __init__(self):
        self.pump1status = 'off'
        self.pump2status = 'off'

    def setpump1(self, newstate):
        self.pump1status = newstate

    def getpump1status(self):
        return self.pump1status

    def setpump2(self, newstate):
        self.pump2status = newstate

    def getpump2status(self):
        return self.pump2status
