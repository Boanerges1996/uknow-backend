from pymodm import MongoModel, fields
from pymongo.write_concern import WriteConcern
from pymongo.operations import IndexModel
from users import User


class BuyAndSell(MongoModel):
    # Category name will be in soon
    buss_name = fields.CharField()
    description = fields.CharField()
    img = fields.CharField()
    date = fields.DateTimeField(default=fields.datetime.datetime.now())
    user = fields.ReferenceField(User, on_delete=fields.ReferenceField.CASCADE)

    class Meta:
        connection_alias = "uknow"
        write_concern = WriteConcern(j=True)
