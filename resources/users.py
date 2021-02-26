from flask import jsonify, Blueprint

from flask_restful import Resource, Api, reqparse, fields, marshal, marshal_with

import models

user_fields = {
	'name': fields.String,
	'phone': fields.String,
	'email': fields.String
}

class UserList(Resource):
	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		self.reqparse.add_argument(
			'name',
			required=True,
			location=['form', 'json']
		)
		self.reqparse.add_argument(
			'phone',
			required=True,
			location=['form', 'json']
		)
		self.reqparse.add_argument(
			'email',
			required=True,
			location=['form', 'json']
		)
		super().__init__()
	
	def get(self):
		users = [marshal(user, user_fields)
			for user in models.User.select()]
		return jsonify({'users': users})

	def post(self):
		args = self.reqparse.parse_args()
		models.User.create(**args)
		return jsonify({'users': [{'name': 'mehri'}]})

class User(Resource):
	pass

users_api = Blueprint('resources.users', __name__)
api = Api(users_api)
api.add_resource(
	UserList,
	'/api/v1/users',
	endpoint='users'
)
api.add_resource(
	User,
	'/api/v1/user/<int:id>',
	endpoint='user'
)