import random


def roll_dice() :
    min = 1
    max = 6

    print "Roll the dice ..."
    print "The values are ..."
    print random.randint(min, max)
    print random.randint(min,max)

    sum = random.randint(min, max) + random.randint(min, max)

    return sum

def main():

    play_again = "y"

    while play_again == "y" or play_again == "Y":

        print
        print "****Game Starts****"

        print "--Player 1--"
        sum_p1 = roll_dice()
        print sum_p1

        print "--Player 2--"
        sum_p2 = roll_dice()
        print sum_p2

        if sum_p1 > sum_p2:
            print "Player 1 wins"
        elif sum_p1 == sum_p2:
            print "Tie"
        else :
            print "Player 2 wins"

        play_again = raw_input("Play again (y or n)? : ")


if __name__ == '__main__':
    main() #call main function