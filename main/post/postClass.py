import datetime
from post.constant import POST
from bson.objectid import ObjectId

class Post():
    def __init__(self):
        self.index = None  #db 에서 받아온 _id가 인덱스
        self.type = 'None'
        self.title = 'title'
        self.author = 'Ananymous'
        self.group = 'Group'
        self.date = datetime.datetime.utcnow()
        self.text = 'temp'

    def __call__(self):
        print("post index : ", self.index)
        print("post type : ", self.type)
        print("post title: ", self.title)
        print("post author : ", self.author)
        print("post group : ", self.group)
        print("post date : ", self.date)
        print("post text: ", self.text)

    def set_post(self, type, user, group, date = None, 
                 index = None, title = 't', text = 't'):
        index = None
        self.type = type
        self.author = user
        self.group = group
        self.date = date
        self.index = index
        self.title= title
        self.text= text

    def set_post2(self, type, user, group, date,
                 index = None, title = 't', text = 't'):
        index = None
        self.type = type
        self.author = user
        self.group = group
        self.date = date
        self.index = index
        self.title= title
        self.text= text

    def input_text(self, title, text):
        self.title = title
        self.text = text

    def set_dict(self):
        dict_post = {}
        dict_post['type'] = self.type
        dict_post['title'] = self.title
        dict_post['author'] = self.author
        dict_post['group'] = self.group
        dict_post['text'] = self.text
        return dict_post

    
    def get_author(self):
        return self.author
    
    def get_date(self):
        return self.date

    def get_title(self):
        return self.title
    
    def get_text(self):
        return self.text

    def get_group(self):
        return self.group





