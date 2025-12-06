import random

while True:
    player=input("'r' for Rock \n'p' for Paper \n's' for Scissors \n Choose A Move :  " )

    pcMove =random.choice(['r' ,'p' , 's'])

    print("Player choosed : " + player)
    print("Pc choosed : " + pcMove) 

    if player == pcMove:
        print("It's a tie")

    elif (player =='p' and pcMove =='r') or (player =='s' and pcMove=='p') or( player =='r' and pcMove=='s'):
        print("You Win! \n    ")

    else:
        print("You lose! \n   ")