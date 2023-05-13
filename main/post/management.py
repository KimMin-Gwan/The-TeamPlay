from post import Post
from post.constant import MAIN_POST, GROUP_POST, POST_COL

class Post_Manager:
    def __init__(self, db, user, group):
        self.db = db
        self.user = user
        self.user = None
        self.group = None

    # 홍보하기 버튼 누르면 실행할 함수
    def make_main_post(self):
        post = Post()
        user = self.user.get_nick_name()
        group = self.group.get_group_name()
        post.set_post(MAIN_POST, user, group)
        return post
    
    def make_group_post(self):
        post = Post()
        user = self.user.get_nick_name()
        group = self.group.get_group_name()
        post.set_post(GROUP_POST, user, group)
        return post

    # 업로드 버튼을 누르면 실행할 함수
    def upload_db(self, post, title, text):
        post.input_text(title, text)
        dict_post = post.set_dict()
        self.db.input_data(POST_COL, dict_post)

    # 목록 보기 (type : str)
    def glance_board(self, type):
        # type은 두가지, 그룹이거나 메인이거나
        cursor = self.db(POST_COL, type)
        self.raw_post_data = cursor

        # 그룹 포스팅일때
        data_list = cursor
        if type is GROUP_POST:
            data_list = []
            group_name = self.group.get_group_name()
            data_list = next((data for data in cursor if data.get('group') == group_name),
                                None)
        
        glance_list = []
        for doc in data_list:
            data = {"_id" : doc["_id"],
                    "title" : doc["title"],
                    }
            glance_list.append(data)
        return glance_list
            
    def load_post(self, index):
        cursor = self.raw_post_data
        # 인덱스로 데이터 찾아오기
        doc = next((data for data in cursor if data.get('_id') == index),
                              None)

        post = Post()
        if doc :
            print(doc)
        else: # 없으면 그냥 초기화상태로 리턴시킴
            print("해당 데이터가 존재하지 않습니다.")
            return post

        # dict를 각가 변수로 변형해서 데이터 세팅
        index = doc["_id"]
        type = doc['type']
        title = doc['title']
        author = doc['author']
        group = doc['group']
        date = doc['date']
        text = doc['text']
        post.set_post(type, author, group, date, 
                        index, title, text)
            
        return  post




       

