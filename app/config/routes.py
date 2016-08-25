
from system.core.router import routes

routes['default_controller'] = 'Users'
routes['/users/home'] = 'Users#index'
routes['GET']['/users/login'] = 'Users#login_page'
routes['POST']['/users/login'] = 'Users#login'
routes['GET']['/users/register'] = 'Users#register_page'
routes['POST']['/users/register'] = 'Users#register'
routes['GET']['/users/add'] = 'Users#add_user_page'
routes['POST']['/users/add'] = 'Users#add_user'
routes['GET']['/users/edit'] = 'Users#edit_user_page'
routes['POST']['/users/edit'] = 'Users#edit_user'
routes['GET']['/users/show/<int:rx_id>'] = 'Users#show_user'

routes['POST']['/messages/create/<int:rx_id>'] = 'Messages#create_message'
routes['POST']['/comments/create/<int:rx_id>'] = 'Comments#create_comment'
