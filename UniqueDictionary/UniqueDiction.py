def make_dictonary(file):
    word_dict = {}
    all_text = ""
    count = 0
    with open(file, "r") as file:
        for line in file:
            all_text += line
        file.close()
    txt_split = all_text.split(' ')
    for i in txt_split:
        count = 0
        for k in txt_split:
            if k == i:
                count += 1
        word_dict[i] = count
    return word_dict


def main():
    print(make_dictonary("text3.txt"))


main()
