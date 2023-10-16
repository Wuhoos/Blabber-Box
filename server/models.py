from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates

from config import db

metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)

db = SQLAlchemy(metadata=metadata)

# Models go here!
class Profile(db.Model, SerializerMixin):
    __tablename__ = 'profile_table'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable = False)

    messages = db.relationship('Message', back_populates ='profile_object')

    conversation_proxy = association_proxy('messages', 'conversations_object')

    serialize_rules = ('-messages.profile_object',)

class Conversations(db.Model, SerializerMixin):
    __tablename__= 'conversation_table'

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String)
    user1_id = db.Column(db.Integer, db.ForeignKey("profile_table.id"), nullable = False)
    user2_id = db.Column(db.Integer, db.ForeignKey("profile_table.id"), nullable = False)

    messages = db.relationship('Message', back_populates='conversations_object')

    profile_proxy = association_proxy('messages', 'profile_object')

    serialize_rules = ('-messages.conversations_object',)

class Message(db.Model, SerializerMixin):
    __tablename__ = 'message_table'

    id = db.Column(db.Integer, primary_key= True)
    content = db.Column(db.String)

    conversation_id = db.Column(db.Integer, db.ForeignKey('conversation_table.id'), nullable=False)
    user_id =db.Column(db.Integer, db.ForeignKey('profile_table.id'), nullable=False)

    profile_object = db.relationship('Profile', back_populates='messages')
    conversations_object = db.relationship('Conversations', back_populates='messages')

    serialize_rules = ('-profile_object.messages', '-conversations_object.messages')