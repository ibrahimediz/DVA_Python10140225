from datetime import datetime
from app import db,ma
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    def __repr__(self):
        return f"User({self.id}, {self.username})"

class UserSchema(ma.Schema):
    class Meta:
        model = User
        fields = ("id", "username")

user_schema = UserSchema()
users_schema = UserSchema(many=True)


class Kitap(db.Model):
    kitap_id = db.Column(db.Integer, primary_key=True)
    kitap_adi = db.Column(db.String(100), nullable=False)
    yazar = db.Column(db.String(100), nullable=False)
    isbn = db.Column(db.String(100), nullable=False)
    olusturma_tarihi = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    yayim_tarihi = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"Kitap({self.kitap_id}, {self.kitap_adi}, {self.yazar}, {self.isbn}, {self.olusturma_tarihi}, {self.yayim_tarihi})"
    

class KitapSchema(ma.Schema):
    class Meta:
        fields = ("kitap_id", "kitap_adi", "yazar", "isbn", "olusturma_tarihi", "yayim_tarihi")

kitap_schema = KitapSchema()
kitapler_schema = KitapSchema(many=True)
