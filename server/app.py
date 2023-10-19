from flask import request, Flask, make_response, jsonify, session
from models import db, Profile, Comment, Post
# from flask_cors import CORS
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt 


app = Flask(__name__)

# CORS(app, supports_credentials=True,  resources='*')

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

# Check login session
@app.get('/check_login')
def check_login():
    user = Profile.query.filter(Profile.id == session.get('user_id')).first()
    if user:
        return user.to_dict(), 200
    else:
        return {'Error': 'Not logged in.'}, 401

# User logout
@app.delete('/logout')
def user_logout():
    session.pop('user_id')
    return {'Success': 'Logged out.'}, 200




# Get all posts
@app.get('/posts')
def main_feed():
    posts = Post.query.all()
    data = [post.to_dict() for post in posts]
    return make_response(jsonify(data), 200)




# Get user individual post
@app.get('/<string:username>/post/<int:id>')
def get_post_by_id(username, id):
    user = Profile.query.filter(Profile.username == username).first()
    post = Post.query.filter(Post.id == id).first()
    if not user:
        return make_response(jsonify({'Error': 'Invalid user.'}))
    if not post:
        return make_response(jsonify({'Error': 'Post not found.'}))
    return make_response(jsonify(post.to_dict()), 200)




# Get user post list
@app.get('/<string:username>/post')
def get_user_posts(username):
    user = Profile.query.filter(Profile.username == username).first()
    if user:
        post_dict = [post.to_dict() for post in user.posts]
        user_dict = user.to_dict()
        user_dict['posts'] = post_dict
        return make_response(post_dict, 200)
    else:
        return {'Error': 'Error'}



# Make a new post
@app.post('/<string:username>/posts')
def make_post(username):
    data = request.json
    user = Profile.query.filter(Profile.username == username).first()
    if user:
        try:
            new_post = Post(content=data.get('content'), profile_id= data.get('profile_id'), title = data.get('title') )
            db.session.add(new_post)
            db.session.commit()
            return make_response(jsonify(new_post.to_dict()), 200)
        except Exception as e:
            print(e)
            return make_response(jsonify({"error":"Could not create post"}), 404)
    return make_response(jsonify({'error': 'cannot post'}))





# Update user post
@app.patch('/<string:username>/post/<int:id>')
def update_profile(username, id):
    post = Post.query.filter(Post.id).first()
    user = Profile.query.filter(Profile.username == username).first()
    data = request.json
    if not user:
        return make_response(jsonify({'Error': 'Wrong user.'}))
    try:
        for key in data:
            setattr(post, key, data[key])
            db.session.add(post)
            db.session.commit()
            return make_response(jsonify(post.to_dict()), 200)
    except Exception as e:
        return make_response(jsonify({"error":"Could not update post. " + str(e)}), 404)




# Delete user post
@app.delete('/<string:username>/post/<int:id>')
def delete_post(username, id):
    post = db.session.get(Post, id)
    user = Profile.query.filter(Profile.username == username).first()
    if not post and user:
        return make_response(jsonify({"error": "User or post does not exist"}), 404)
    db.session.delete(post)
    db.session.commit()
    return make_response(jsonify({}), 200)




# Delete user profile
@app.delete('/profile/<int:id>')
def delete_profile(id):
    profile = db.session.get(Profile, id)
    if not profile:
        return make_response(jsonify({"error":"Profile does not exist"}), 404)
    db.session.delete(profile)
    db.session.commit()
    return make_response(jsonify({}), 200) 




# Post new comment
@app.post('/<string:username>/post/<int:id>')
def add_comment(username, id):
    data = request.json
    user = Profile.query.filter(Profile.username == username).first()
    post = Post.query.filter(Post.id == id).first()
    if user and post:
        try:
            new_comment = Comment(text=data.get('text'), post_id=data.get('post_id'), profile_id=data.get('profile_id'))
            db.session.add(new_comment)
            db.session.commit()
            return make_response(jsonify(new_comment.to_dict()), 200)
        except Exception as e:
            print(e)
            return make_response(jsonify({"error":"Could not create comment"}), 404)
    return make_response(jsonify({'error': 'Information invalid'}))




# Delete comment
@app.delete('/<string:username>/<string:title>/comments/<int:id>')
def delete_comment(username, id, title):
    comment = db.session.get(Comment, id)
    title = Post.query.filter(Post.title == title).first()
    username = Profile.query.filter(Profile.username == username).first()
    if not username:
        return make_response(jsonify({'error':'cannot find username'}))
    if not title:
        return make_response(jsonify({"error": "User or Comment does not exist"}), 404)
    if not comment:
        return make_response(jsonify({"error": "Comment does not exist"}), 404)
    db.session.delete(comment)
    db.session.commit()
    return make_response(jsonify({}), 200)


if __name__ == '__main__':
    app.run(port = 5545, debug = True)


