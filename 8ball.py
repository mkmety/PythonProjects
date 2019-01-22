import time
import random

another = True

responses = ["As I see it, yes", "Ask again later", "Better not tell you now", "Cannot predict now",
             "Concentrate and ask again", "Don’t count on it", "It is certain", "It is decidedly so", "Most likely",
             "My reply is no", "My sources say no", "Outlook good", "Outlook not so good", "Reply hazy try again",
             "Signs point to yes", "Very doubtful", "Without a doubt", "Yes", "Yes, definitely", "You may rely on it"]
while another:
    question = input("Ask 8 Ball a Question: ")
    print("Thinking...")
    time.sleep(3)
    print(random.choice(responses))
    another_question = input("Would you like to ask another question? ")
    if another_question == "Yes":
        another = True
    elif another_question == "No":
        another = False
    else:
        print("Not a valid response")
        another = False
