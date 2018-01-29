def ask_question():
    question = 0
    while question != 'quit':
        question = input("What is your question? ")
        if question[-1] != '?':
            print("I'm sorry, I can only answer questions.")


m8 = ask_question()
print(m8)
