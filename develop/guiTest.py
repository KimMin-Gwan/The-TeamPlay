import tkinter as tk

class LoginWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.username_entry = tk.Entry(self)
        self.password_entry = tk.Entry(self, show="*")
        self.login_button = tk.Button(self, text="로그인", command=self.login)

        self.username_entry.pack()
        self.password_entry.pack()
        self.login_button.pack()

    def login(self):
        # 로그인 로직을 처리하는 코드
        # 예를 들면, 사용자가 입력한 정보를 확인하고 인증하는 과정 등

        # 로그인 성공 시 다른 클래스로 이동
        self.master.switch_to_other_window()

class OtherWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.label = tk.Label(self, text="다른 창")
        self.label.pack()

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("메인 창")
        self.geometry("300x200")

        self.login_window = LoginWindow(self)
        self.other_window = OtherWindow(self)

        self.login_window.pack()

    def switch_to_other_window(self):
        self.login_window.pack_forget()
        self.other_window.pack()

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
