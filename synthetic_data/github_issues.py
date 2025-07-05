from faker import Faker
from datetime import datetime
import random

fake = Faker()

LABELS = ["bug", "enhancement", "question", "documentation", "help wanted"]

def generate_synthetic_github_issues(count=5):
    """
    Generates a list of fake GitHub-like issues.
    Each issue contains a title, body, user, labels, and creation timestamp.
    """
    issues = []
    for _ in range(count):
        issues.append({
            "title": fake.sentence(nb_words=4),
            "body": fake.paragraph(nb_sentences=3),
            "user": fake.user_name(),
            "labels": random.sample(LABELS, k=random.randint(1, 3)),
            "created_at": fake.date_time_between(start_date='-20d', end_date='now').isoformat()
        })
    return issues