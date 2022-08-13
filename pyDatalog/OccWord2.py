from pyDatalog import pyDatalog
pyDatalog.create_terms('X, Y, Z')
# needed to get started with using pyDatalog


def punctuation_list():
    import string
    punc_list = []
    for g in string.punctuation:
        punc_list += g
    # return a list of all punctuation marks
    return punc_list


def cleanMessage(Message):
    punc_list = punctuation_list()
    cleanText = ""
    splitText = []
    for a in Message:
        if a not in punc_list:
            # if the current instance of a is a special character, do not put it in cleanText
            cleanText += a

    splitText = cleanText.split()
    # remove all special characters from the input string that might throw off the results
    # for example, "cat," and "cat" may register as two unique words
    # only letters and numbers will remain
    # lastly, split the string into lists of strings every time a space is found
    return splitText


def FreqWord(Message):
    # Message is a LIST
    mostFreq = ""
    # holds the word that occurs most often (so far)
    TopOccurs = 0
    # holds the number of times the word that occurs most often occurs
    TempOccurs = 0
    # holds the number of times the current word occurs
    for a in Message:
        for b in Message:
            if b == a:
                TempOccurs += 1
                # every time the word that is being looked at occurs in the list, add 1 to TempOccurs
        if TempOccurs >= TopOccurs:
            mostFreq = a
            TopOccurs = TempOccurs
            # if the current word occurs more times than the word that occurred most often so far,
            # the current word becomes the word that occurs most often
        TempOccurs = 0
        # the programs begins again, looking at the next word in the list
    print("'" + mostFreq + "' occurs " + str(TopOccurs) + " times.")
    # print the most frequent word and how many times it appears, but only return the word
    return mostFreq


# INPUT EXAMPLE --> hor__se c(at rat c.at ho*rse c'at r/at
print((X == input("Enter a message >")) & (Y == cleanMessage(X.v())) & (Z == FreqWord(Y.v())))
# X is the name of the column that holds the input as a row
# Y is the name of the column that holds the input without special characters as a row
# Z is the name of the column that holds a word from the input that occurs most often
