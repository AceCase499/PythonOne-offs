from pyDatalog import pyDatalog
pyDatalog.create_terms('X, Y')
# needed to get started with using pyDatalog


def FreqWord(Sentence):
    Words = Sentence.split()
    thisWord = ""
    # holds the current word
    Frequency = 0
    # holds the number of times the word occurs
    Dictionary = ""
    for a in Words:
        for b in Words:
            thisWord = a
            if b not in Dictionary:
                if b == a:
                    Frequency += 1
                    # every time the word that is being looked at occurs in the list, add 1 to Frequency
        if thisWord not in Dictionary:
            Dictionary += thisWord + ": " + str(Frequency) + ", "
            # add the current word and its frequency to the Dictionary
        Frequency = 0
        # the programs begins again, looking at the next word in the list, reset Frequency value
    return Dictionary


# INPUT EXAMPLE --> horse cat rat cat horse cat rat
# result should be cat
print((X == input("Enter a message >")) & (Y == FreqWord(X.v())))
# X is the name of the column that holds the input as a row
# Y is the name of the column that holds the word that occurs most often as a row
