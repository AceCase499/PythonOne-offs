def punctuation_list():
    import string

    punc_list = []
    for g in string.punctuation:
        punc_list += g
    return punc_list


def checkFile(user_file):
    try:
        with open(user_file, "r") as user_file:
            user_file.close()
    except FileNotFoundError:
        return False
    else:
        return True


def readFile(user_file):
    all_text = ""
    punc_list = punctuation_list()
    noPuncText = ""

    with open(user_file, "r") as user_file:
        for line in user_file:
            all_text += line
        user_file.close()

    for a in all_text:
        if a == "-":
            noPuncText += " "
        if a not in punc_list:
            noPuncText += a.lower()
    wordList = noPuncText.split()
    print("\n>>Your file has been processed successfully. Now loading Main Menu...")
    print(wordList)
    return wordList


def createDictionary(wordList):
    word_dict = {}
    for i in wordList:
        count = 0
        for k in wordList:
            if k == i:
                count += 1
        word_dict[i] = count
    print("\n>>A new word dictionary has been created out of the entered file!")
    return word_dict


def sortDictionaryAlphabetically(word_dict):
    wordList = sorted(word_dict.items())
    alpha_dict = {}
    for k, v in wordList:
        alpha_dict[k] = v
    return alpha_dict


def topWordCounts(word_dict):
    print("\nDisplay the word dictionary in order of word count")
    print("%-15s |     %s" % ("Word", "Count"))
    print("----------------+----------")
    valList = word_dict.values()
    length = len(word_dict)
    for i in range(0, length):
        for k, v in word_dict.items():
            if v == max(valList):
                print("%-15s |     %s" % (k, v))
                valList.remove(max(valList))
                break


def displayMenu():
    print("\t\t\t\t\t--MENU--\n"
          "(1) Search a word in the book dictionary and find how many times the word occurred\n"
          "(2) Show top 10 occurring words in the book\n"
          "(3) Show the least occurring 10 words in the book\n"
          "(4) Show the alphabetically first 10 words and their counts\n"
          "(5) Show the alphabetically last 10 words and their counts\n"
          "(6) Sort the dictionary alphabetically, write it to a file and quit the program")


def OneWordFreq(words_dict, UserWord):
    return words_dict.get(UserWord)


def Top10Alpha(alpha_dict):
    print("\nChoice 4: Show the alphabetically first 10 words and their counts.")
    print("%-15s |     %s" % ("Word", "Count"))
    print("----------------+----------")
    for i in range(1, 11):
        print("%-15s |     %s" % (list(alpha_dict.keys())[i], list(alpha_dict.values())[i]))


def Bottom10Alpha(alpha_dict):
    print("\nChoice 5: Show the alphabetically last 10 words and their counts.")
    print("%-15s |     %s" % ("Word", "Count"))
    print("----------------+----------")
    for i in range(-1, -11, -1):
        print("%-15s |     %s" % (list(alpha_dict.keys())[i], list(alpha_dict.values())[i]))


def TopTenFreq(word_dict):
    valList = sorted(word_dict.values())
    print("\nChoice 2: Show top 10 occurring words in the book.")
    print("%-15s |     %s" % ("Word", "Count"))
    print("----------------+----------")
    for i in range(1, 11):
        for k, v in word_dict.items():
            if v == max(valList):
                print("%-15s |     %s" % (k, v))
                valList.remove(max(valList))
                break


def BottomTenFreq(word_dict):
    valList = list(word_dict.values())
    print("\nChoice 3: Show the least occurring 10 words in the book.")
    print("%-15s |     %s" % ("Word", "Count"))
    print("----------------+----------")
    counter = 1
    for k, v in word_dict.items():
        if counter == 11:
            break
        if v == min(valList):
            print("%-15s |     %s" % (k, v))
            valList.remove(min(valList))
            counter += 1


def writeDictToFile(alpha_dict):
    print("\nChoice 6: Sort the dictionary alphabetically, write it to a file and quit the program.")
    with open("ionDictionary.txt", "w") as NewFile:
        NewFile.write("WORD_DICTIONARY.TXT\n")
        NewFile.write("%-15s |     %s" % ("Word", "Count"))
        NewFile.write("\n")
        NewFile.write("----------------+----------\n")
        for k in alpha_dict:
            NewFile.write("%-15s |     %s" % (k, alpha_dict[k]))
            NewFile.write("\n")
        NewFile.close()
    print(">>Dictionary written to file successfully.")


def main():
    Done = False
    print("Welcome to Book Dictionary Maker!")
    user_file = input("Enter a file you want to use (Remember to include the extension): ")

    while not Done:
        if checkFile(user_file):
            wordList = readFile(user_file)
            word_dict = createDictionary(wordList)
            alpha_dict = sortDictionaryAlphabetically(word_dict)
            inputList = ['1', '2', '3', '4', '5', '6']
            displayMenu()
            response = input("Please enter the number of the function you want to use: ")

            if response == '1':
                print("\nChoice 1: Search a word in the book dictionary and find how many times the word occurred.")
                UserWord = input("Enter a word: ")
                print("%-15s |     %s" % ("Word", "Count"))
                print("----------------+----------")
                print("%-15s |     %s" % (UserWord, OneWordFreq(word_dict, UserWord)))
            elif response == '2':
                TopTenFreq(word_dict)
            elif response == '3':
                BottomTenFreq(word_dict)
            elif response == '4':
                print(Top10Alpha(alpha_dict))
            elif response == '5':
                print(Bottom10Alpha(alpha_dict))
            elif response == '6':
                writeDictToFile(alpha_dict)
                Done = True
            elif response not in inputList:
                print("XX Input Error! Your input must be a number from the list above. Try again.")
        else:
            print("XX ERROR! File  ", user_file, "  either does not exist or was spelled incorrectly. Try again.")
            user_file = input("Enter a file you want to use (Remember to include the extension): ")
    print("★Thank you for using Dictionaries for your Books. Goodbye!★")


main()
