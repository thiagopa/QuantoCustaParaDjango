from mongoengine import *
from settings import DBNAME
from constants import A

connect(DBNAME)

class CloudTag(Document):
    
    name = StringField(max_length=50)
    size = StringField(max_length=10)

    def article(self):
        if self.name.endswith(A) :
            return A
        else :
            return ""