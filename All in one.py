def start():
    yes =["yes", "y"]
    no =["no", "n"]
    game = 0
    while game == 0:
     game= int(input("Pick a game 1 - 20? "))
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
            if playagain is no:
                start()
            else:
                continue




start()

