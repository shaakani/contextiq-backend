from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

LABELS = ["bug", "enhancement", "question", "documentation", "help wanted"]

def generate_synthetic_issues(num_issues=5):
    """
    Generates a list of fake GitHub-like issues.
    Each issue contains a title, body, user, labels, and creation timestamp.
    """
    issues = []
    for _ in range(num_issues):
        issue = {
            "title": fake.sentence(nb_words=6),
            "body": fake.paragraph(nb_sentences=3),
            "user": fake.user_name(),
            "labels": random.sample(LABELS, k=random.randint(1, 3)),
            "created_at": fake.date_time_between(start_date="-30d", end_date="now").isoformat()
        }
        issues.append(issue)
    return issues
