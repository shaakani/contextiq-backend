# To generate synthetic chat-like data using Faker

from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

def generate_synthetic_messages(num_messages=10):
    """
    Generates a list of synthetic chat messages with random users and timestamps.
    Each message is a dict with user, message text, and timestamp.
    """
    messages = []
    for _ in range(num_messages):
        user = fake.user_name()
        # Generate a random message about a tech topic
        message = fake.sentence(nb_words=random.randint(5, 15))
        # Generate a timestamp within the last 7 days
        timestamp = fake.date_time_between(start_date='-7d', end_date='now')
        
        messages.append({
            "user": user,
            "message": message,
            "timestamp": timestamp.isoformat()
        })
    # Sort messages by timestamp ascending
    messages.sort(key=lambda x: x["timestamp"])
    return messages
