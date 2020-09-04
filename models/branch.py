from pymodm import MongoModel, fields
from pymongo.write_concern import WriteConcern


class Branch(MongoModel):
    name = fields.CharField()

    class Meta:
        connection_alias = "uknow"
        write_concern = WriteConcern(j=True)
