from pymodm import MongoModel, fields
from pymongo.write_concern import WriteConcern
from pymongo.operations import IndexModel


class Branch(MongoModel):
    name = fields.CharField()

    class Meta:
        connection_alias = "uknow"
        write_concern = WriteConcern(j=True)
        indexes = [
            IndexModel('name', unique=True, partialFilterExpression={
                '_cls': '%s.Branch' % (__name__,)})
        ]
