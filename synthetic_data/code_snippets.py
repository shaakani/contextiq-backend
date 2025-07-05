# This endpoint will generate synthetic coding snippets and comments—mimicking
# a scenario where code is shared in a dev discussion or AI assistant interaction.

#It will generate synthetic code snippets with user names, programming languages, code blocks, and timestamps.



from faker import Faker
from datetime import datetime
import random

fake = Faker()

SNIPPETS = {
    "Python": ["for i in range(5):\n    print(i)", "def greet(name):\n    return f\"Hello, {name}!\""],
    "JavaScript": ["for (let i = 0; i < 5; i++) {\n  console.log(i);\n}"],
    "Go": ["for i := 0; i < 5; i++ {\n  fmt.Println(i)\n}"],
    "Java": ["for (int i = 0; i < 5; i++) {\n  System.out.println(i);\n}"],
    "Ruby": ["5.times do |i|\n  puts i\nend"]
}

def generate_synthetic_code_snippets(count=5):
    snippets = []
    for _ in range(count):
        lang = random.choice(list(SNIPPETS.keys()))
        snippets.append({
            "user": fake.user_name(),
            "language": lang,
            "code": random.choice(SNIPPETS[lang]),
            "created_at": fake.date_time_between(start_date='-7d', end_date='now').isoformat()
        })
    return snippets