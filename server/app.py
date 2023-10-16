from flask import request, Flask
from flask_restful import Resource, Api
from config import app, db, api
from flask_socketio import SocketIO, send

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
socketIo = SocketIO(app, cors_allowed_origins = '*')

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

@socketIo.on('message')
def handle_message(msg):
    send(msg, broadcast = True)
    return None

@app.route('/')
def index():
    return '<h1>Project Server</h1>'


db = SQLAlchemy(metadata=metadata)
migrate = Migrate(app, db)
db.init_app(app)

if __name__ == '__main__':
    app.run(port = 5555, debug = True)
