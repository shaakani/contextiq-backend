# This endpoint will generate synthetic coding snippets and comments—mimicking
# a scenario where code is shared in a dev discussion or AI assistant interaction.

#It will generate synthetic code snippets with user names, programming languages, code blocks, and timestamps.

from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

LANGUAGES = ["Python", "JavaScript", "Java", "C++", "Go", "Ruby"]

SAMPLE_SNIPPETS = {
    "Python": [
        'def greet(name):\n    return f"Hello, {name}!"',
        'for i in range(5):\n    print(i)',
        'import requests\nresponse = requests.get("https://api.example.com")'
    ],
    "JavaScript": [
        'function greet(name) {\n  return `Hello, ${name}`;\n}',
        'for (let i = 0; i < 5; i++) {\n  console.log(i);\n}',
        'fetch("https://api.example.com").then(response => response.json())'
    ],
    "Java": [
        'public class HelloWorld {\n  public static void main(String[] args) {\n    System.out.println("Hello, World!");\n  }\n}',
        'for (int i = 0; i < 5; i++) {\n  System.out.println(i);\n}'
    ],
    "C++": [
        '#include <iostream>\nint main() {\n  std::cout << "Hello, World!";\n  return 0;\n}',
        'for (int i = 0; i < 5; i++) {\n  std::cout << i << std::endl;\n}'
    ],
    "Go": [
        'package main\nimport "fmt"\nfunc main() {\n  fmt.Println("Hello, World!")\n}',
        'for i := 0; i < 5; i++ {\n  fmt.Println(i)\n}'
    ],
    "Ruby": [
        'def greet(name)\n  "Hello, #{name}!"\nend',
        '5.times do |i|\n  puts i\nend'
    ]
}

def generate_code_snippets(num_snippets=5):
    """
    Generate a list of synthetic code snippets with metadata.
    """
    snippets = []

    for _ in range(num_snippets):
        language = random.choice(LANGUAGES)
        code = random.choice(SAMPLE_SNIPPETS[language])
        user = fake.user_name()
        timestamp = fake.date_time_between(start_date='-7d', end_date='now')

        snippets.append({
            "user": user,
            "language": language,
            "code": code,
            "created_at": timestamp.isoformat()
        })

    snippets.sort(key=lambda x: x["created_at"])
    return snippets
