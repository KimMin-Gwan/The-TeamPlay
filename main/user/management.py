import profileClass

# 로그인하게 해주는 클래스
class Login:
    def __init__(self):
        self._user_number = -1
        self.id = 'ID'
        self.password = 'password'

    def _find_id(self, id):
        #DB에서 아이디를 찾음
        #now_id = db.search(id)
        user_number = -1 # 임시
        if user_number is -1:
            print("Wrong ID")
            return False
        self._user_number = user_number
        # 비밀번호도 찾아옴
        # now_pw = db.serach(user_number.pw)
        now_pw = '0000'
        self.password= now_pw
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
        return self.user_numbe
    
    # 로그인 클래스의 핵심 기능
    def login(self, id, password):
        id_flag = self._find_id(id)
        if id_flag is False:
            return False, self._user_number()
        
        pw_flag = self._match_password(password)
        if pw_flag is False:
            return False, self._user_number()

        return True, self._user_number


# 유저 관리 프로세스
class User_Manager():
    def __init__(self): #db 매게변수로 추가해야함
        # self.db = db
        self.login_flag = False
        self.user_name = 'Anaymous'
        self.user_number = -1

    def __call__(self):
        print("Now User : ", self.user_name)

    def login(self, id, password):
        self.login = Login()
        flag, user_number = self.login.login(id, password)
        if flag is True:
            # user클래스 생성
            profileClass.user()
            return True #유저 이름도 반환해야할듯
        else:
            return False #유저이름 반환할것

    def logout(self):
        pass

    def sign_in(self):


