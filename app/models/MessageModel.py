from system.core.model import Model

class MessageModel(Model):
    def __init__(self):
        super(MessageModel, self).__init__()

    def create_message(self, msg, rx_id, tx_id):
        print "-" * 40
        msg = dict(msg)
        print msg
        data = {
            'rx_id' : rx_id,
            'tx_id' : tx_id,
            'text' : msg['comment'][0]
        }
        print data
        query = 'INSERT INTO messages (text, user_id_rx, user_id_tx) VALUE (:text, :rx_id, :tx_id)'
        self.db.query_db(query,data)
        return True

    def get_messages(self,rx_id):
        query =  'SELECT * FROM messages '
        query += 'JOIN users ON user_id_tx = users.id '
        query += 'WHERE messages.user_id_rx = :rx_id'
        msgs = self.db.query_db(query,{'rx_id':rx_id})
        return msgs
