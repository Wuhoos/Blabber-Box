from random import randint, choice as rc
from faker import Faker
from app import app
from models import db, Profile, Conversations, Message
from random import randint, choice, choices

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        profiles = []

        for n in range(1):
            profile = Profile(username = fake.first_name(), password = '')
            profiles.append(profile)
        db.session.add_all(profiles)
        db.session.commit()

        conversations = []

        for n in range(10):
            conversation = Conversations(message = fake.text())
            conversations.append(conversation)

        db.session.add_all(conversations)
        db.session.commit()

        messages = []

        for n in range(10):
            message = Message(content = fake.text(), conversation_id = choice(conversations).id, user_id = choice(profiles).id)
            messages.append(message)

        db.session.add_all(messages)
        db.session.commit()

       