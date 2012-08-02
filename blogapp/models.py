from mongoengine import *
from quantocustaparadjango.settings import DBNAME


# Create your models here.
connect(DBNAME)

class Post(Document):
    title = StringField(max_length=120, required=True)
    content = StringField(max_length=500, required=True)
    last_update = DateTimeField(required=True)