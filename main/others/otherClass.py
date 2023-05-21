from others.constant import PROF_COL, PROF_DATA

class Rental_Post:
    def __init__():
        pass

class Professor():
    def __init__(self, pf_data):
        self._data = {}
        self._data[PROF_DATA[0]] = pf_data[PROF_DATA[0]]  # name
        self._data[PROF_DATA[1]] = pf_data[PROF_DATA[1]]  # email
        self._data[PROF_DATA[2]] = pf_data[PROF_DATA[2]]  # major
        self._data[PROF_DATA[3]] = pf_data[PROF_DATA[3]]  # office
        self._data[PROF_DATA[4]] = pf_data[PROF_DATA[4]]  # assistant_tel
        self._data[PROF_DATA[5]] = pf_data[PROF_DATA[5]]  # office_tel

    def __call__(self):
        print("Professor information")
        print("office: ", self._data[PROF_DATA[0]])
        print("assistant_tel: ", self._data[PROF_DATA[1]])
        print("office_tel: ", self._data[PROF_DATA[2]])

    def get_data(self):
        return self._data
    
    def get_name_major(self):
        nm_mj = self._data[PROF_DATA[0]] + ' , ' + self._data[PROF_DATA[2]]
        return nm_mj
        


