## main.py

"""
1. welcome 메세지 띄우기
2. 데이터 베이스 연결하기

3-1. 1. 게시판 보기
3-3. 2. 그룹 카테고리 보기
3. 만약 로그인 안했다면 == 비회원 메뉴판 보여주기
3-2. 3. 로그인 하기

4. 만약 로그인 했을시 == 회원 게시판 보여주기
4-1. 3. 내 프로필 보기 
4-2. 4. 팀 만들기
4-3. 5. 교수님 찾기

5. 메뉴 고르기
6. 메뉴 맞는지 확인하기
7. 만약 메뉴 고른게 맞다면 -> 지시에 맞게 수행
8. 아니면 -> 컨티뉴

"""

import utils
#import post
import user
#import others
import GUI
import group

"""
1. 메인 메뉴 켜면 뭐해야됨?
 - db 연결해야됨 -> 성공
 - 사용자 관리 클래스 생성 -> 로그인, 회원가입 성공
 - 그룹 검색 클래스 생성
 - 교수님 찾기 클래스생성?
 - 종료 버튼
2. 사용자 관리 클래스에서 뭐해야됨
 - 로그인, 회원가입 -> 정상 동작
 - 그룹 확인 -> 그룹 확인 및 수정 동작
 - 그룹 생성 -> 그룹 생성해야됨
"""


#메인 펑션 해서 UI랑 연동해야됨
class Main_Function:
    def __init__(self):
        self.db = utils.Databass()

    def user_management(self):
        self.user_manager = user.User_Manager(self.db)
        return self.user_manager
    
    def group_management(self):
        self.now_user = self.user_management.get_user()
        self.group_manager = group.Group_Manger(self.db, self.now_user)


from bson.objectid import ObjectId
import pprint

def main():
    main_function = Main_Function()
    gui = GUI.MyGUI(main_function)
    gui.mainloop()
    









if __name__ == "__main__":
    main()
