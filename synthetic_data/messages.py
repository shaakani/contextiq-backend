from faker import Faker
from datetime import datetime
import random

fake = Faker()

def generate_synthetic_messages(num_messages=10):
    messages = []
    for _ in range(num_messages):
        messages.append({
            "user": fake.user_name(),
            "message": fake.sentence(nb_words=random.randint(5, 15)),
            "timestamp": fake.date_time_between(start_date='-7d', end_date='now').isoformat()
        })
    messages.sort(key=lambda x: x["timestamp"])
    return messages