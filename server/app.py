from flask import request, Flask, make_response, jsonify, session
# from flask_restful import Resource, Api
from models import db, Profile, Conversations, Message
# from flask_socketio import SocketIO, send
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt 
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import MetaData

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False
# socketIo = SocketIO(app, cors_allowed_origins = '*')

bcrypt = Bcrypt(app)
migrate = Migrate(app, db)
db.init_app(app)

# @socketIo.on('message')
# def handle_message(msg):
#     send(msg, broadcast = True)
#     return None
@app.route('/')
def index():
    return '<h1>Project Server</h1>'

#Create user profile
@app.post('/profile')
def create_user():
    data = request.json
    password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    user = Profile(username = data.get('username'), password = password)
    db.session.add(user)
    db.session.commit()
    session['user_id'] = user.id
    return user.to_dict(), 201

#User login
@app.post('/login')
def user_login():
    data = request.json
    user = Profile.query.filter(Profile.username == data.get('username')).first()
    if user and bcrypt.check_password_hash(user.password, data.get('password')):
        session['user_id'] = user.id
        return user.to_dict(), 201
    else:
        return {'Error': 'Invalid username and/or password'}, 401

@app.get('/check_login')
def check_login():
    user = Profile.query.filter(Profile.id == session.get('user_id')).first()
    if user:
        return user.to_dict(), 200
    else:
        return {'Error': 'Not logged in.'}, 401

@app.delete('/logout')
def user_logout():
    session.pop('user_id')
    return {'Success': 'Logged out.'}, 200

@app.get('/<string:username>/conversations')
def get_user_conversations(username):
    user = Profile.query.filter(Profile.username == username).first()
    if user:
        convo_dict = [convo.to_dict(rules = ('-messages',)) for convo in user.conversation_proxy]
        user_dict = user.to_dict(rules = ('-messages','-username', '-password'))
        user_dict['conversations'] = convo_dict
        return make_response(convo_dict, 200)
    else:
        return {'Error': 'Error'}

@app.patch('/profile/<int:id>')
def update_profile(id):
    update_pf = db.session.get(Profile, id)
    data = request.json
    try:
        for key in data:
            setattr(update_pf, key, data[key])
            db.session.add(update_pf)
            db.session.commit()
            return make_response(jsonify(update_pf.to_dict()), 200)
    except Exception as e:
        return make_response(jsonify({"error":"Could not update profile. " + str(e)}), 404)

@app.delete('/profile/<int:id>')
def delete_profile(id):
    profile = db.session.get(Profile, id)
    if not profile:
        return make_response(jsonify({"error":"Profile does not exist"}), 404)
    db.session.delete(profile)
    db.session.commit()
    return make_response(jsonify({}), 200) 

# @app.get('/conversations/<int:id>')
# def get_user_convo(id):
#     convo = Profile.query.filter(Profile.id == id).first()
#     if not convo:
#         return make_response(jsonify({"error":"conversation does not exist"}), 404)
#     return make_response(jsonify(convo.to_dict()), 200)

# @app.post('/conversations')
# def post_conversations():
#     data = request.json
#     try:
#         new_convo = Conversations(message=data.get('message'), user1_id=data.get('user1_id'), user2_id=data.get('user2_id'))
#         db.session.add(new_convo)
#         db.session.commit()
#         return make_response(jsonify(new_convo.to_dict()), 200)
#     except:
#         return make_response(jsonify({"error":"Could not create conversation"}), 404)

@app.delete('/conversations/<int:id>')
def delete_conversation(id):
    convo = db.session.get(Conversations, id)
    if not convo:
        return make_response(jsonify({"error":"Conversation does not exist"}), 404)
    db.session.delete(convo)
    db.session.commit()
    return make_response(jsonify({}), 200)

if __name__ == '__main__':
    app.run(port = 5555, debug = True)
