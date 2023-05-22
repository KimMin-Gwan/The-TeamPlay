from group import GROUP_COL, GROUP_DATA
from user import GROUP_POINT, USER_COL
from group.groupClass import Group

"""
1. 그룹 확인 -> 그룹 확인 및 수정 동작  : 정상 동작함
2. 그룹 생성 -> 그룹 생성해야됨         : 정상 동작함
3. 그룹 관리 -> 그룹호출하고, 포스팅, 이슈, 멤버 삭제
"""

"""
해야하는일
1. 그룹 클래스 만들기 정상 동작
2. 포스팅 기능 만들기 이제 만들어야됨
3. 포스팅에서 그룹에 참가하기 기능 구현
"""

# 그룹 만드는 클래스
# 정상동작함
# 상속할껄
class Make_Group:
    def __init__(self, db, user):
        self.db = db 
        self.user = user
        self.group = {}

    # 생성창에서 데이터 받아서 실행
    def set_group_data(self, name, purpose, size):
        self.group[GROUP_DATA[1]] = name
        self.group[GROUP_DATA[2]] = purpose
        self.group[GROUP_DATA[3]] = size
        self.group[GROUP_DATA[4]] = 'None'
        for i in range(size):
            if i == 0:
                self.group['Master'] = self.user.get_nick_name()
            else:
                self.group['Member' + str(i)] = 'None'

        temp_index  = self.db.get_size_col(GROUP_COL)
        if temp_index is not -1:
            index = temp_index + 1
        else:
            print('Wrong Col')
            return
        self.group[GROUP_DATA[0]] = index 

    # 버튼 누르면 이거 실행
    def make_group_db(self):
        self.db.input_data(GROUP_COL, self.group)
        self.db.update_data(USER_COL, 
                            self.user.get_user_number(), # 유저넘버
                            'num_group', #그룹
                            self.user.get_num_group() + 1  # 그룹 인덱스
                            )
        self.db.update_data(USER_COL, 
                            self.user.get_user_number(), # 유저넘버
                            GROUP_POINT[self.user.get_num_group()], #그룹
                            self.group[GROUP_DATA[0]]  # 그룹 인덱스
                            )
        self.user.set_group_list(self.group[GROUP_DATA[0]])

"""
그룹 메니저가 하는일
1. 그룹 생성 : 가능
2. 그룹 확인 : 가능
3. 그룹 수정 : 불가능
"""

class Group_Manger:
    def __init__(self, db, user):
        self.db = db
        self._user = user
        self._group_list = [] # 그룹 인덱스 보관
        self._num_group = 0
        self._group_data = []
    
    # 그룹 메니저 세팅?
    def set_groups(self):
        self._group_list = self._user.get_group_list()
        self._num_group = self._user.get_num_group()
        print('test : ', self._num_group)
        temp = None
        self._group_data = []
        for arg in self._group_list:
            temp = self.db.get_data_id(GROUP_COL, arg)
            self._group_data.append(temp)

    #def get_groups(self):
    #    return self._group_data, self._num_group
    
    # 그룹 생성하기
    def make_group(self):
        mk_group = Make_Group(self.db, self._user)
        return mk_group
    
    # 그룹 보여주기 및 객체로 생성하기
    # 정상동작 확인
    def set_show_group(self):
        self._groups = []
        for arg in self._group_list:
            group = Group(self.db, arg)
            self._groups.append(group)
        
        return self._groups, self._num_group
    
    def set_issue(self, index, new_issue):
        group = self._groups[index]
        id = group.set_group_issue(new_issue)
        self.db.update_data(GROUP_COL, id, 'issue', new_issue)

    def join_group(self, group, txt):
        
        group_data = self.db.get_data_name(GROUP_COL, group)
        id = group_data["index"] # 그룹 index
        name = self._user.get_nick_name()
        data = {'index' : id,
                'name' : name,
                'txt' : txt
                }

        self.db.input_data('join_data', data)
    
    def show_join_txt(self, index):
        group = self._groups[index]
        group_id= group.get_group_index()
        print(group_id)
        data = self.db.get_data_list2('join_data', group_id)
        print(data)
        return data

    def allow_join_group(self, index, data):
        group = self._groups[index]
        id = group.get_group_id()
        name = data['name']
        this_group = data['index']
        member_list = group.get_group_member()
        print(member_list)
        i = 0
        for arg in member_list:
            print(arg)
            if arg == 'None':
                print('here')
                group.set_group_member(i, name)
                self.db.update_data(GROUP_COL, id, 'Member' + str(i), name)
                break
            else:
                i += 1

        user = self.db.get_data_nick_name(USER_COL, name)

        self.db.update_data(USER_COL, 
                            user['_id'], # 유저넘버
                            'num_group', #그룹
                            user['num_group'] + 1  # 그룹 인덱스
                            )
        self.db.update_data(USER_COL, 
                            user['_id'], # 유저넘버
                            GROUP_POINT[user['num_group']],#그룹
                            this_group  # 그룹 인덱스
                            )
        self.db.delete_data('join_data', '_id', data['_id'])

        print('정상등록')

        print('new print')

