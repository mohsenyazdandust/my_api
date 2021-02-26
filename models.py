import datetime
from peewee import *

DATABASE = SqliteDatabase("users.sqlite")

class User(Model):
	name = CharField()
	phone = CharField()
	email = CharField()

	class Meta:
		database = DATABASE

def initialize():
	DATABASE.connect()
	DATABASE.create_tables([User], safe=True)
	DATABASE.close()