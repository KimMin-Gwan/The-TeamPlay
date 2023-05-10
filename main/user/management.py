from user import PERSON_DATA, USER_DATA
from utils import Databass
import user

# 로그인하게 해주는 클래스
# 정상작동 확인
class Login:
    def __init__(self, db):
        self.db = db
        self._user_number = -1
        self.id = 'ID'
        self.password = 'password'

    def _find_id(self, ID):
        #DB에서 아이디를 찾음
        col = user.USER_COL
        user_data = self.db.get_data_id(col, ID)
        user_id = user_data['_id']
        if user_id is -1:
            print("Wrong ID")
            return False
        self._user_number = user_id 
        # 비밀번호도 찾아옴
        self.password = user_data['password']
        return True

    # 비밀번호 확인
    def _match_password(self, password):
        if self.password == password:
            return True
        else:
            print('Wrong PW')
            return False
    
    # 유저 번호 받아가기
    def get_user_number(self):
        return self._user_number
    
    # 로그인 클래스의 핵심 기능
    def login(self, id, password):
        id_flag = self._find_id(id)
        if id_flag is False:
            return False, self._user_number
        
        pw_flag = self._match_password(password)
        if pw_flag is False:
            return False, self._user_number

        return True, self._user_number
    
# 가입 절차를 진행하는 클래스
## 정상 작동 확인
# 중복검사 해야됨
class Sign_up:
    def __init__(self, db):
        self.user = {}
        self._db = db


    def set_user_data(self, id, pw, nn, it, ng = 0):
        self.user[USER_DATA[0]] = id
        self.user[USER_DATA[1]] = pw
        self.user[USER_DATA[2]] = nn
        self.user[USER_DATA[3]] = it
        self.user[USER_DATA[4]] = ng

    def set_person_dat(self, name, sex, age, tel, email, major, grade):
        self.user[PERSON_DATA[0]] = name
        self.user[PERSON_DATA[1]] = sex 
        self.user[PERSON_DATA[2]] = age 
        self.user[PERSON_DATA[3]] = tel 
        self.user[PERSON_DATA[4]] = email 
        self.user[PERSON_DATA[5]] = major 
        self.user[PERSON_DATA[6]] = grade

    def sign_up_db(self):
        col = 'user_data'
        self._db.input_data(col, self.user)



# 유저 관리 프로세스
class User_Manager():
    def __init__(self, db): #db 매게변수로 추가해야함
        self.db = db
        self.login_flag = False
        self.user = None # 객체

    def __call__(self):
        self.user()

    # 정상 동작함
    def login(self, id, password):
        self.login = Login(self.db)
        flag, user_number = self.login.login(id, password)
        if flag is True:
            # user클래스 생성
            #user_data = self.db.get_data(user.USER_COL, user_number)
            self.user = user.User(user_number, self.db)
            self.login_flag = True 
            return self.login_flag #유저 이름도 반환해야할듯
        else:
            return self.login_flag #유저이름 반환할것

    # 정상 동작함
    def logout(self):
        self.login_flag = False
        self.user = None
    
    # 정상 동작함
    def sign_up(self):
        sign_up = Sign_up(self.db)
        return sign_up
    