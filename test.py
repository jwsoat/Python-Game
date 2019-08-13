def firsttime():
    firsttimeans = input("have you played before? ")
    if firsttimeans == "no":
        print("Gane 1 Simple maths  " 
              "Game 2 Guess the Number")
        start()
    else:
        start()

def start():
    import random
    game = 0
    while game == 0:
     game= int(input("Pick a game 1 - 2? "))
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
                start()
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
                    playagain = input("play again")
                    if playagain == "no":
                        start()
                    if playagain == "yes":
                        numberguess()

                if guess =="":
                    print("try again")
        numberguess()


firsttime() #keep at bottom



