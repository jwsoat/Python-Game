def gameselector():
    import random
    import time
    game = 0
    while game == 0:
     game= int(input("Pick a game 1 - 3? "))
    if game == 1:
        while game == 1:
            print("Game 1 Selected")
            print("Maths Calc rounding to 2dp")
            num1 = float(input("Number 1  "))
            num2 = float(input("Number 2  "))
            numansplus = num1 + num2
            numanssub = num1 - num2
            numanstimes = num1 * num2
            numansdivide = num1 / num2
            round(numansplus, 2)
            round(numanssub, 2)
            round(numanstimes, 2)
            plusround = round(numansdivide, 2)
            subround = round(numanssub, 2)
            roundtimes = round(numanstimes, 2)
            divideround = round(numansdivide, 2)
            print ("{} plus {} equals {}".format(num1,num2,plusround))
            print ("{} minus {} equals {}".format(num1,num2,subround))
            print ("{} times {} equals {}".format(num1,num2,roundtimes))
            print ("{} divide {} equals {}".format(num1,num2,divideround))
            playagain = input("play again")
            if playagain == "no":
                gameselector()
            #else:
                #continue
    while game == 2:
        print ("Gane 2 Selected")
        print ("Number guessing game")
        def numberguess():
            number = random.randint(1,100)
            print (number)
            guesses = 0
            print ("Guess number between 1 and 100")
            guesses +=1
            while guesses <10:
                guess = int(input("Your guess"))
                guesses +=1
                if guess < number:
                    print ("try again")

                if guess > number:
                    print ("try again")


                if guess == number:

                    print ("You Won")
                    print ("it took {} number of guesses".format(guesses))
                    playagain()

                if guess =="":
                    print("try again")
        numberguess()
    while game == 3:
        dicerollmin = 1
        dicerollmax = 6
        rollagain = "yes"
        while rollagain == "yes" or rollagain == "y":
            print("rolling dice")
            time.sleep(1)
            print("the values are")
            print(random.randint(dicerollmin,dicerollmax))
            print(random.randint(dicerollmin,dicerollmax))
            rollagain = input("roll again?")
            if rollagain == "no":
                gameselector()
    def playagain():
        playagain = input("play again")
        if playagain == "no":
            gameselector()




def firsttime():
    firsttimeans = input("have you played before? ")
    if firsttimeans == "no":
        print("Gane 1 Simple maths  ")
        print("Game 2 Guess the Number  ")
        print("Game 3 Dice Roll")
        gameselector()
    else:
        gameselector()




firsttime() #keep at bottom



