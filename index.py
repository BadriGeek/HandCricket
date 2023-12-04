import random

userchoice=int(input("Enter 1 for Batting or Enter 2 for Bowling "))
if userchoice == 1:
    print("Its time to hit Six")
else :
    print ("Its time to break Stumps")

finalscore=[]
disp="No runs"
for innngs in range(1,3):
    score=[]
    for balls in range(1,7):
        Randnum = random.randrange(1,7)
        userinp = int(input("Enter a score : "))
        if userinp == Randnum :
            disp="You are out!!"
            score.append(0)
            print(disp)
            break
        elif userinp<=0 or userinp >=7:
            disp = "Invalid Number"
            score.append(0)
            print(disp)
            
        else :
            disp="You scored  "
            score.append(userinp)
            print(disp,userinp)
    print ("Your Total Score is ",sum(score))        
    finalscore.append(sum(score))
    score.clear()
    

print("Your Total Score is ",finalscore)
