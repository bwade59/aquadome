#!/usr/local/bin/python3

import threading
import time
from pprint import pprint

import simplejson as json

from pymongo import MongoClient

from bson import ObjectId

from growbed import Growbed
from fishtank import Fishtank
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


class StatusReportEncoder(json.JSONEncoder):
    def default(self, obj):
        if not isinstance(obj, StatusReport):
            return super(StatusReportEncoder, self).default(obj)
        return obj.__dict__


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

        self.report = {}

        self.dbconnection = self._get_db_conn()

    def _get_db_conn(self):
        # Connection to Mongo DB
        client = MongoClient("mongodb://aquaponics:1q2w3e4r@ds161493.mlab.com:61493/aquaponicsdome")
        db = client.get_database("aquaponicsdome")
        coll = db.get_collection(("status"))
        return coll

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

    def testmongo(self):

        self.report = {"_id": 0,
                       "duration": 1,
                       "flast": 'date and time',
                       "fnext": 'date and time',
                       "fimg": 'feeding.img',
                       "fimg_time": 'date and time',
                       "watertemp": 73,
                       "ventstatus": 'closed',
                       "ph": 7.0,
                       "ambtemp": 73,
                       "pump1": 'on',
                       "pump2": 'off'}
        for i in range(50, 100):
            self.report["_id"] = ObjectId()
            self.report["ambtemp"] = i
            self.dbconnection.insert(self.report)

        x = self.dbconnection.find({})
        for i in x:
            pprint(i)

    def main(self):
        self.testmongo()
