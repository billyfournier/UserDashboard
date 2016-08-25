
from system.core.controller import *

class Comments(Controller):
    def __init__(self, action):
        super(Comments, self).__init__(action)
        self.load_model('CommentModel')
        self.db = self._app.db

    def create_comment(self,rx_id):
        msg_id = request.form
        tx_id = session['user']['id']
        self.models['CommentModel'].create_comment(request.form, tx_id)
        return redirect('/users/show/'+str(rx_id))

    def get_comments(self):
        pass
