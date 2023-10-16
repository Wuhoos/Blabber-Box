from random import randint, choice as rc
from faker import Faker
from app import app
from models import db, Profile, Conversations, Message

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        profiles = []
        for n in range(10):
            profile = Profile(username = fake.username(), password = fake.country())
            profiles.append(profile)
        
        db.session.add_all(profiles)
        db.session.commit()

        messages = []

        for n in range(10):
            message = Message(content = fake.text())
            messages.ppend(message)

        db.session.add_all(messages)
        db.session.commit()

        conversations = []

        for n in range(10):
            conversation = Conversation(message = fake.text())
            conversations.append(conversations)

        db.session.add_all(conversations)
        db.session.commit()