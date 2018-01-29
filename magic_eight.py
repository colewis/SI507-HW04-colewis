import random

def ask_question():
    while True:
        question = input("What is your question? ")
        if question[-1] != '?':
            if question != 'quit':
                print("I'm sorry, I can only answer questions.")
            else:
                exit()
        else:
            answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good",  "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]
            answer = random.choice(answers)
            print(answer)


