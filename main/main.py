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
import post
import user
import others


def main():
    login_flag = False
    print('--------->> well come to Team-play << --------------')
    print('--------   please wait for loading     -------------')

    #로딩 해야됨
    #utils.get_database()
    print('-------------- loading complete ---------------------')
    while True:

        check, menu = utils.temp_gui(login_flag)

        if check is True:
            continue
        
        # 메뉴에 따른 동작
        if menu == 1:
            post.get_post()
        elif menu == 2:
            post.get_Teams()
        # 9번은 종료키 
        elif menu == 9:
            break
        else:
            # 비회원 전용 
            if login_flag is False:
                if menu == 3:
                    user_profile, login_flag = user.login()
                else:
                    print('WRONG INPUT!!!!')
                    continue
            # 회원 전용
            else:
                if menu == 3:
                    user_profile.get_profile()
                elif menu == 4:
                    user.make_team()
                elif menu ==5:
                    others.get_Professr()
                else:
                    print('WRONG INPUT!!!!')
                    continue
        
        print('>>>>>>>>> Return to  Main Menu <<<<<<<<<')


if __name__ == "__main__":
    main()
