import datetime
import random

start_time = datetime.datetime.now()

Allcorrect =  False

while Allcorrect == False:
    question1 = input("What is 2 + 2: ")
    if question1 == "4":
        question2 = input("What is 2 x 3: ")
        if question2 == "6":
            question3 = input("What is 6 + 9: ")
            if question3 == "15":
                question4 = input("What is 12 x 5: ")
                if question4 == "60":
                    question5 = input("What is 11 x 11: ")
                    if question5 == "121":
                        Allcorrect =  True


time_taken = datetime.datetime.now()-start_time
print(time_taken)
