from pymongo import MongoClient


class PostContent:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.codewizardtest
        self.Users = self.db.Users
        self.Posts = self.db.Posts

    def post_content(self, data):
        inserted_post = self.Posts.insert_one({"username": data.username, "posts": data.content})
        return True

    def get_all_posts(self):
        all_posts = self.Posts.find()
        new_posts = []

        for posts in all_posts:
            posts['user'] = self.Users.find_one({"username": posts['username']})
            new_posts.append(posts)

        return new_posts
