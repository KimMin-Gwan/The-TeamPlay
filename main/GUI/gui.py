import tkinter as tk
from GUI.constant import MAIN_MENU, USER_MENU1, USER_MENU2, GROUP_MENU
from post.constant import MAIN_POST, GROUP_POST, POST_COL

class MyGUI(tk.Tk):
    def __init__(self, main_function):
        super().__init__()
        self.main_function = main_function
        self.post_manager = main_function.post_management()
        # GUI 설정
        self.title("My GUI")
        self.geometry("700x700")
        self.login_flag = False
        self.group_manager = None
        #self.process_canvas = tk.Canvas(self, bg="white", height=700, width=500)
        #self.process_canvas.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.main_menu()
        #self.user_menu(user)
        #self.group_menu()

    def remove_all_widgets(self):
        # 모든 위젯 제거
        for widget in self.winfo_children():
            widget.destroy()

    def main_menu(self):
        # 캔버스 생성 후 메인 타이틀 표기
        self.remove_all_widgets()
        self.buttons = []

        for i in range(len(MAIN_MENU)):
            self.my_button = tk.Button(self,
                                    text=MAIN_MENU[i],
                                    command = lambda index = i: self.handle_main_menu(index))
            self.my_button.grid(row=i + 1, column=0, padx=10, pady=10, sticky="ew")
            #self.my_button.pack(pady = 10)
            self.buttons.append(self.my_button)



    def handle_main_menu(self, index):
        if index == 0 : #'사용자 관리':
            self.user_management()
        elif index == 1 : #'그룹 검색':
            self.group_search()
        elif index == 2 : #'교수님 찾기':
            self.professor_search()
        elif index == 3 : # '종료':
            self.exit_application()

    def user_management(self):
        # 사용자 관리 버튼의 프로토타입 함수
        print("User management button clicked")
        self.user_manager = self.main_function.user_management()
        if self.login_flag:
            self.user_menu2()
        else:
            self.user_menu1()

    def group_search(self):
        # 그룹 검색 버튼의 프로토타입 함수
        print("Group search button clicked")

    def professor_search(self):
        # 교수님 찾기 버튼의 프로토타입 함수
        print("Professor search button clicked")

    def exit_application(self):
        # 종료 버튼의 프로토타입 함수
        self.destroy()

    def user_menu1(self):
        # 캔버스 생성 후 유저 정보 표기
        #for button in self.buttons:
        #    button.grid_forget()
        self.remove_all_widgets()
        # 유저 메뉴 버튼 생성
        self.buttons = []
        for i in range(len(USER_MENU1)):
            self.my_button = tk.Button(self,
                                    text=USER_MENU1[i],
                                    command = lambda index = i: self.handle_user_menu1(index))
            #self.my_button.pack(pady = 10)
            self.my_button.grid(row=i + 1, column=0, padx=10, pady=10, sticky="ew")
            self.buttons.append(self.my_button)


    def handle_user_menu1(self, index):
        if index == 0 : #'로그인':
            #self.login_menu = False
            self.login()
        elif index == 1 : #'회원가입':
            self.sign_up_set = self.user_manager.sign_up()
            self.sign_up()
        elif index == 2 : #'홈화면':
            self.main_menu()


    def login(self):
        # 캔버스 생성 후 유저 정보 표기
        self.remove_all_widgets()
        print('login button clicked')
        self.label_id = tk.Label(self, text="ID:")
        self.label_id.grid(row=1, column=0, sticky="e")
        self.user_id = tk.Entry(self)
        self.user_id.grid(row=1, column=3, padx=10, pady=10, sticky="ew")
        #self.user_id.pack(pady = 10)
        self.label_pw = tk.Label(self, text="PW:")
        self.label_pw.grid(row=2, column=0, sticky="e")
        self.user_pw = tk.Entry(self)
        self.user_pw.grid(row=2, column=3, padx=10, pady=10, sticky="ew")
        #self.user_pw.pack(pady = 10)
        # 버튼 생성
        self.button1 = tk.Button(self, text="입력", command=self.login_check)
        self.button1.grid(row=3, column=3, padx=10, pady=10, sticky="ew")
        #self.button1.pack(pady = 10)

    def login_check(self):
        #self.login_menu = True
        id = self.user_id.get()
        pw = self.user_pw.get()
        flag = self.user_manager.login(id, pw)

        if flag:
            self.user_id.delete(0, tk.END)
            self.user_pw.delete(0, tk.END)
            self.button1.grid_forget()
            # 포스트 매니저도 같이 로그인해줘야됨
            self.post_manager.set_user(self.user_manager.get_user())
            self.user_menu2()
        else: #재귀?
            self.user_id.delete(0, tk.END)
            self.user_pw.delete(0, tk.END)
            self.login()
        
    def sign_up(self): # 여기서부터
        # 캔버스 생성 후 유저 정보 표기

        self.remove_all_widgets()

        self.label_id = tk.Label(self, text="ID :")
        self.label_id.grid(row=1, column=0, sticky="e")
        self.user_id = tk.Entry(self)
        self.user_id.grid(row=1, column=3, padx=10, pady=10, sticky="ew")

        self.label_pw = tk.Label(self, text="PW :")
        self.label_pw.grid(row=2, column=0, sticky="e")
        self.user_pw = tk.Entry(self)
        self.user_pw.grid(row=2, column=3, padx=10, pady=10, sticky="ew")

        self.label_nn = tk.Label(self, text="Nick_name :")
        self.label_nn.grid(row=3, column=0, sticky="e")
        self.user_nn = tk.Entry(self)
        self.user_nn.grid(row=3, column=3, padx=10, pady=10, sticky="ew")

        self.label_it = tk.Label(self, text="Interest :")
        self.label_it.grid(row=4, column=0, sticky="e")
        self.user_it = tk.Entry(self)
        self.user_it.grid(row=4, column=3, padx=10, pady=10, sticky="ew")

        self.label_name = tk.Label(self, text="name :")
        self.label_name.grid(row=5, column=0, sticky="e")
        self.user_name = tk.Entry(self)
        self.user_name.grid(row=5, column=3, padx=10, pady=10, sticky="ew")

        self.label_sex = tk.Label(self, text="Sex :")
        self.label_sex.grid(row=6, column=0, sticky="e")
        self.user_sex = tk.Entry(self)
        self.user_sex.grid(row=6, column=3, padx=10, pady=10, sticky="ew")

        self.label_age = tk.Label(self, text="Age :")
        self.label_age.grid(row=7, column=0, sticky="e")
        self.user_age = tk.Entry(self)
        self.user_age.grid(row=7, column=3, padx=10, pady=10, sticky="ew")

        self.label_tel = tk.Label(self, text="tel :")
        self.label_tel.grid(row=8, column=0, sticky="e")
        self.user_tel = tk.Entry(self)
        self.user_tel.grid(row=8, column=3, padx=10, pady=10, sticky="ew")

        self.label_email = tk.Label(self, text="Email :")
        self.label_email.grid(row=9, column=0, sticky="e")
        self.user_email = tk.Entry(self)
        self.user_email.grid(row=9, column=3, padx=10, pady=10, sticky="ew")

        self.label_major = tk.Label(self, text="Major :")
        self.label_major.grid(row=10, column=0, sticky="e")
        self.user_major = tk.Entry(self)
        self.user_major.grid(row=10, column=3, padx=10, pady=10, sticky="ew")

        self.label_grade = tk.Label(self, text="Grade :")
        self.label_grade.grid(row=11, column=0, sticky="e")
        self.user_grade = tk.Entry(self)
        self.user_grade.grid(row=11, column=3, padx=10, pady=10, sticky="ew")

        # 버튼 생성
        self.button1 = tk.Button(self, text="입력", command=self.sign_up_check)
        self.button1.grid(row=12, column=3, padx=10, pady=10, sticky="ew")
        #self.button1.pack(pady = 10)

    def sign_up_check(self):
        #self.login_menu = True
        id = self.user_id.get()
        pw = self.user_pw.get()
        nn = self.user_nn.get()
        it = self.user_it.get()
        name = self.user_name.get()
        sex = self.user_sex.get()
        age = self.user_age.get()
        tel = self.user_tel.get()
        email = self.user_email.get()
        major = self.user_major.get()
        grade = self.user_grade.get()

        self.sign_up_set.set_user_data(id, pw, nn, it)
        self.sign_up_set.set_person_data(name, sex, age, tel, email, major, grade)

        self.sign_up_set.sign_up_db()

        self.remove_all_widgets()
        self.user_menu1()

    def user_menu2(self):
        # 캔버스 생성 후 유저 정보 표기
        self.remove_all_widgets()

        # 유저 메뉴 버튼 생성
        self.buttons = []
        for i in range(len(USER_MENU2)):
            self.my_button = tk.Button(self,
                                    text=USER_MENU2[i],
                                    command = lambda index = i: self.handle_user_menu2(index))
            self.my_button.grid(row=i + 1, column=3, padx=10, pady=10, sticky="ew")
            #self.my_button.pack(pady = 10)
            self.buttons.append(self.my_button)

    def handle_user_menu2(self, index):
        if self.group_manager is None:
            self.group_manager = self.main_function.group_management()

        if index == 0 : #'로그아웃':
            self.login_flag = False
            self.user_manager.logout()
            self.group_manager = None
            self.main_menu()
        elif index == 1 : #'회원 정보 편집':
            pass # 나중에 만들자
        elif index == 2 : #'그룹 생성':
            self.mk_group_manager = self.group_manager.make_group()
            self.make_group()
        elif index == 3 : #'그룹 확인':
            self.check_group()
        elif index == 4 : #'홈 화면':
            self.main_menu()

    def make_group(self):
        self.remove_all_widgets()
        self.label_gn = tk.Label(self, text="Group Name :")
        self.label_gn.grid(row=1, column=0, sticky="e")
        self.group_name = tk.Entry(self)
        self.group_name.grid(row=1, column=3, padx=10, pady=10, sticky="ew")

        self.label_pp = tk.Label(self, text="Purpose :")
        self.label_pp.grid(row=2, column=0, sticky="e")
        self.purpose = tk.Entry(self)
        self.purpose.grid(row=2, column=3, padx=10, pady=10, sticky="ew")

        self.label_size = tk.Label(self, text="Size of Group:")
        self.label_size.grid(row=3, column=0, sticky="e")
        self.group_size = tk.Entry(self)
        self.group_size.grid(row=3, column=3, padx=10, pady=10, sticky="ew")

        # 버튼 생성
        self.button1 = tk.Button(self, text="입력", command=self.make_group_check)
        self.button1.grid(row=12, column=3, padx=10, pady=10, sticky="ew")
        #self.button1.pack(pady = 10)
        
    def make_group_check(self):
        #self.login_menu = True
        gn = self.group_name.get()
        pp = self.purpose.get()
        size = int(self.group_size.get())

        self.mk_group_manager.set_group_data(gn, pp, size)

        self.mk_group_manager.make_group_db()

        self.remove_all_widgets()
        self.user_menu2()

    def check_group(self):
        # 다지우기
        self.remove_all_widgets()

        self.group_manager.set_groups()
        self.group_list, _ = self.group_manager.set_show_group()

        # 그룹 갯수 판별
        if len(self.group_list) is 0:
            self.group_label = tk.Label(self, text="가입한 그룹이 없어요.")
            self.group_label.grid(row=3, column=0, sticky="e")
            # 버튼 생성
            self.button1 = tk.Button(self, text="이전화면", command=self.user_menu2)
            self.button1.grid(row=12, column=3, padx=10, pady=10, sticky="ew")
            #self.button1.pack(pady = 10)
        else:
            self.buttons = []
            self.group_label = tk.Label(self, text="그룹 리스트")
            self.group_label.grid(row=1, column=1, sticky="e")

            for i in range(len(self.group_list)):
                self.my_button = tk.Button(self,
                                        text=self.group_list[i].get_group_name(),
                                        command = lambda index = i: self.group_menu(index))
                self.my_button.grid(row=2, column=i + 1, padx=10, pady=10, sticky="ew")
                #self.my_button.pack(pady = 10)
                self.buttons.append(self.my_button)
            self.button1 = tk.Button(self, text="이전화면", command=self.user_menu2)
            self.button1.grid(row=3, column=1, padx=10, pady=10, sticky="ew")


    def group_menu(self, index):
        self.remove_all_widgets()
        self.post_manager.set_group(self.group_list[index])
        g_index = self.group_list[index].get_group_index()
        group_name = self.group_list[index].get_group_name()
        member = self.group_list[index].get_group_member()
        size = self.group_list[index].get_group_size()
        #purpose = self.group_list[index].get_group_purpose()
        # 그룹 메뉴 캔버스 생성
        self.process_canvas = tk.Canvas(self, bg="white", height=300, width=500)
        self.process_canvas.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # 그룹 정보 표기
        self.process_canvas.create_text(150, 50, text=f"{group_name} 팀 입니다.", font=("Arial", 20))
        self.process_canvas.create_text(100, 100, text=f"팀장 이름: {member[0]}", font=("Arial", 15))

        # 그룹 메뉴 버튼 생성
        for i in range(len(GROUP_MENU)):
            self.my_button = tk.Button(self,
                                    text=GROUP_MENU[i],
                                    command = lambda index = i: self.handle_group_menu(index))
            self.my_button.grid(row=i + 1, column=0, padx=10, pady=10, sticky="ew")
            #self.my_button.pack(pady = 10)
            self.buttons.append(self.my_button)

    def handle_group_menu(self, index):
        if index == 0 : #'그룹 포스트 ':
            self.explore_group_post()
        elif index == 1 : #'렌탈 신청':
            pass # 나중에 만들자
        elif index == 2 : #'이슈 등록' :
            pass # 이거는 그룹 클래스에 포함 시키자
        elif index == 3 : # '홍보글 작성':
            self.exit_application()
        elif index == 4 : # '그룹 탈퇴':
            pass # 이것도 만들어야됨
        elif index == 5 : # '홈 화면':
            self.main_menu()

    def explore_group_post(self):
        self.remove_all_widgets()
        post_list = self.post_manager.glance_board(GROUP_POST)
        i = 0
        self.glance_canvases= []
        self.buttons = []
        for post in post_list:          
            # 그룹 메뉴 캔버스 생성
            self.glance_canvas= tk.Canvas(self, bg="white", height=100, width=500)
            self.glance_canvas.grid(row=i + 1, column=0, columnspan=2, padx=10, pady=10)
            # 그룹 정보 표기
            self.glance_canvas.create_text(100, 50, text=f"{post['title']}", font=("Arial", 20))
            self.glance_canvases.append(self.glance_canvas)
            # 버튼
            self.my_button = tk.Button(self, text="자세히", 
                                       command=lambda idx=i: self.load_post(idx) )
            self.my_button.grid(row=i+1, column=1, padx=10, pady=10, sticky="ew")
            self.buttons.append(self.my_button)

            i += 1

        self.button1 = tk.Button(self, text="포스팅하기", command=self.posting)
        self.button1.grid(row=i + 1, column=1, padx=10, pady=10, sticky="ew")
        
    def posting(self):
        self.remove_all_widgets()

        self.label_post_title= tk.Label(self, text="title :")
        self.label_post_title.grid(row=1, column=0, sticky="e")
        self.post_title= tk.Entry(self)
        self.post_title.grid(row=1, column=3, padx=10, pady=10, sticky="ew")

        self.label_post_text= tk.Label(self, text="Text :")
        self.label_post_text.grid(row=2, column=0, sticky="e")
        self.post_text= tk.Entry(self)
        self.post_text.grid(row=2, column=3, padx=10, pady=10, sticky="ew")

        

        # 버튼 생성
        self.button1 = tk.Button(self, text="업로드", command=self.group_post_upload)
        self.button1.grid(row=12, column=3, padx=10, pady=10, sticky="ew")

    def group_post_upload(self):
        post = self.post_manager.make_group_post()
        title = self.post_title.get()
        text = self.post_text.get()

        self.post_manager.upload_db(post, title, text)
        self.remove_all_widgets()
        self.explore_group_post()




    def load_post(self, index):
        pass


