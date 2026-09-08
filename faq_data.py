from database import get_all_faqs


def load_faqs():
    rows = get_all_faqs()

    faqs = []

    for row in rows:
        faq = {
            "id": row[0],
            "question": row[1],
            "answer": row[2]
        }

        faqs.append(faq)

    return faqs


if __name__ == "__main__":
    faqs = load_faqs()

    for faq in faqs:
        print(faq)