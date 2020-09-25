from flask_restful import Resource
from flask import request, current_app as app, jsonify
from models import admin as ad
from flask_bcrypt import Bcrypt
from bson import json_util, ObjectId
import json
import jwt
from functools import wraps

bcrypt = Bcrypt()


class AdminSignUp(Resource):
    def post(self):
        try:
            data = request.get_json()
            hashedPassword = bcrypt.generate_password_hash(
                data["password"]).decode("utf-8")
            ad.Admin(email=data["email"], password=hashedPassword).save()
            obj = ad.Admin.objects.values().get({"email": data["email"]})
            serialized = json.loads(json_util.dumps(obj))
            return {**serialized, "logged": True}
        except Exception as err:
            print(err)
            return {"message": "Email already exists", "exist": True}, 201


class AdminLogin(Resource):
    def post(self):
        try:
            data = request.get_json()
            info = ad.Admin.objects.values.get({"email": data["email"]})
            verify = json.loads(json_util.dumps(info))
            if bcrypt.check_password_hash(info["password"], data["password"]):
                auth = jwt.encode(
                    {"sub": data["email"]}, app.config.get("SECRET_KEY"), algorithm="HS256").decode("utf-8")
                return {**info, "logged": True, "auth_token": auth}, 200
            return {"message": "Invalid password", "logged": False, "exist": True}, 401
        except Exception as err:
            print(err)
            return {"message": "Account doesnt exist", "exist": False, "logged": False}, 401
