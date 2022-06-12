from db import db
from typing import List

class UserModel(db.Model):

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(50), nullable=False)


    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    def __repr__(self):
        return (
            f"**User** "
            f"user_id: {self.user_id} "
            f"name: {self.name} "
            f"email: {self.email}"
            f"**User** "
        )
    
    def json(self):
        return {'name': self.name, 'email': self.email, 'phone': self.phone, 'address': self.address}

    @classmethod
    def find_by_name(cls, name) -> "UserModel":
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id) -> "UserModel":
        return cls.query.filter_by(user_id=_id).first()

    @classmethod
    def find_all(cls) -> List["UserModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()