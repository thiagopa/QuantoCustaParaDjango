from mongoengine import *
from settings import DBNAME

connect(DBNAME)

class CloudTag(Document):
    name = StringField(max_length=50)
    size = StringField(max_length=10)
