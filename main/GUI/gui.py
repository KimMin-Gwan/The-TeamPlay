import tkinter as tk
from tkinter.font import Font
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
        self.remove_all_widgets()
        post_list = self.post_manager.glance_board(MAIN_POST)
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
                                       command=lambda idx=i: self.load_main_post(idx) )
            self.my_button.grid(row=i+1, column=1, padx=10, pady=10, sticky="ew")
            self.buttons.append(self.my_button)

            i += 1

        self.button1 = tk.Button(self, text="메인메뉴", command=self.main_menu)
        self.button1.grid(row=i + 1, column=1, padx=10, pady=10, sticky="ew")


    def load_main_post(self, index):
        # 지우기
        self.remove_all_widgets()
        post = self.post_manager.load_post(index)
        self.main_post_group = post.get_group()

        title = post.get_title()
        author = post.get_author()
        raw_date = post.get_date()
        date = raw_date.strftime("%Y-%m-%d %H:%M:%S.%f")
        title = post.get_title()
        text = post.get_text()

        self.process_canvas = tk.Canvas(self, bg="white", height=200, width=500)
        self.process_canvas.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        # 그룹 정보 표기
        self.process_canvas1 = tk.Canvas(self, bg="white", height=400, width=500)
        self.process_canvas1.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.process_canvas.create_text(150, 50, text=f"제목 : {title}", font=("Arial", 20))
        self.process_canvas.create_text(100, 100, text=f"작성자 : {author}", font=("Arial", 15))
        self.process_canvas.create_text(200, 150, text=f"작성일 : {date}", font=("Arial", 15))   

        lines = []
        wraplength =400
        current_line = ""
        words = text.split()


        font = Font(family="Arial", size=20)  # 폰트 설정
        for word in words:
            if font.measure(current_line + " " + word) <= wraplength:
                current_line += " " + word
            else:
                lines.append(current_line)
                current_line = word

        lines.append(current_line)

        y = 50  # 시작 y 좌표
        for line in lines:
            self.process_canvas1.create_text(500// 2, y, text=line, font=font, anchor=tk.CENTER)
            y += 30  # 줄 간격 조정

        # 이거 만들어야됨
        self.button2 = tk.Button(self, text="가입신청", command=self.join_group)
        self.button2.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        self.button1 = tk.Button(self, text="이전화면", command=self.group_search)
        self.button1.grid(row=3, column=1, padx=10, pady=10, sticky="ew")


    # 가입 신청을 넣음
    # 그룹 db에 추가
    # 그룹장이 가입 신청을 받음
    # 신청 받기
    # 그룹 db에서 삭제

    def join_group(self):
        self.remove_all_widgets()

        self.label_join_txt= tk.Label(self, text="Introduce :")
        self.label_join_txt.grid(row=1, column=0, sticky="e")
        self.join_txt= tk.Entry(self)
        self.join_txt.grid(row=1, column=3, padx=10, pady=10, sticky="ew")

        self.button1 = tk.Button(self, text="신청하기", command=self.join_check)
        self.button1.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    def join_check(self):

        group_name = self.main_post_group
        join_txt = self.join_txt.get()
        self.group_manager.join_group(group_name, join_txt)

        self.remove_all_widgets()

        self.join_check_label= tk.Label(self, text="신청되었습니다!")
        self.join_check_label.grid(row=1, column=1, sticky="e")

        self.button1 = tk.Button(self, text="홈으로", command=self.main_menu)
        self.button1.grid(row=3, column=1, padx=10, pady=10, sticky="ew")


    def professor_search(self):
        # 다지우기
        self.remove_all_widgets()

        self.pf_list = self.main_function.professor_management()

        # 그룹 갯수 판별
        if len(self.pf_list) is 0:
            self.group_label = tk.Label(self, text="등록된 교수님이 없어요.")
            self.group_label.grid(row=3, column=0, sticky="e")
            # 버튼 생성
            self.button1 = tk.Button(self, text="이전화면", command=self.user_menu2)
            self.button1.grid(row=12, column=3, padx=10, pady=10, sticky="ew")
            #self.button1.pack(pady = 10)
        else:
            self.buttons = []
            self.group_label = tk.Label(self, text="교수님 리스트")
            self.group_label.grid(row=1, column=1, sticky="e")

            for i in range(len(self.pf_list)):
                self.my_button = tk.Button(self,
                                        text=self.pf_list[i].get_name_major(),
                                        command = lambda index = i: self.get_pf_detail(index))
                self.my_button.grid(row=2, column=i + 1, padx=10, pady=10, sticky="ew")
                #self.my_button.pack(pady = 10)
                self.buttons.append(self.my_button)
            self.button1 = tk.Button(self, text="이전화면", command=self.main_menu)
            self.button1.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    def get_pf_detail(self, index):
        # 다지우기
        self.remove_all_widgets()

        prof = self.pf_list[index]
        pf_data = prof.get_data()
        name = pf_data['name']
        email = pf_data['email']
        major = pf_data['major']
        office = pf_data['office']
        ass_tel = pf_data['assistant_tel']
        office_tel = pf_data['office_tel']

        self.process_canvas = tk.Canvas(self, bg="white", height=400, width=500)
        self.process_canvas.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # 그룹 정보 표기
        self.process_canvas.create_text(150, 50, text=f"{name} 교수님", font=("Arial", 20))
        self.process_canvas.create_text(100, 100, text=f"전공 : {major}", font=("Arial", 15))
        self.process_canvas.create_text(140, 150, text=f"이메일 : {email}", font=("Arial", 15))   
        self.process_canvas.create_text(80, 200, text=f"연구실 : {office}", font=("Arial", 15))   
        self.process_canvas.create_text(130, 250, text=f"조교 번호 : {ass_tel}", font=("Arial", 15))   
        self.process_canvas.create_text(130, 300, text=f"연구실 번호 : {office_tel}", font=("Arial", 15))   


        self.button1 = tk.Button(self, text="이전화면", command=self.professor_search)
        self.button1.grid(row=3, column=1, padx=10, pady=10, sticky="ew")


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
        self.button2 = tk.Button(self, text="홈으로", command=self.main_menu)
        self.button2.grid(row=3, column=2, padx=10, pady=10, sticky="ew")

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
            self.login_flag = True 
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

        self.button2 = tk.Button(self, text="홈으로", command=self.main_menu)
        self.button2.grid(row=12, column=2, padx=10, pady=10, sticky="ew")
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
        self.now_group_index = index
        self.remove_all_widgets()
        self.post_manager.set_group(self.group_list[index])
        g_index = self.group_list[index].get_group_index()
        group_name = self.group_list[index].get_group_name()
        member = self.group_list[index].get_group_member()
        issue = self.group_list[index].get_issue()
        size = self.group_list[index].get_group_size()
        #purpose = self.group_list[index].get_group_purpose()
        # 그룹 메뉴 캔버스 생성
        self.process_canvas = tk.Canvas(self, bg="white", height=200, width=500)
        self.process_canvas.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # 그룹 정보 표기
        self.process_canvas.create_text(150, 50, text=f"{group_name} 팀 입니다.", font=("Arial", 20))
        self.process_canvas.create_text(100, 100, text=f"팀장 이름: {member[0]}", font=("Arial", 15))
        self.process_canvas.create_text(100, 150, text=f"공지 : {issue}", font=("Arial", 15))   

        # 그룹 메뉴 버튼 생성
        for i in range(len(GROUP_MENU)):
            self.my_button = tk.Button(self,
                                    text=GROUP_MENU[i],
                                    command = lambda index = i: self.handle_group_menu(index))
            self.my_button.grid(row=i + 1, column=0, padx=10, pady=10, sticky="ew")
            #self.my_button.pack(pady = 10)
            self.buttons.append(self.my_button)

        if self.user_manager.get_user().get_nick_name() == member[0]:
            self.button1 = tk.Button(self, text="신청확인", command=self.show_join)
            self.button1.grid(row=8, column=0, padx=10, pady=10, sticky="ew")

    def show_join(self):
        self.remove_all_widgets()

        index = self.now_group_index
        self.join_data = self.group_manager.show_join_txt(index)

        if len(self.join_data) is 0:
            self.group_label = tk.Label(self, text="신청이 없어요.")
            self.group_label.grid(row=3, column=0, sticky="e")
            # 버튼 생성
            self.button1 = tk.Button(self, text="이전화면", command=self.user_menu2)
            self.button1.grid(row=12, column=3, padx=10, pady=10, sticky="ew")
            #self.button1.pack(pady = 10)
        else:
            self.buttons = []
            self.group_label = tk.Label(self, text="신청 리스트")
            self.group_label.grid(row=1, column=1, sticky="e")
            i = 0
            for join_data in self.join_data:
                self.my_button = tk.Button(self,
                                        text=join_data['name'],
                                        command = lambda index = i: self.show_join_detail(index))
                self.my_button.grid(row=2, column=i + 1, padx=10, pady=10, sticky="ew")
                #self.my_button.pack(pady = 10)
                self.buttons.append(self.my_button)
            self.button1 = tk.Button(self, text="이전화면", command=self.user_menu2)
            self.button1.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    def show_join_detail(self, index):
        self.remove_all_widgets()

        self.temp_index = index
        data = self.join_data[index]
        name = data["name"]
        txt = data['txt']

        self.group_label = tk.Label(self, text=f"이름 : {name}")
        self.group_label.grid(row=0, column=1, sticky="e")
        self.group_label = tk.Label(self, text=f"소개 : {txt}")
        self.group_label.grid(row=1, column=1, sticky="e")

        self.button1 = tk.Button(self, text="이전화면", command=self.user_menu2)
        self.button1.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

        self.button2 = tk.Button(self, text="승인", command=self.allow_join_group)
        self.button2.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

    def allow_join_group(self):
        group_index = self.now_group_index
        data = self.join_data[self.temp_index]  
        self.group_manager.allow_join_group(group_index, data)
        self.user_menu2()

    def handle_group_menu(self, index):
        if index == 0 : #'그룹 포스트 ':
            self.explore_group_post()
        elif index == 1 : #'렌탈 신청':
            pass # 나중에 만들자
        elif index == 2 : #'이슈 등록' :
            self.change_issue()
        elif index == 3 : # '홍보글 작성':
            self.posting_type = 1
            self.posting()
        elif index == 4 : # '그룹 탈퇴':
            pass # 이것도 만들어야됨
        elif index == 5 : # '홈 화면':
            self.main_menu()

    def change_issue(self):
        self.remove_all_widgets()
        index = self.now_group_index
        issue = self.group_list[index].get_issue()
        self.label_now_issue = tk.Label(self, text=f"현재 이슈 : {issue}")
        self.label_now_issue.grid(row=0, column=0, sticky="e")

        self.label_issue = tk.Label(self, text="New Issue :")
        self.label_issue.grid(row=1, column=0, sticky="e")
        self.group_issue = tk.Entry(self)
        self.group_issue.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        self.button1 = tk.Button(self, text="변경", command=self.issue_update)
        self.button1.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    def issue_update(self):
        new_issue = self.group_issue.get()
        index = self.now_group_index

        self.group_manager.set_issue(index, new_issue)

        self.remove_all_widgets()
        self.user_menu2()

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
                                       command=lambda idx=i: self.load_group_post(idx) )
            self.my_button.grid(row=i+1, column=1, padx=10, pady=10, sticky="ew")
            self.buttons.append(self.my_button)

            i += 1

        self.posting_type = 0
        self.button1 = tk.Button(self, text="포스팅하기", command=self.posting)
        self.button1.grid(row=i + 1, column=1, padx=10, pady=10, sticky="ew")

        self.button2 = tk.Button(self, text="메인메뉴", command=self.main_menu)
        self.button2.grid(row=i + 1, column=0, padx=10, pady=10, sticky="ew")
        
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

        if self.posting_type ==  0:
            self.button1 = tk.Button(self, text="업로드", command=self.group_post_upload)
            self.button1.grid(row=12, column=3, padx=10, pady=10, sticky="ew")
        else:
            self.button1 = tk.Button(self, text="업로드", command=self.main_post_upload)
            self.button1.grid(row=12, column=3, padx=10, pady=10, sticky="ew")

    def main_post_upload(self):
        post = self.post_manager.make_main_post()
        title = self.post_title.get()
        text = self.post_text.get()

        self.post_manager.upload_db(post, title, text)
        self.remove_all_widgets()
        self.main_menu()

    def group_post_upload(self):
        post = self.post_manager.make_group_post()
        title = self.post_title.get()
        text = self.post_text.get()

        self.post_manager.upload_db(post, title, text)
        self.remove_all_widgets()
        self.explore_group_post()



    def load_group_post(self, index):
        # 지우기
        self.remove_all_widgets()
        post = self.post_manager.load_post(index)

        title = post.get_title()
        author = post.get_author()
        raw_date = post.get_date()
        date = raw_date.strftime("%Y-%m-%d %H:%M:%S.%f")
        title = post.get_title()
        text = post.get_text()

        self.process_canvas = tk.Canvas(self, bg="white", height=200, width=500)
        self.process_canvas.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        # 그룹 정보 표기
        self.process_canvas1 = tk.Canvas(self, bg="white", height=400, width=500)
        self.process_canvas1.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.process_canvas.create_text(150, 50, text=f"제목 : {title}", font=("Arial", 20))
        self.process_canvas.create_text(100, 100, text=f"작성자 : {author}", font=("Arial", 15))
        self.process_canvas.create_text(200, 150, text=f"작성일 : {date}", font=("Arial", 15))   

        lines = []
        wraplength =400
        current_line = ""
        words = text.split()


        font = Font(family="Arial", size=20)  # 폰트 설정
        for word in words:
            if font.measure(current_line + " " + word) <= wraplength:
                current_line += " " + word
            else:
                lines.append(current_line)
                current_line = word

        lines.append(current_line)

        y = 50  # 시작 y 좌표
        for line in lines:
            self.process_canvas1.create_text(500// 2, y, text=line, font=font, anchor=tk.CENTER)
            y += 30  # 줄 간격 조정

        self.button1 = tk.Button(self, text="이전화면", command=self.explore_group_post)
        self.button1.grid(row=3, column=1, padx=10, pady=10, sticky="ew")


