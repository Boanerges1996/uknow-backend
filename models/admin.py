from pymodm import MongoModel, fields
from pymongo.write_concern import WriteConcern
from pymongo.operations import IndexModel


class Admin(MongoModel):
    email = fields.EmailField(required=True)
    password = fields.CharField(required=True)
    pic = fields.CharField(
        default="https://img2.pngio.com/united-states-avatar-organization-information-png-512x512px-user-avatar-png-820_512.jpg")

    class Meta:
        connection_alias = "uknow"
        write_concern = WriteConcern(j=True)
        indexes = [
            IndexModel('email', unique=True, partialFilterExpression={
                '_cls': '%s.Admin' % (__name__,)})
        ]
