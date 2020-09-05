from flask_restful import Resource
from flask import request, current_app as app, jsonify
from models import notification as nb
from flask_bcrypt import Bcrypt
from bson import json_util, ObjectId
import json
from auth import authentication_required


class NotificationRegister(Resource):
    def post(self, id):
        try:
            print(id)
            data = request.get_json()
            use = nb.Us.objects.values().get({"_id": ObjectId(id)})
            bran = nb.Br.objects.values().get(
                {"_id": ObjectId(data["branch_id"])})
            notify = nb.Notification(
                user=use, description=data["description"], img=data["img"], branch=bran).save()
            return {"message": "saved successfully"}, 201
        except Exception as err:
            print(err)
            return {"message": "Error doesn't exist"}, 401
