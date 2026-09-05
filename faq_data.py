def load_faqs():
    faqs = []

    with open("data/faqs.txt", "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            question, answer = line.split("|", 1)

            print("Question:", question)
            print("Answer:", answer)

    return faqs


load_faqs()