'''opens a specified file and displays all the unique words found in file'''


def main():
    input_name = input("Enter the name of the file")
    inputFile = open(input_name, 'r')
    text = inputFile.read()
    words = text.split()

    unique_words = set(words)

    print("There are the unique words in the text: ")
    for word in unique_words:
        print(word)

    inputFile.close()


main()
