from app import app
from models import db, Message

def seed_messages():
    with app.app_context():
        # Clear existing messages
        Message.query.delete()
        
        # Create sample messages
        messages = [
            Message(body="Hello world!", username="Liza"),
            Message(body="This is a great app!", username="Duane"),
            Message(body="Flask is awesome", username="Sarah"),
            Message(body="React and Flask work well together", username="Mike"),
            Message(body="Learning full-stack development", username="Alex")
        ]
        
        for message in messages:
            db.session.add(message)
        
        db.session.commit()
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_messages()