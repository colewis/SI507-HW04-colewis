import random

def ask_question():
<<<<<<< HEAD
    question = 0
    while question != 'quit':
        question = input("What is your question? ")
        if question[-1] != '?':
            print("I'm sorry, I can only answer questions.")
=======
    question = input("What is your question?")
    answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good",  "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]
    answer = random.choice(answers)
    return answer

    

print(ask_question())

>>>>>>> origin/add_questions


