import sqlite3
from flask_restful import Resource, reqparse
from Models.user import UserModel



class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                       type=str,
                       required=True,
                       help= 'This field is requiered!')
    parser.add_argument('password',
                       type=str,
                       required=True,
                       help= 'This field is requiered!')

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message":"username already exist!"}, 400

        UserModel(data['username'],data['password']).save_to_db() #we can also do UserModel(**data).save_to_db()
        return {"message":"User created successfully!"}, 201
