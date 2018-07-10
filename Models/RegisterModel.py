import pymongo
from pymongo import MongoClient
import bcrypt

class RegisterModel:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.codewizardtest
        self.Users = self.db.Users

    def insert_user(self, data):
        hashed = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt())

        id = self.Users.insert({"username": data.username, "Full name": data.name, "email": data.email, "password": hashed})
        print ("User id is", id)

