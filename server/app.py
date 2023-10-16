from flask import request, Flask, make_response, jsonify
from flask_restful import Resource, Api
from models import db, *
from flask_socketio import SocketIO, send

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
socketIo = SocketIO(app, cors_allowed_origins = '*')

migrate = Migrate(app, db)
db.init_app(app)

@socketIo.on('message')
def handle_message(msg):
    send(msg, broadcast = True)
    return None

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

@app.route('/')
def index():
    # return render_template('home.html')
    return '<h1>Project Server</h1>'


@app.get('/<str:username>/<int:id>')
def get_user_conversations(username, id):
    convos_list = db.session.get(Profile, id, username)
    data = [convo.to_dict() for convo in convos_list]
    return make_response(jsonify(data), 200)

@app.patch('/<str:username>/<int:id>')
def update_profile(username, id):
    update_pf = db.session.get(Profile, id, username)
    data = request.json
    try:
        for key in data:
            setattr(update_pf, key, data[key])
            db.session.add(update_pf)
            db.session.commit()
            return make_response(jsonify(update_pf.to_dict()), 200)
    except Exception as e:
        return make_response(jsonify({"error":"Could not update profile. " + str(e)}), 404)

@app.delete('/<str:username>/<int:id>')
def delete_profile(username, id):
    profile = db.session.get(Profile, id, username)
    if not profile:
        return make_response(jsonify({"error":"Profile does not exist"}), 404)
    db.session.delete(profile)
    db.session.commit()
    return make_response(jsonify({}), 200) 

@app.get('/conversations/<int:id>')
def get_user_convo(id):
    convo = Profile.query.filter(Profile.id == id).first()
    if not convo:
        return make_response(jsonify({"error":"conversation does not exist"}), 404)
    return make_response(jsonify(convo.to_dict()), 200)

@app.post('/conversations')
def post_conversations():
    data = request.json
    try:
        new_convo = Conversations(message=data.get('message'), user1_id=data.get('user1_id'), user2_id=data.get('user2_id'))
        db.session.add(new_convo)
        db.session.commit()
        return make_response(jsonify(new_convo.to_dict()), 200)
    except:
        return make_response(jsonify({"error":"Could not create conversation"}), 404)

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
