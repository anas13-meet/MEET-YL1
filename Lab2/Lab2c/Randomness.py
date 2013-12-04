import random

def flip(prob):
    if random.random() < prob:
        return "H"
    else:
        return "T"

def flipNtimes(n):
    coin_flips = []
    for x in xrange(n):
        coin_flips.append(flip(0.5))
    return coin_flips

if __name__ == "__main__":
    #to flip a fair coin every time the user presses n:
    c = raw_input("Type n to flip a coin: ")
    while c == "n":
        print flip(0.5)
        c = raw_input("Type n to flip a coin: ")

    # to first ask the user what the probability is
    prob = float(raw_input("What should the probability of heads be? "))
    c = raw_input("Type n to flip a coin: ")
    while c == "n":
        print flip(prob)
        c = raw_input("Type n to flip a coin: ")

    # to flip N times and return as an array
    n = int(raw_input("How many times should I flip the coin? "))
    print flipNtimes(n)