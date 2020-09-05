from flask_restful import Resource
from flask import request, current_app as app
from models import branch, notification
from flask_bcrypt import Bcrypt
from bson import json_util, ObjectId
import json
from auth import authentication_required


class ResgisterBranch(Resource):
    method_decorators = [authentication_required]

    def post(self):
        try:
            data = request.get_json()
            br = branch.Branch(name=data["name"]).save()
            return {"message": "Branch created successfully"}
        except Exception as err:
            print(err)
            return {"message": "Branch already exists"}


class GetAllBranches(Resource):
    def get(self):
        try:
            branches = branch.Branch.objects.values().all()
            serialized = json.loads(json_util.dumps(branches))
            return serialized
        except Exception as err:
            print(err)
            return {"message": "No branches available"}
