from system.core.model import Model

class CommentModel(Model):
    def __init__(self):
        super(CommentModel, self).__init__()

    def create_comment(self, msg, tx_id):
        data = {
            'user_id' : tx_id,
            'message_id' : msg['msg_id'],
            'text' : msg['comment']
        }
        query = 'INSERT INTO comments (text, user_id, message_id) VALUE (:text, :user_id, :message_id)'
        self.db.query_db(query, data)
        return True

    def get_comments(self,rx_id):
        query = 'SELECT * FROM comments WHERE comments.message_id = '
        # msgs = self.db.query_db(query,{'rx_id':rx_id})
        return msgs
