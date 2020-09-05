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
            # print(id)
            data = request.get_json()
            notify = nb.Notification(
                user=ObjectId(id), description=data["description"], img=data["img"], branch=ObjectId(data["branch_id"])).save()
            return {"message": "saved successfully"}, 201
        except Exception as err:
            print(err)
            return {"message": "Error doesn't exist"}, 401


class GetAllNotification(Resource):
    def get(self):
        try:
            data = nb.Notification.objects.values().all()
            serialized = json.loads(json_util.dumps(data))
            return serialized, 200
        except Exception as err:
            print(err)
            return {"message": "No data available"}
