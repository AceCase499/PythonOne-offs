def maxminavg(userlist):
    averages = []
    for i in userlist:
        print("Largest Values:")
        print(max(i))
        print("Lowest Values:")
        print(min(i))

        thesum = 0
        for num in i:
            thesum += num
        theavg = thesum / 4
        averages.append(theavg)
        thesum = 0
    return averages


def main():
    scores = [(89, 77, 90, 88), (72, 88, 56, 91), (67, 73, 77, 80), (89, 7, 67, 77)]
    print(maxminavg(scores))
    print(max(maxminavg(scores)))


main()
