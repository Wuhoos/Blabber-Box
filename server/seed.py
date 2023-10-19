from random import randint, choice as rc
from faker import Faker
from app import app
from models import db, Profile, Comment, Post
from random import randint, choice, choices

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")

        Profile.query.delete()
        Comment.query.delete()
        Post.query.delete()
        
        profiles = []

        for n in range(5):
            profile = Profile(username = fake.first_name(), password = fake.last_name())
            profiles.append(profile)
        db.session.add_all(profiles)
        db.session.commit()


        posts = []

        for n in range(5):
            content = Post(content = fake.text(), profile_id = choice(profiles).id, title = fake.country())
            posts.append(content)

        db.session.add_all(posts)
        db.session.commit()

        comments = []

        for n in range(5):
            text = Comment(text = fake.name(), profile_id = choice(profiles).id, post_id = choice(posts).id)
            comments.append(text)

        db.session.add_all(comments)
        db.session.commit()

    