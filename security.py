from werkzeug.security import safe_str_cmp
#from Resources.user import User
from Models.user import UserModel

"""These methods are part of the Flask-JWT module which adds basic JWT features to our Flask application.
It has been designed in such a way that we can only get the user id using payload['identity']
since that is the most important thing needed for authentication."""


def authenticate(username,password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password): #This syntax is the same than this one : if user is not None and user.password == password
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
