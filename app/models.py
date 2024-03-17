from . import db
from werkzeug.security import generate_password_hash



class Property(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'propertydata'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    bedrooms = db.Column(db.Integer)
    location = db.Column(db.String(80))
    price = db.Column(db.Integer)
    type = db.Column(db.String(10))
    description = db.Column(db.String(255))



    def __init__(self,id,title,bedrooms,location,price,type,description):
        self.id = id
        self.title = title
        self.bedrooms = bedrooms
        self.location = location
        self.price = price
        self.type = type
        self.description = description


    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support
