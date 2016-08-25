
from system.core.controller import *

class Messages(Controller):
    def __init__(self, action):
        super(Messages, self).__init__(action)
        self.load_model('MessageModel')
        self.db = self._app.db

    def create_message(self,rx_id):
        route = '/users/'
        tx_id = session['user']['id']
        self.models['MessageModel'].create_message(request.form, rx_id, tx_id)
        return redirect('/users/show/'+str(rx_id))

    def get_messages(self):
        pass
