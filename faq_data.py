def load_faqs():
    faqs = []

    with open("data/faqs.txt", "r", encoding="utf-8") as file:

        for line in file:
            line = line.strip()

            if not line:
                continue

            question, answer = line.split("|", 1)

            faq = {
                "question": question,
                "answer": answer
            }

            faqs.append(faq)

    return faqs

if __name__ == "__main__":
    faqs = load_faqs()

    for faq in faqs:
        print(faq)