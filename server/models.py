from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates



metadata = MetaData(
    naming_convention = {
        "ix": 'ix_%(column_0_label)s',
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
    }
)

db = SQLAlchemy(metadata=metadata)

# Models go here!


class Post(db.Model, SerializerMixin):
    __tablename__= 'post_table'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)

    profile_id = db.Column(db.Integer, db.ForeignKey('profile_table.id'), nullable=False)

    comments = db.relationship('Comment', back_populates='post_object')
    profile_object = db.relationship('Profile', back_populates='posts')

    profile_proxy = association_proxy('comments', 'profile_object')


   
    serialize_rules = ('-comments.post_object', '-profile_object.posts')



class Comment(db.Model, SerializerMixin):
    __tablename__ = 'comment_table'

    id = db.Column(db.Integer, primary_key= True)
    text = db.Column(db.String)

    post_id = db.Column(db.Integer, db.ForeignKey('post_table.id'), nullable=False)
    profile_id =db.Column(db.Integer, db.ForeignKey('profile_table.id'), nullable=False)

    profile_object = db.relationship('Profile', back_populates='comments')
    post_object = db.relationship('Post', back_populates='comments')

   
    serialize_rules = ('-profile_object.comments', '-post_object.comments')


class Profile(db.Model, SerializerMixin):
    __tablename__ = 'profile_table'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable = False)
    posts = db.relationship('Post', back_populates='profile_object')
    comments = db.relationship('Comment', back_populates='profile_object')

    post_proxy = association_proxy('comments', 'post_object')

    serialize_rules = ('-comments.profile_object', '-posts.profile_object',)



