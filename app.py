from flask import Flask
import models
from resources.users import users_api

DEBUG = True

app = Flask(__name__)
app.register_blueprint(users_api)

@app.route('/')
def hello_word():
	return "Hello!" 

if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG)
