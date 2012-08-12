from mongoengine import *
from constants import A

class CloudTag(Document):
    
    name = StringField(max_length=50)
    size = StringField(max_length=10)

    def article(self):
        if self.name.endswith(A) :
            return A
        else :
            return ""

class Item(EmbeddedDocument):
    name = StringField(max_length=50)            
        
class ProductService(Document):
    
    name = StringField(max_length=50)
    items = ListField(EmbeddedDocumentField(Item))

