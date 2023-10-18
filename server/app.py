from flask import request, Flask, make_response, jsonify, session
from models import db, Profile, Comment, Post
from flask_cors import CORS
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt 


app = Flask(__name__)

CORS(app, supports_credentials=True)

app.config['SECRET_KEY'] = 'mysecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False


bcrypt = Bcrypt(app)
migrate = Migrate(app, db)
db.init_app(app)


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

@app.get('/<string:username>/posts')
def get_user_posts(username):
    user = Profile.query.filter(Profile.username == username).first()
    if user:
        post_dict = [post.to_dict() for post in user.posts]
        user_dict = user.to_dict()
        user_dict['posts'] = post_dict
        return make_response(post_dict, 200)
    else:
        return {'Error': 'Error'}

# @app.patch('/profile/<int:id>')
# def update_profile(id):
#     update_pf = db.session.get(Profile, id)
#     data = request.json
#     try:
#         for key in data:
#             setattr(update_pf, key, data[key])
#             db.session.add(update_pf)
#             db.session.commit()
#             return make_response(jsonify(update_pf.to_dict()), 200)
#     except Exception as e:
#         return make_response(jsonify({"error":"Could not update profile. " + str(e)}), 404)

@app.delete('/profile/<int:id>')
def delete_profile(id):
    profile = db.session.get(Profile, id)
    if not profile:
        return make_response(jsonify({"error":"Profile does not exist"}), 404)
    db.session.delete(profile)
    db.session.commit()
    return make_response(jsonify({}), 200) 



@app.post('/<string:username>/posts')
def make_post(username):
    data = request.json
    user = Profile.query.filter(Profile.username == username).first()
    if user:
        try:
            new_post = Post(content=data.get('content'), profile_id= data.get('profile_id') )
            db.session.add(new_post)
            db.session.commit()
            return make_response(jsonify(new_post.to_dict()), 200)
        except:
            return make_response(jsonify({"error":"Could not create post"}), 404)
    return make_response(jsonify({'error': 'cannot post'}))

@app.delete('/posts/<int:id>')
def delete_post(id):
    comment = db.session.get(Post, id)
    if not comment:
        return make_response(jsonify({"error": "Post does not exist"}), 404)
    db.session.delete(comment)
    db.session.commit()
    return make_response(jsonify({}), 200)

if __name__ == '__main__':
    app.run(port = 5545, debug = True)
