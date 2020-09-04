from pymodm import MongoModel, fields
from pymongo.write_concern import WriteConcern
from pymongo.operations import IndexModel
from branch import Branch
from users import User


class Notification(MongoModel):
    description = fields.CharField()
    date = fields.DateTimeField(default=fields.datetime.datetime.now())
    user = fields.ReferenceField(User, on_delete=fields.ReferenceField.CASCADE)
    branch = fields.ReferenceField(
        Branch)
    img = fields.CharField()

    class Meta:
        connection_alias = "uknow"
        write_concern = WriteConcern(j=True)
