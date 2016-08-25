from system.core.model import Model

class UserModel(Model):
    def __init__(self):
        super(UserModel, self).__init__()

    def register_user(self, user_info):
        #validate user info HERE
        pw_hash = self.bcrypt.generate_password_hash(user_info['pwd'])
        first_user_check = self.db.query_db('select * from users')
        if len(first_user_check) < 1:
            user_level = 9
        else:
            user_level = 1

        data = {
            'email' : user_info['email'],
            'first_name' : user_info['fname'],
            'last_name' : user_info['lname'],
            'password' : pw_hash,
            'user_level' : user_level
        }
        query =  'INSERT INTO users (email, first_name, last_name, password, user_level) '
        query += 'VALUE(:email, :first_name, :last_name, :password, :user_level)'
        new_user_id = self.db.query_db(query,data)
        data2 = {
            'id' : new_user_id
        }
        query2 =  'SELECT * FROM users WHERE users.id = :id LIMIT 1;'
        user = self.db.query_db(query2, data2)
        if len(user) != 1: return None
        return user[0]

    def login_user(self, user_info):
        #VALIDATE DATA HERE
        data = {
            'email' : user_info['email'],
            'password' : user_info['pwd']
        }
        query = 'SELECT * FROM users WHERE users.email = :email LIMIT 1'
        user = self.db.query_db(query, data)

        check = self.bcrypt.check_password_hash(user[0]['password'], data['password'])
        if not check:
            return None
        return user[0]


    def get_users(self):
        query = 'SELECT * FROM users'
        users = self.db.query_db(query)
        return users

    def get_user(self,user_id):
        print user_id
        data = {'id':user_id}
        query = 'SELECT * FROM users WHERE users.id = :id LIMIT 1'
        user = self.db.query_db(query, data)
        return user[0]

    def edit_user(self, user_info):
        pass
