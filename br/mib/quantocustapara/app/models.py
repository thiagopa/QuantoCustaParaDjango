from mongoengine import *
from constants import A

class BaseModel :
    def article(self):
        if self.name.endswith(A) :
            return A
        else :
            return ""

class CloudTag(Document,BaseModel):
    
    name = StringField(max_length=50)
    size = StringField(max_length=10)

class Item(EmbeddedDocument):
    name = StringField(max_length=50)
    quantity = IntField()            
        
class ProductService(Document,BaseModel):
    
    name = StringField(max_length=50)
    items = ListField(EmbeddedDocumentField(Item))

