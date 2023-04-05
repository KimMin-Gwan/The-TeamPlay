class Person():
    def __init__(self):
        self._name = 'Ananymous'
        self._sex = 'None'
        self._age = 0
        self._tel = '010-1234-1234'
        self._email = 'Ananymous@nothing.ac'


class Student(Person):
    def __init__(self):
        self._major = 'None'
        self._grade = 0

class user(Student):
    def __init__(self):
        self._id = 'ID'
        self._pw = 'pw'
        self._nick_name = 'random'
        self._interset = 'Nothing'
    



