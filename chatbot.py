from tfidf_model import find_best_answer


print("========================================")
print("          AI FAQ ASSISTANT")
print("========================================")
print("Welcome to the AI FAQ Assistant!")
print("I can answer questions from the FAQ knowledge base.")
print()
print("You can ask questions about:")
print("- Admission")
print("- Admission requirements")
print("- Required documents")
print("- Admission status")
print("- Fees")
print("- College contact")
print("- College location")
print("- Courses")
print()
print("Type 'exit' to end the conversation.")
print("========================================")
print()


while True:

    question = input("You: ").strip()


    if question.lower() == "exit":

        print("Bot: Goodbye!")

        break


    if not question.strip():

        print("Bot: Please enter a question.")

        continue


    if question.lower() in ["hello", "hi", "hey"]:

        print("Bot: Hello! How can I help you?")

        continue


    answer = find_best_answer(question)

    print("Bot:", answer)