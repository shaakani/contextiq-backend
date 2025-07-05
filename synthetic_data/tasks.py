from faker import Faker
from datetime import datetime
import random

fake = Faker()

def generate_synthetic_tasks(num_tasks=5):
    statuses = ['todo', 'in progress', 'done']
    priorities = ['low', 'medium', 'high']
    tasks = []

    for _ in range(num_tasks):
        tasks.append({
            "title": fake.sentence(nb_words=4),
            "description": fake.paragraph(nb_sentences=2),
            "status": random.choice(statuses),
            "priority": random.choice(priorities),
            "assignee": fake.user_name(),
            "created_at": fake.date_time_between(start_date='-14d', end_date='now').isoformat()
        })

    return tasks