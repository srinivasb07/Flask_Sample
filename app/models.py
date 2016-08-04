from app import db
from marshmallow_jsonapi import Schema, fields
from marshmallow import validate

class CRUD_MixIn():

    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()

    def update(self):
        self.modification_time = db.func.current_timestamp()
        return db.session.commit()

    def delete(self, resource):
        db.session.delete(resource)
        return db.session.commit()

class Users(db.Model, CRUD_MixIn):
    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(250), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    name = db.Column(db.String(250), nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    creation_time = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    modification_time = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self,  email,  password,  name,  active):

        self.email = email
        self.password = password
        self.name = name
        self.active = active

class UsersSchema(Schema):

    not_blank = validate.Length(min=1, error='Field cannot be blank')
    # add validate=not_blank in required fields
    id = fields.Integer(dump_only=True)

    email = fields.Email(validate=not_blank)
    password = fields.String(validate=not_blank)
    name = fields.String(validate=not_blank)
    active = fields.Boolean()
    creation_time = fields.DateTime(dump_only=True)
    modification_time = fields.DateTime(dump_only=True)
    role = fields.String(validate=not_blank)

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/User/"
        else:
            self_link = "/User/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'user'