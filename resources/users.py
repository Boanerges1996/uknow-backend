from flask_restful import Resource
from flask import request, current_app as app, jsonify
from models import users
from flask_bcrypt import Bcrypt
from bson import json_util, ObjectId
import json
import jwt
from functools import wraps
from auth import authentication_required

bcrypt = Bcrypt()


class UserSignup(Resource):
    def post(self):

        try:
            data = request.get_json()
            hashedPassword = bcrypt.generate_password_hash(
                data["password"]).decode("utf-8")
            users.User(
                email=data["email"], firstname=data["firstname"], lastname=data["lastname"],
                telephone=data["telephone"], year=data["year"], isLocal=data["isLoacal"],
                password=hashedPassword).save()
            obj = users.User.objects.values().get({"email": data["email"]})

            sanitized = json.loads(json_util.dumps(obj))
            print(sanitized)
            return {**sanitized, "logged": True}, 201

        except Exception as err:
            print(err)
            return {"message": "Email already exists", "exist": True}, 200

        # print(data)
        # return {"message": "received"}, 201


class LoginUser(Resource):
    def post(self):
        try:
            data = request.get_json()
            log = users.User.objects.values().get({"email": data["email"]})
            verify = json.loads(json_util.dumps(log))
            if bcrypt.check_password_hash(verify["password"], data["password"]):
                auth = jwt.encode(
                    {"sub": data["email"]}, app.config.get("SECRET_KEY"), algorithm="HS256").decode("utf-8")

                return {**verify, "logged": True, "exist": True, "auth_token": auth}
            return {"message": "Invalid email or password", "error": True}, 401

        except Exception as err:
            print(err)
            return {"message": "Account doesnt exist", "exist": False}, 404


class UserMethod(Resource):
    method_decorators = [authentication_required]

    def get(self, id):
        try:
            search = users.User.objects.values().get({"_id": ObjectId(id)})
            info = json.loads(json_util.dumps(search))
            return info
        except Exception as err:
            print('Voila')
            print(err)
            return {"message": "This id doesnt exist"}, 404

    def put(self, id):
        try:
            data = request.get_json()
            update = users.User.objects.raw({"_id": ObjectId(id)}).update(
                {"$set": {**data}})
            search = users.User.objects.values().get({"_id": ObjectId(id)})
            info = json.loads(json_util.dumps(search))
            return info
        except Exception as err:
            print(err)
            return {"message": "This id doesnt exist, therefore you can't update"}, 404

    def delete(self, id):
        try:
            deletion = users.User.objects.raw({"_id": ObjectId(id)}).delete()
            return {"message": "Deletion succesful"}
        except Exception as err:
            print(err)
            return {"message": "This id doesnt exist, therefore you can't delete"}, 404
