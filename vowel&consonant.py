def vowel_counter(string, vowelL):
    count = 0
    for ch in string:
        if ch in vowelL:
            count += 1
    return count

#  def consonant_counter(string):


def main():
    vowels = 0
    consonants = 0
    vowelL = 'aeiou'
    string = input("Enter a string: ")

    vowels = vowel_counter(string, vowelL)
    #  consonants = consonant_counter(string, vowelL)

    print("The string you entered includes, ", vowels, " vowels and ", consonants, " consonants.")


main()
