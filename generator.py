"""
I used this to generate the intial text files. The files, though, have changed so this will no longer work.
"""
import random    
import sys
import json

BASE_LETTERS = ["s", "td", "n", "m", "r", "l", "shch", "kg", "fv", "pb"]

def letterToNumber(letter):
    r = -1
    if letter == "s":
        r = 0
    elif letter == "td":
        r = 1
    elif letter == "n":
        r = 2
    elif letter == "m":
        r = 3
    elif letter == "r":
        r = 4
    elif letter == "l":
        r = 5
    elif letter == "shch":
        r = 6
    elif letter == "kg":
        r = 7
    elif letter == "fv":
        r = 8
    elif letter == "pb":
        r = 9
    else:
        raise SystemExit("letter outside of range: {}".format(letter))
    return r

def NumberToLetter(numeral):
    r = ""
    if numeral == "0":
        r = "s"
    elif numeral == "1":
        r = "td"
    elif numeral == "2":
        r = "n"
    elif numeral == "3":
        r = "m"
    elif numeral == "4":
        r = "r"
    elif numeral == "5":
        r = "l"
    elif numeral == "6":
        r = "shch"
    elif numeral == "7":
        r = "kg"
    elif numeral == "8":
        r = "fv"
    elif numeral == "9":
        r = "pb"
    else:
        raise SystemExit("numeral outside of range: {}".format(numeral))
    return r

def generateDictionary():
    s = ""
    myList = []
    n1, n2, s1, s2 = "", "", "", ""
    for x in BASE_LETTERS:
        for y in BASE_LETTERS:
            n1 = str(letterToNumber(x))
            n2 = str(letterToNumber(y))
            s1 = x 
            s2 = y
            myList.append([n1, n2, s1, s2])
    f = open('dictionary.txt', 'w')
    json.dump(myList, f)
    f.close()

def generateUser(filename):
    s = ""
    myList = []
    n1, n2, s1, s2 = "", "", "", ""
    attempts, score = 0, 0
    for x in BASE_LETTERS:
        for y in BASE_LETTERS:
            n1 = str(letterToNumber(x))
            n2 = str(letterToNumber(y))
            s1 = x 
            s2 = y
            myList.append([n1, n2, s1, s2, attempts, score])
    f = open(filename, 'w')
    json.dump(myList, f)
    f.close()    

if __name__ == "__main__":
    #generateDictionary()
    generateUser('user03.txt')
