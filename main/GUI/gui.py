import tkinter as tk
from constant import MAIN_MENU, USER_MENU, GROUP_MENU, user


class MyGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        #self.f_main = main_function()

        # GUI 설정
        self.title("My GUI")
        self.geometry("700x700")
        
        self.process_canvas = tk.Canvas(self, bg="white", height=700, width=500)
        self.user_menu(user)
        #self.group_menu()

    def main_menu(self):
        # 캔버스 생성 후 메인 타이틀 표기
        self.process_canvas.pack()
        self.process_canvas.create_text(150, 50, text="The - TeamPlay", font=("Arial", 20))

        # 메인 메뉴 버튼 생성
        for i, menu in enumerate(MAIN_MENU):
            btn = tk.Button(self.process_canvas, text=menu, width=30, height=2, font=("Arial", 15))
            btn.place(x=150, y=100 + i * 50)
            btn.bind('<Button-1>', lambda e, menu=menu: self.handle_main_menu(menu))

    def user_menu(self, user):
        # 캔버스 생성 후 유저 정보 표기
        self.process_canvas.delete("all")
        self.process_canvas.pack()
        if user['name'] is not 'Ananymous':
            self.process_canvas.create_text(150, 50, text=f"{user['name']}님 환영합니다.", font=("Arial", 20))
            self.process_canvas.create_text(100, 100, text=f"이름: {user['name']}", font=("Arial", 15))
            self.process_canvas.create_text(100, 150, text=f"학과: {user['major']}", font=("Arial", 15))
            self.process_canvas.create_text(100, 200, text=f"ID: {user['id']}", font=("Arial", 15))
            self.process_canvas.create_text(100, 250, text=f"관심 분야: {user['interest']}", font=("Arial", 15))

        # 유저 메뉴 버튼 생성
        for i, menu in enumerate(USER_MENU):
            btn = tk.Button(self.process_canvas, text=menu, width=30, height=2, font=("Arial", 15))
            btn.place(x=150, y=300 + i * 50)
            btn.bind('<Button-1>', lambda e, menu=menu: self.handle_user_menu(menu))

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