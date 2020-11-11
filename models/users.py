from pymodm import MongoModel, fields
from pymongo.write_concern import WriteConcern
from pymongo.operations import IndexModel


class User(MongoModel):
    email = fields.EmailField(required=True)
    # name = fields.CharField()
    firstname = fields.CharField()
    lastname = fields.CharField()
    password = fields.CharField()
    telephone = fields.CharField()
    branch = fields.ReferenceField("Branch")
    year = fields.CharField(default="One")
    isLocal = fields.BooleanField(default=True)
    first = fields.BooleanField(default=True)
    pic = fields.CharField(
        default="https://img2.pngio.com/united-states-avatar-organization-information-png-512x512px-user-avatar-png-820_512.jpg")
    admin = fields.ReferenceField("Admin")

    class Meta:
        connection_alias = "uknow"
        write_concern = WriteConcern(j=True)
        indexes = [
            IndexModel('email', unique=True, partialFilterExpression={
                '_cls': '%s.User' % (__name__,)})
        ]
