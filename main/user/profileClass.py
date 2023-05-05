class Person():
    def __init__(self):
        self._name = 'Ananymous'
        self._sex = 'None'
        self._age = 0
        self._tel = '010-1234-1234'
        self._email = 'Ananymous@nothing.ac'
        self._major = 'None'
        self._grade = 0


class user(Person):
    def __init__(self, user_number, db):
        super.__init__()
        user_data = db.find_one({"_id" : user_number})
        self._id = user_data['identify']
        self._pw = user_data['password']
        self._nick_name = user_data['nick_name']
        self._interest = user_data['interest']

    



