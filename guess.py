from random import randint
"""Guess a number"""
global num
num = 1000
end = False

def menu():
    print("\n")
    print("Welcome to \'Guess a number\' game!")
    print("Choose an option:")
    print("1: Start game")
    print("2: Settings")
    print("0: Quit")
    res = int(input("> "))
    if res == 0:
        endgame()
    elif res == 1:
        start()
    elif res == 2:
        settings()
    else:
        print("Incorrect input, try again")

def endgame():
    print("See you!")
    global end
    end = True

def settings():
    print("Settings")
    print("1: Set maximum number")
    print("0: Back to menu")
    res = int(input("> "))
    if res == 0:
        return
    elif res == 1:
        setnum()

def setnum():
    n = int(input("Enter new number: "))
    if n <=0:
        print("Error! Number must be higher than 0")
    else:
        num = n

def start():
    n = randint(0, num)
    least = 0
    most = num
    g = None
    while g != n:
        if g != None:
            if g > n:
                print("Try lower")
                most = g
            else:
                print("Try higher")
                least = g
        print("The number is between " + str(least) + " and " + str(most))
        g = int(input("Guess: "))
    if g == n:
        print("Correct! The number is " + str(n))
while not end:
    menu()
