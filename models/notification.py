from pymodm import MongoModel, fields
from pymongo.write_concern import WriteConcern
from pymongo.operations import IndexModel
from .branch import Branch as Br
from .users import User as Us


class Notification(MongoModel):
    description = fields.CharField()
    date = fields.DateTimeField(default=fields.datetime.datetime.now())
    user = fields.ReferenceField(Us, on_delete=fields.ReferenceField.CASCADE)
    branch = fields.ReferenceField(
        Br)
    img = fields.CharField()

    class Meta:
        connection_alias = "uknow"
        write_concern = WriteConcern(j=True)
