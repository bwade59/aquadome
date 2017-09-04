#!/usr/local/bin/python3

import threading
import time
from pprint import pprint

from bson import ObjectId
from pymongo import MongoClient

from fishtank import Fishtank
from growbed import Growbed
from sumptank import Sumptank


class StatusReport(object):
    info = {
        "duration": 1,
        "flast": [],
        "fnext": [],
        "fimg": [],
        "fimg_time": [],
        "watertemp": 73,
        "ventstatus": [],
        "ph": 7.0,
        "ambtemp": 73,
        "pump1": [],
        "pump2": []}


class Aquadome(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.report = StatusReport()
        self.threadID = 1
        self.name = "Aquadome"
        self.exitflag = 0
        self.fishtank = Fishtank()
        self.growbeds = {Growbed("GB-1"), Growbed("GB-2")}
        self.sumptank = Sumptank()
        self.ventstatus = 'closed'
        self.ambtemp = 0
        self.report = {}
        self.dbconnection = self._get_db_conn()

    @staticmethod
    def _get_db_conn():
        # Connection to Mongo DB
        client = MongoClient("mongodb://aquaponics:1q2w3e4r@ds161493.mlab.com:61493/aquaponicsdome")
        db = client.get_database("aquaponicsdome")
        coll = db.get_collection("status")
        return coll

    def run(self):
        print("Starting " + self.name)
        while True:
            print('ok')
            for gb in self.growbeds:
                print(gb.getmydesignation())
            self.fishtank.feedfish()
            self.fishtank.setph(6.8)
            print("ph: %0.2f" % self.fishtank.getph())
            self.fishtank.setwatertemp(75)
            print("water temp: %0.1f" % self.fishtank.getwatertemp())
            self.setambtemp(75)
            print("air temp: %0.1f" % self.getambtemp())
            time.sleep(2)

    def getambtemp(self):
        return self.ambtemp

    def setambtemp(self, wt):
        self.ambtemp = wt
        return self.ambtemp

    def openvent(self):
        self.ventstatus = "opened"

    def closevent(self):
        self.ventstatus = "closed"

    def getventstatus(self):
        return self.ventstatus

    def buildreport(self):
        self.report["_id"] = ObjectId()
        self.report["watertemp"] = self.fishtank.getwatertemp()
        self.report["ph"] = self.fishtank.getph()
        self.report["ambtemp"] = self.getambtemp()
        self.report["pump1"] = self.sumptank.getpump1status()
        self.report["pump2"] = self.sumptank.getpump2status()
        self.report["ventstatus"] = self.getventstatus()
        self.report["flast"] = self.fishtank.getflast()
        self.report["fnext"] = self.fishtank.getfnext()
        self.report["fimg"] = self.fishtank.getfimg()
        self.report["fimg_time"] = self.fishtank.getfimgtime()

    def testmongo(self):

        self.buildreport()
        self.dbconnection.insert(self.report)

        x = self.dbconnection.find({})
        for i in x:
            pprint(i)

    def main(self):
        self.testmongo()
