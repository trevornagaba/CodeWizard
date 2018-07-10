import pymongo, bcrypt
from pymongo import MongoClient


class LoginModel:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.codewizardtest
        self.Users = self.db.Users

    def check_user(self, data):
        myUser = self.Users.find_one({"username":data.username})

        if myUser:
            if bcrypt.checkpw(data.password.encode(), myUser["password"].encode()):
                return myUser
            else:
                return False
        else:
            return False
