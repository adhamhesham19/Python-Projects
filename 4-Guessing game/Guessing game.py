import random

attemps_list=[]


def showScor():
    if not attemps_list: 
        print("There no scor , please start ")
    else:
        print(f"The current high scor is {min(attemps_list)} attemps. ")


attepmts =0

rand_number=random.randint(1 ,10)

print("Hello player! welcome!")
player_name=input("what's your name? ")

wanna_play=input(
    f"Hi {player_name} , would you like to play the gussing game?"
    "(Enter Yes /NO): ").lower()

if wanna_play=="no": 
    print("That's cool , thanks!")
    exit()
else:
    showScor()

while wanna_play =="yes":
    try:
        guss= int(input("Pick a number form 1 to 10 : "))
        if (guss<1 or guss >10 ):
            raise ValueError("please guss anumber within the given range. ")
        attepmts+=1


        
        if(guss==rand_number):
            print("Nice , you got it!")
            
            print(f"It took you {attepmts} attepmts!")
            wanna_play=input(" would you like to play again? (Enter Yes /NO): ")
            attemps_list.append(attepmts)


            if wanna_play=="no":
                print("that's cool!, have a good day.")
            else:
                attepmts=0
                rand_number=random.randint(1 , 10)
                showScor()
                continue


        elif(guss > rand_number):
            print("It's lower!")
        elif(guss< rand_number):
            print("It's higher!")
    
    
    
    
    except ValueError as err:
        print(err)