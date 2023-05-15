import tkinter as tk
from GUI.constant import MAIN_MENU, USER_MENU1, USER_MENU2, GROUP_MENU, user


class MyGUI(tk.Tk):
    def __init__(self, main_function):
        super().__init__()
        self.main_function = main_function

        # GUI 설정
        self.title("My GUI")
        self.geometry("700x700")
        
        #self.process_canvas = tk.Canvas(self, bg="white", height=700, width=500)
        #self.process_canvas.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.main_menu()
        #self.user_menu(user)
        #self.group_menu()

    def main_menu(self):
        # 캔버스 생성 후 메인 타이틀 표기
        self.buttons = []
        for button in self.buttons:
            button.grid_forget()

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
        for button in self.buttons:
            button.grid_forget()
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
            self.login_menu = False
            self.login()
        elif index == 1 : #'회원가입':
            self.sign_up()
        elif index == 2 : #'홈화면':
            self.main_menu()


    def login(self):
        # 캔버스 생성 후 유저 정보 표기
        for button in self.buttons:
            button.grid_forget()
        print('login button clicked')
        if self.login_menu is False:
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
        self.login_menu = True
        id = self.user_id.get()
        pw = self.user_pw.get()
        flag = self.user_manager.login(id, pw)

        if flag:
            self.user_id.delete(0, tk.END)
            self.user_pw.delete(0, tk.END)
            self.button1.grid_forget()
            self.user_menu2()
        else: #재귀?
            self.user_id.delete(0, tk.END)
            self.user_pw.delete(0, tk.END)
            self.login()
        
    def sign_up(self): # 여기서부터
        # 캔버스 생성 후 유저 정보 표기
        for button in self.buttons:
            button.grid_forget()

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
        self.label_pw = tk.Label(self, text="PW:")
        self.label_pw.grid(row=2, column=0, sticky="e")
        self.user_pw = tk.Entry(self)
        self.user_pw.grid(row=2, column=3, padx=10, pady=10, sticky="ew")
        # 버튼 생성
        self.button1 = tk.Button(self, text="입력", command=self.login_check)
        self.button1.grid(row=3, column=3, padx=10, pady=10, sticky="ew")
        #self.button1.pack(pady = 10)


    def user_menu2(self):
        # 캔버스 생성 후 유저 정보 표기
        for button in self.buttons:
            button.gird_forget()
        # 유저 메뉴 버튼 생성
        self.buttons = []
        for i in range(len(USER_MENU1)):
            self.my_button = tk.Button(self,
                                    text=USER_MENU2[i],
                                    command = lambda index = i: self.handle_user_menu2(index))
            self.my_button.grid(row=i + 1, column=3, padx=10, pady=10, sticky="ew")
            #self.my_button.pack(pady = 10)
            self.buttons.append(self.my_button)



    def group_menu(self):
        # 그룹 메뉴 캔버스 생성
        self.process_canvas.delete("all")
        self.process_canvas.pack()

        # 그룹 정보 표기
        self.process_canvas.create_text(150, 50, text=f"새로운 개발자 팀 입니다.", font=("Arial", 20))
        self.process_canvas.create_text(100, 100, text=f"팀장 이름: 아무개", font=("Arial", 15))

        # 그룹 메뉴 버튼 생성
        for idx, menu in enumerate(GROUP_MENU):
            btn = tk.Button(self.process_canvas, text=menu, width=30, height=2, font=("Arial", 15))
            btn.place(x=150, y=300 + idx * 50)
            btn.bind('<Button-1>', lambda e, menu=menu: self.handle_group_menu(menu))



def main():
    gui = MyGUI()
    gui.mainloop()



if __name__ == '__main__':
    main()