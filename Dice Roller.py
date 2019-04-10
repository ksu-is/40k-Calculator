import random
cont=1
while cont==1:
    BS=int(input("Enter BS: "))
    NumDice=int(input("Enter Number of shot: "))
    rerolls= int(input("Any rerolls? [Yes=1] [No=0] "))
    count = 0
    hit = 0
    missed = 0
    hotdeath = 0
    rehit = 0
    Reroll_Results=[]
    Hit_Results=[]
    #Hit Results
    
    while count < NumDice:
        roll = random.randint(1,6)
        Hit_Results.append(roll)
        count +=1
        if roll >= BS:
            hit+=1
        else:
            missed+=1
    Hit_Results.sort()
    print("the results are: ",Hit_Results)
    print("# of hits: ",hit)
    print("# of Missed: ",missed)




    #Rerolls
    if missed >= 1:
        if rerolls == 1:
            ans=int(input("reroll 1's or all? [1's= 1] [All=2]"))
            if ans == 1:
                for reroll in Hit_Results:
                    if reroll == 1:
                        roll =random.randint(1,6)
                        Reroll_Results.append(roll)
                        if roll>= BS:
                            hit+=1
                            missed-=1
                        
                        
            

        
          
