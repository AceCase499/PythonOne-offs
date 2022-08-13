def main():
    word_counter = []
    with open("../newsText.txt", "r") as the_file:
        for line in the_file:
            the_split = line.split(" ")
            word_counter.append(len(the_split))
        the_file.close()
        the_sum = sum(word_counter)
        the_avg = the_sum / len(word_counter)
        print(the_avg)


main()
