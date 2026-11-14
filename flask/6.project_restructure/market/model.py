from market import db

class Item(db.Model):
    id = db.Column(db.Integer(),primary_key =True)
    name = db.Column(db.String(length =50),nullable = False , unique = True)
    price = db.Column(db.Integer(),nullable= False )
    barcode= db.Column(db.String(length =12),nullable= False , unique = True)
    description = db.Column(db.String(length =1024),nullable = False,unique = True)
    def __repr__(self):
        return f"Item(id={self.id}, name='{self.name}', price={self.price}, barcode='{self.barcode}', description='{self.description}')"

