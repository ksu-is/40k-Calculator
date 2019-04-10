import random
cont=1
while cont==1:
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print ("warhammer shooting phase dice roller")
    print ('')
    print ('')
    BS = int(input("enter attackers ballistic skill: "))
    print('')
    spc = int(input('are you using a special weapon? (no=0; gets hot=1; rending= 2; strength of x=3)(if more than one do not seperate with commas and write in order)'))
    print('')
    if BS< 6:
        hitRoll = BS
        gbs = 0
    else:
        gbs = 1
        hitTwo = 7-BS
    count = 0
    hit = 0
    missed = 0
    hotdeath = 0
    rehit = 0
    numDice = int(input("please enter amount of dice (1 die per model regardless of bs unless they have more shots): "))
    print('')
    if spc == 1 or spc == 12 or spc == 123 or spc == 13:
        atksave = int(input('what is the attackers save'))
        print('')
        atksavetwo = int(input('what is the attackers no pain save (if none write 0)'))
        print('')
    re = int(input('enter available rerolls if any: '))



    #hit roller
    roll_list=[]
    while count < numDice:
        roll = random.randint(1,6)
        count += 1
        if gbs == 0: 
            if hitRoll <= roll:
                hit += 1
            else:
                missed +=1
                if roll == 1:
                    if (spc == 1 or spc == 12 or spc == 123 or spc == 13):
                        roll = random.randint(1,6)
                        if roll >= atksave:
                            hotdeath += 0
                        else:
                            roll = random.randint(1,6)
                            if roll >= atksavetwo and atksavetwo != 0:
                                hotdeath += 0
                            else:
                                hotdeath += 1
        else:
            if 2 <= roll:
                hit += 1
            else:
                if roll == 1:
                    if (spc == 1 or spc == 12 or spc == 123 or spc == 13):
                        roll = random.randint(1,6)
                        if roll >= atksave:
                            hotdeath += 0
                        else:
                            roll = random.randint(1,6)
                            if roll >= atksavetwo and atksavetwo != 0:
                                hotdeath += 0
                            else:
                                hotdeath += 1
                roll = random.randint(1,6)
                if hitTwo <= roll:
                    hit += 1
                else:
                    missed += 1
                    if roll == 1:
                        if (spc == 1 or spc == 12 or spc == 123 or spc == 13):
                            roll = random.randint(1,6)
                            if roll >= atksave:
                                hotdeath += 0
                            else:
                                roll = random.randint(1,6)
                                if roll >= atksavetwo and atksavetwo != 0:
                                    hotdeath += 0
                                else:
                                    hotdeath += 1
    if missed < re:
        rerolls = missed
    else:
        rerolls = re
    print(roll_list)

    #rerolls
    
    if re < 0:
        count = 0
        while count < rerolls:
            roll = random.randint(1,6)
            count += 1
            if gbs == 0: 
                if hitRoll <= roll:
                    hit += 1
                else:
                    missed +=1
                    if roll == 1:
                        if (spc == 1 or spc == 12 or spc == 123 or spc == 13):
                            roll = random.randint(1,6)
                            if roll >= atksave:
                                hotdeath += 0
                            else:
                                roll = random.randint(1,6)
                                if roll >= atksavetwo and atksavetwo != 0:
                                    hotdeath += 0
                                else:
                                    hotdeath += 1
            else:
                if 2 <= roll:
                    hit += 1
                else:
                    roll = random.randint(1,6)
                    if hitTwo <= roll:
                        hit += 1
                    else:
                        missed += 1
                        if roll == 1:
                            if (spc == 1 or spc == 12 or spc == 123 or spc == 13):
                                roll = random.randint(1,6)
                                if roll >= atksave:
                                    hotdeath += 0
                                else:
                                    roll = random.randint(1,6)
                                    if roll >= atksavetwo and atksavetwo != 0:
                                        hotdeath += 0
                                    else:
                                        hotdeath += 1
    hit = hit - hotdeath
    if hit != 0:
        print ("number of hits: {}".format(hit))
        
    if hotdeath >= 1:
        print ('number of gets hot casualties: {}'.format(hotdeath))
    if hit == 0:
        print ("there were no hits")
   
   #wounds
    if hit != 0:
        if spc == 13 or spc == 123 or spc == 3 or spc == 23:
            HV = 0
        else:
            TT = int(input("what is the targets toughness: "))
            WSR = int(input("what is the weapon strength: "))
            HV = TT-WSR
        count=0
        wound=0
        six = 0
        WV =""
        if HV == 0:
            WV = 4
        elif HV ==-1:   
            WV = 3
        elif HV <=-2:
            WV = 2
        elif HV ==1:
            WV = 5
        elif 2 <= HV <= 3:
            WV = 6
        elif HV >= 4:
            WV = 0
        elif spc == 13 or spc == 123 or spc == 3 or spc == 23:
            WV = 4
        while count < hit:
            roll = random.randint(1,6)
            if WV == 0:
                print ("there are no wounds")
                break
            elif roll >= WV:
                wound +=1
                count +=1
                if spc == 2 or spc == 12 or spc == 123 or spc == 32:
                    if roll == 6:
                        six += 1
                        wound -= 1
            else:
                count +=1
        redundant = wound + six
        print ("there are {} wounds inflicted".format(redundant))
    else:
        print ('there are no wounds')
        wound = 0






    #save rolls
    if wound != 0:
        armourSave = int(input("what is unit armour save; "))
        save = int(input("what is the invoulnerable or cover save (if none write 0): "))
        painSave = int(input("what is the feel no pain save (if none write 0): "))
        weaponAP = int(input("what is the weapon AP: "))
        count = 0
        live = 0
        dead = 0
        while count < wound:
            roll = random.randint(1,6)
            if weaponAP <= armourSave:
                if save == 0 and painSave == 0:
                    print('there are {} wounds'.format(redundant))
                    break
                else:
                    if roll >= save and save != 0:
                        live += 1
                        count += 1
                    elif 2*TT > WSR:
                        roll = random.randint(1,6)
                        if roll >= painSave and painSave != 0:
                            live += 1
                            count += 1
                        else:
                            count += 1
                            dead += 1
                    else:
                        count += 1
                        dead += 1
            elif roll >= armourSave:
                live += 1
                count += 1
            else:
                if painSave < 0 and 2*TT > WSR:
                    roll = random.randint(1,6)
                    if roll >= painSave:
                        live += 1
                        count += 1
                    else:
                        dead += 1
                        count += 1
                else:
                    dead += 1
                    count += 1
        count = 0
        while count < six:
            roll = random.randint(1,6)
            if roll >= save and save != 0:
                live += 1
                count += 1
            elif 2*TT > WSR:
                roll = random.randint(1,6)
                if roll >= painSave and painSave == 0:
                    live += 1
                    count += 1
                else:
                    count += 1
                    dead += 1
            else:
                count += 1
                dead += 1
        print ("there are {} wounds, and".format(dead))
        print ("{} saves.".format(live))
    else:
        print ('nothing dies')
