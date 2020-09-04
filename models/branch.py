from pymodm import MongoModel, fields
from pymongo.write_concern import WriteConcern


class Branch(MongoModel):
    name = fields.CharField()
