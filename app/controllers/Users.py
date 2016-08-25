
from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('UserModel')
        self.load_model('MessageModel')
        self.db = self._app.db


    def index(self):
        if 'user' in session:
            users = self.models['UserModel'].get_users()
            print session['user']
            if session['user']['user_level'] == 9:
                return self.load_view('admin.html', users=users, this_user=session['user'])
            else:
                return self.load_view('user.html', users=users, this_user=session['user'])
        else:
            return self.load_view('index.html')

    def login_page(self):
        return self.load_view('login.html')
    def register_page(self):
        return self.load_view('register.html')

    def add_user_page(self):
        if 'user' in session:
            if session['user']['user_level'] == 9:
                return self.load_view('add.html')
        return redirect('/')

    def logoff(self):
        session.pop('user')
        return redirect('/')

    def login(self):
        user = self.models['UserModel'].login_user(request.form)
        if user is None: return redirect('/')
        session['user'] = user
        return redirect('/')

    def register(self):
        user = self.models['UserModel'].register_user(request.form)
        if user is None: return redirect('/')
        session['user'] = user
        return redirect('/')


    def add_user(self):
        self.models['UserModel'].register_user(request.form)
        return redirect('/')

    def edit_user_page(self):
        pass
    def edit_user(self):
        pass

    def show_user(self,rx_id):
        tx =  session['user']
        user = self.models['UserModel'].get_user(rx_id)
        msgs = self.models['MessageModel'].get_messages(rx_id)
        return self.load_view('message.html', user=user, me=tx, messages=msgs)
