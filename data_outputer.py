__author__ = "Liang"
__Date__ = 2017 / 8 / 17

from pymongo import MongoClient

class data_outputer(object):

    def __init__(self):
        self.db=MongoClient("localhost",27017).tiebadata

    def insert(self,item):
        ttable=(self.db)["topicinfo"]
        ttable.insert(item)