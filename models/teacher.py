from pymodm import MongoModel, fields
from pymongo.write_concern import WriteConcern
from pymongo.operations import IndexModel


# class Teacher(MongoModel):
#     firstname = fields.CharField()
#     lastname = fields.CharField()
#     telephone = fields.CharField()
#     email = fields.EmailField(required=True)
#     courses = [fields.ReferenceField("Courses")]
