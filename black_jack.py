import random 
import time 
import os
cards = [11,2,3,4,5,6,7,8,9,10,10,10,1]
player = []
def clear():
    os.system("cls" if os.name=="nt" else os.system("clear")) 
def adjust_for_ace(hand):
    while sum(hand) > 21 and 11 in hand:
        hand[hand.index(11)] = 1
    return hand
def game():
        print("""
    1.froggy
    2.twenty one
    3.snake
    """)
        game = input("what will you play to day?: ")
        if game.lower() == "froggy" or game.lower() ==  "snake":
            print("checking")
            time.sleep(2)
            print ("coming soon")
            print("-_-"*10)
        elif game.lower() == "twenty one" :
            player = []
            computer_Cards = []
            print("checking........")
            time.sleep(2)
            print("starting game........")
            print("-_- "*10)
            time.sleep(5)
            player_card=random.choices(cards ,k=2)
            player.extend(player_card)
            print (f" you got {player} they  = {sum(player)} ") 
            computer_Cards = [random.choice(cards )]
            print (f"computer gets {computer_Cards}")
            while sum(player) <21:
                more_card = input("do you want to get more card (Y/N) ")        
                if more_card.lower() == "y":
                    more_card = random.choice(cards)  
                    adjust_for_ace(computer_Cards)
                    player.append(more_card)
                    print (f" you got {player} they  = {sum(player)} ")
                else:
                    break
            if sum (player) >21:
                adjust_for_ace(player)
            while sum(computer_Cards) <17:
                computer_Cards.append(random.choice(cards))
                adjust_for_ace(computer_Cards)
            print(f"computer got {computer_Cards} thats = {sum(computer_Cards)}")
            if sum(computer_Cards) >21:
                adjust_for_ace(computer_Cards)
            print("finding the winner")
            time.sleep(2)
            if sum(player ) == sum(computer_Cards) or sum(player)>21 and sum(computer_Cards)>21 :
                print("draw")
            elif sum(player ) <=21 and sum(computer_Cards)<= 21 and sum(player) >  sum(computer_Cards) or sum(computer_Cards) > 21:
                print("""
             *****
            you won
             *****
            """)
            elif sum(player ) <=21 and sum(computer_Cards)<= 21 and sum(computer_Cards) >  sum(player) or sum(player) >21:
                print("""
             (:__:)
            you lost
             (:__:)
            """)
        else:
            print ("error")
while True:
    if input("press entre to start") == "":
        more_game = "y"
        while more_game=="y":
            clear()
            game() 
            more_play = input("Do you want to play more(Y/N)?: ").lower()
            if more_play == "n":
                clear()
                break   
        clear()
        break
    break
