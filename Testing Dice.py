import random

#roll dice
def dice_roll(ans):
        results_list=[]
        amount=ans
        while amount>=1:
            roll=random.randint(1,6)
            results_list.append(roll)
            amount-=1
        results_list.sort()
        return results_list
    
def modifier_applier(input_list):
    mod_value=int(input("What is the modifier?: "))
    for value in input_list:
        value+=mod_value
    return input_list



#count Hits/miss
def hit_counter(input_results_list):
    hits=0
    missed=0
    for shot in input_results_list:
        if shot >= BS:
            hits+=1
        else: missed +=1
    return hits
    


def miss_counter(input_results_list):
    hits=0
    missed=0
    for shot in input_results_list:
        if shot >= BS:
            hits+=1
        else: missed +=1
    return missed
    



#reroll
def reroll_counter(input_list):
    reroll_type= input("\n1's [1]; All [2]; or None[Enter]: ")
    reroll_list=input_list
    for reroll in reroll_list:
        if int(reroll_type)==1:
            if reroll ==1:
                reroll=random.randint(1,6)
                print("this",reroll)
                #add counter so you can set index below
                reroll_list[]=reroll
        if int(reroll_type)==2:
            if reroll < BS:
                reroll=random.randint(1,6)
        else: pass
    reroll_list.sort()
    return reroll_list


#wound Roll
def wound_list_creator(num_hits):
    wound_list=dice_roll(num_hits)
    wound_list.sort()
    return wound_list



#wound rerolls

def wound_counter(T,S,input_list):
    wounds_count=0
    for wound in input_list:
        if S>T:
            if S>=2*T:
                if wound >= 2:
                    wounds_count+=1
            else:
                if wound >=3:
                    wounds_count+=1
        if S==T:
            if wound >=4:
                wounds_count+=1
        if S<T:
            if T>=2*S:
                if wound==6:
                    wounds_count+=1
            else:
                if wound >=5:
                    wounds_count+=1
    return wounds_count


#save rolls
def save_roll_creator(num_wounds):
    save_roll_list=dice_roll(num_wounds)
    save_roll_list.sort()
    return save_roll_list

#save counter
def save_test_creator(input_list,AP,save_value):
    saves=0
    failed=0
    for save in input_list:
        if save-AP>save_value:
            saves+=1
        else:
            failed+=1
    return saves



count=1
while count==1:
    #info
    print("")
    print("")
    print("")
    print("")
    print("\n[New Attack Start]\n")
    print("----------------------")
    answer=int(input("\nEnter number of dice to roll: "))
    BS = int(input("Enter Ballistic Skill value: "))

    #hits
    results = dice_roll(answer)
    print("The results are: \n",results)
    hit_results= hit_counter(results)
    print("\nHit results: ",hit_results)
    miss_results= miss_counter(results)
    print("\nMiss results: ",miss_results)
    
    #reroll
    print('---------------------------------------')
    print("\nAny available Rerolls?")
    updated_list=reroll_counter(results)
    updated_list=modifier_applier(updated_list)
    print("Updated List Results: \n",updated_list)
    hit_results= hit_counter(results)
    print("\nHit results: ",hit_results)
    miss_results= miss_counter(results)
    print("\nMiss results: ",miss_results)
    
    #wounds
    Wound_rolls=wound_list_creator(hit_results)
    print("Wound Rolls: \n",Wound_rolls)
   
   
    #wounds reroll
    print("\n Any Avaiable Rerolls?")
    Wound_rolls=reroll_counter(Wound_rolls)
    Wound_rolls=modifier_applier(Wound_rolls)
    print("Wound rolls after rerolls: \n",Wound_rolls)
    #wounds final
    toughness=int(input("What is targets Toughness?: "))
    Strength=int(input("What is the Weapons Strength?: "))
    AP=int(input("What is the Weapon AP value?: "))
    num_wounds=wound_counter(toughness,Strength,Wound_rolls)
    print("Number of wounds: \n",num_wounds)
   
    #saves
    Save_roll=save_roll_creator(num_wounds)
    print("Save roll List: \n",Save_roll)
    save_value=int(input("what is the Targets save value?: "))
    successful_saves=save_test_creator(Save_roll,AP,save_value)
    print("Number of successful saves: ",successful_saves)
    print("Number of Failed saves: ",num_wounds-successful_saves)


    #totals



#update list

    
        
 




