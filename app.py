import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT



from security import authenticate, identity
from Resources.user import UserRegister
from Resources.item import Item, ItemList
from Resources.store import Store, StoreList



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' #It means that the sqlalchemy database is going to live at the root folder of our project.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'
api = Api(app)



jwt =JWT(app,authenticate,identity) #/auth

api.add_resource(Store, '/store/<string:name>') #http://127.0.0.1:5000/store/<name>
api.add_resource(Item,'/item/<string:name>') #http://127.0.0.1:5000/item/<name>
api.add_resource(ItemList,'/items') #http://127.0.0.1:5000/items
api.add_resource(StoreList,'/stores') #http://127.0.0.1:5000/stores
api.add_resource(UserRegister,'/register') #http://127.0.0.1:5000/register

if __name__ == '__main__':
    app.run(port=5001, debug=True)
