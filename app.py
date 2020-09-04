from flask import Flask, jsonify, request
from flask_restful import Api, Resource

from pymodm import connect


# Resource import
from resources import users

app = Flask(__name__)
api = Api(app)


connect("mongodb://localhost/uknow", alias="uknow")

api.add_resource(users.UserSignup, "/user/signup")
api.add_resource(users.LoginUser, "/user/login")
api.add_resource(users.UserMethod, "/user/meth/<string:id>")

# @app.route("/user", methods=["POST"])
# def createUser():
#     # get_json converts the json to python dictionary
#     users.UserSignup()


if __name__ == '__main__':
    app.run(port=5000, debug=True)
