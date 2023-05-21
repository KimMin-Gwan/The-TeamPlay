from group.constant import GROUP_COL, GROUP_DATA

class Group:
    def __init__(self, db, index):
        data = db.get_data_index(GROUP_COL, index)
        self._id = data['_id']
        self._group_member = []
        self.index = data[GROUP_DATA[0]]
        self._group_name = data[GROUP_DATA[1]]
        self._group_purpose = data[GROUP_DATA[2]]
        self._size = data[GROUP_DATA[3]]
        self._group_issue = data[GROUP_DATA[4]]

        for i in range (self._size):
            if i == 0:
                self._group_member.append(data['Master'])
            else:
                self._group_member.append(data['Member' + str(i)])

    def __call__(self):
        print("group index : ", self.index)
        print("group group name : ", self._group_name)
        print("group group purpose : ", self._group_purpose)
        print("group group size : ", self._size)
        print("group member : ", self._group_member)
        print("group issue : ", self._group_issue)

    def set_group_issue(self, txt):
        self._group_issue = txt
        return self._id
    
    def set_group_member(self, key, name):
        self._group_member[key] = name

    def get_group_id(self):
        return self._id

    def get_issue(self):
        return self._group_issue

    def get_group_member(self):
        return self._group_member

    def get_group_index(self):
        return self.index

    def get_group_name(self):
        return self._group_name

    def get_group_purpose(self):
        return self._group_purpose

    def get_group_size(self):
        return self._size