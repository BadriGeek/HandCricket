import random

Randnum = random.randrange(1,7)
print(Randnum)
userinp = int(input("Enter a score : "))
score=[]
disp="No runs"


if (userinp == Randnum):
    score.append(disp)
    disp="You are out!!"
    print(disp)
    
    
else :
    disp="Your score is "
    score.append(userinp)
    print(disp,userinp)
    
print(score)    
    

