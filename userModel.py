class User():
    def __init__(self,id,first_name,last_name,username,contact = '000'):
        self.id = id
        self.first_name = str(first_name)
        self.last_name = str(last_name)
        self.username = username
        self.contact = contact

def create_user(data_user):
    user = User(data_user.id,data_user.first_name,data_user.last_name,data_user.username)
    return user

def user_to_json(user:User):
    json_user = {
        user.id:{
            'last_name':user.last_name,
            'first_name':user.first_name,
            'username': user.username,
            'contact':user.contact
        }
    }
    return json_user


