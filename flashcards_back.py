import random    
import sys
import json
import datetime as dt
import os.path

#BASE_LETTERS = ["s", "t", "d", "n", "m", "r", "l", "sh", "ch", "k", "g", "f", "v", "p", "b"]

# ======================================================

class Question:
    def __init__(self, line):
        self.front = line[0]
        self.back1 = line[1]
        self.back2 = line[2]
        self.timesViewed = line[3]
        self.score = line[4]
        self.timeTaken = line[5]

    def printQuestion(self):
        print("front: {} | back1: {} | back2: {} | timesViewed: {} | score: {}".format(self.front, self.back1, self.back2, self.timesViewed, self.score))

    def writeQuestion(self):
        return [self.front, self.back1, self.back2, self.timesViewed, self.score, self.timeTaken]

# ======================================================

class Quiz:
    baseList = []
    score = 0
    filename = ""
    def __init__(self, filename):
        
        self.filename = filename
        f = open(filename, "r")
        myList = json.load(f)
        f.close()
        for myElem in myList:
            newQuestion = Question(myElem)
            self.baseList.append(newQuestion)

    def generateQuestion(self, index):
        if index < 0 or index > len(self.baseList):
            raise SystemError("index is out of range: {}".format(index))
        return self.baseList[index]

    def generateRandomQuestion(self):
        ranNum = int(random.randrange(0, len(self.baseList)))        
        return self.baseList[ranNum]
        
    def printQuestions(self):
        for e in self.baseList:
            e.printQuestion()
            #print("front: {} | back: {} | timesViewed: {} | score: {}".format(e.front, e.back, e.timesViewed, e.score))

    def writeQuestions(self):
        myList = []
        for e in self.baseList:
            writableForm = e.writeQuestion()
            myList.append(writableForm)
        f = open(self.filename, 'w')
        json.dump(myList, f)
        f.close()

# ======================================================

def main(filename, quizLength):
    if os.path.isfile(filename):
        pass
    else:
        raise SystemExit("Can't find this file: {}".format(filename))
    counter = 0
    quiz = Quiz(filename)
    #quiz.printQuestions()
    while counter < quizLength:
        n1=dt.datetime.now()
        question = quiz.generateRandomQuestion()
        question.timesViewed += 1
        #print("question: {}".format(question.front))
        userReply = input("(" + str(counter + 1) + "/" + str(quizLength) + ") " + question.back1 + question.back2 + " > ")
        n2=dt.datetime.now()
        c = n2 - n1
        numMicro = c.total_seconds()
        question.timeTaken = numMicro
        print("{} | Microseconds: {}".format(question.front, numMicro))
        if userReply.strip() == question.front:
            question.score += 1
            quiz.score += 1
            print("Correct!")
        else:
            print("Try again.")
        counter += 1
    print("------------------")
    print("Your score: {}%".format(int((quiz.score/quizLength)*100)))
    print("------------------")
    quiz.writeQuestions()

# ======================================================

if __name__ == "__main__":
    filename = "back.txt"
    if os.path.isfile(filename):
        pass
    else:
        raise SystemExit("Can't find this file: {}".format(filename))
    quizLength = 4
    main(filename, quizLength)

