import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
bb =client.moteur_recherche
def donnee_job():
    for obj in bb.flashbot.find():
     print(obj)
    return 
