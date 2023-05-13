import user
from user import PERSON_DATA, USER_DATA, GROUP_POINT

class Person():
    def __init__(self, user_number, db):
        user_data = db.get_data(user.USER_COL, user_number)
        self._data_p = {
            "name": user_data[PERSON_DATA[0]],
            "sex": user_data[PERSON_DATA[1]],
            "age": user_data[PERSON_DATA[2]],
            "tel": user_data[PERSON_DATA[3]],
            "email": user_data[PERSON_DATA[4]],
            "major": user_data[PERSON_DATA[5]],
            "grade": user_data[PERSON_DATA[6]]
        }

    def get_data(self):
        return self._data_p

    def set_data(self, data):
        self._data_p = data

    def get_property(self, property_name):
        return self._data_p.get(property_name)

    def set_property(self, property_name, value):
        self._data_p[property_name] = value


class User(Person):
    def __init__(self, user_number, db):
        #user_data = db.find_one({"_id": user_number})
        super().__init__(user_number, db)
        user_data = db.get_data(user.USER_COL, user_number)
        self._data = {}
        self.user_number = user_number
        self._data[USER_DATA[0]] = user_data[USER_DATA[0]]
        self._data[USER_DATA[1]] = user_data[USER_DATA[1]]
        self._data[USER_DATA[2]] = user_data[USER_DATA[2]]
        self._data[USER_DATA[3]] = user_data[USER_DATA[3]]
        self._data[USER_DATA[4]] = user_data[USER_DATA[4]]

        self._group_list = []
        for i in range(self._data[USER_DATA[4]]):
            self._group_list.append(user_data[GROUP_POINT[i]])

    def __call__(self):
        print("User Information:")
        print("ID:", self._data[USER_DATA[0]])
        print("Password:", self._data[USER_DATA[1]])
        print("Nick Name:", self._data[USER_DATA[2]])
        print("Interest:", self._data[USER_DATA[3]])
        print("Number of Groups:", self._data[USER_DATA[4]])

        print("\nPerson Information:")
        print("Name:", self._data_p["name"])
        print("Sex:", self._data_p["sex"])
        print("Age:", self._data_p["age"])
        print("Telephone:", self._data_p["tel"])
        print("Email:", self._data_p["email"])
        print("Major:", self._data_p["major"])
        print("Grade:", self._data_p["grade"])

    def get_group_list(self):
        return self._group_list

    def get_num_group(self):
        return self._data[USER_DATA[4]]

    def get_user_number(self):
        return self.user_number

    def get_id(self):
        return self._data[USER_DATA[0]]

    def get_pw(self):
        return self._data[USER_DATA[1]]

    def get_nick_name(self):
        return self._data[USER_DATA[2]]

    def get_interest(self):
        return self._data[USER_DATA[3]]

    def get_property(self, property_name):
        return self._data.get(property_name)

    def set_property(self, property_name, value):
        self._data[property_name] = value

    def set_group_list(self, index):
        self._group_list.append(index)
        self._data[USER_DATA[4]] += 1

