import os
import random

class DadJokes:
    def __init__(self, prompt, answer): #constructor
        self.__prompt = prompt #this is a string
        self.__answer = answer #this is a string

    def PrintRandomJoke(self):
        print("Prompt: ", self.__prompt)
        print("Correct Answer: ", self.__answer)
    

def read_dadjokes():
    count = 0
    try: 
        with open (r"/Users/Elena/Downloads/DadJokes.txt") as f:
            for line in f:
                count += 1
                if count % 2 != 0: #odd numbers 
                    parts = line.strip("\n")
                    parts = parts.split(",")
                    promptlist.append(parts)
                else:
                    parts = line.strip("\n")
                    parts = parts.split(",")
                    answerlist.append(parts)
            # print (promptlist)
            # print (answerlist)

    except OSError:
        print ("Sorry could not find file")

def jokeselect():
    global promptlist, answerlist
    question = int(input("Pick a number from 0-9: "))
    print ("You have selected joke " + str(question))
    random_prompt = promptlist[question]
    random_answer = answerlist[question]
    print ("")
    print ("The joke is...")
    cleanprompt = random_prompt[0]
    cleananswer = random_answer[0]
    print (cleanprompt)
    print ("")
    reply = input("Enter a response: ")
    print ("")
    return cleanprompt, cleananswer 


#VARIABLES
promptlist = []
answerlist = []     

#CALLING FUNCTION 
read_dadjokes()
cleanprompt, cleananswer = jokeselect()

#CREATING OBJECT
object  = DadJokes(cleanprompt, cleananswer)

#CALLING METHOD
object.PrintRandomJoke()
