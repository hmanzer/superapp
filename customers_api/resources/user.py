
from flask_restx import Resource, fields,Namespace
from models.user import UserModel
from flask import request
from schemas.user import UserSchema

user_schema = UserSchema()

user_ns = Namespace('user', description='User related operations')
user = user_ns.model('User', {
    'name': fields.String('Name of the User'),
    'email': fields.String('Email of the user'),
    'phone': fields.String('Phone of user'),
    'address': fields.String('Address of user')
})

class User(Resource):

    def get(self, id):
        user_data = UserModel.find_by_id(id)

        if user_data:
            return user_schema.dump(user_data)
        return {'message': "User Not Found"}, 404

    @user_ns.expect(user)
    def put(self, id):

            user_data = UserModel.find_by_id(id)
            user_json = request.get_json()

            if user_data:
                user_data.name = user_json['name']
                user_data.email = user_json['email']
                user_data.phone = user_json['phone']
                user_data.address = user_json['address']
            else:
                user_data = user_schema.load(user_json)
        
            user_data.save_to_db()
            return user_schema.dump(user_data), 200

    @user_ns.expect(user)
    @user_ns.doc('Create a user')

    def post(self):
        user_json = request.get_json()
        user_data = user_schema.load(user_json)
        user_data.save_to_db()

        return user_schema.dump(user_data), 201