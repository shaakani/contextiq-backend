from faker import Faker

fake = Faker()

def generate_synthetic_doc_summary(count=5):
    summaries = []
    for _ in range(count):
        summaries.append({
            "title": fake.sentence(nb_words=5),
            "summary": fake.paragraph(nb_sentences=3)
        })
    return summaries