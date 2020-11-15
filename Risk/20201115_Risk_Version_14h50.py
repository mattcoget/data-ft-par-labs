#!/usr/bin/env python3
#make the file exectuable 
# --------------------------------------
# INITIALIZE
#import colors for background
#from colorama import Fore

import time

all_players = [None] * 6

class Player:
    def __init__(self, name, soldiers):
        self.name = name
        self.soldiers = soldiers
        self.countries = []


def play_game():
    nb_players = phase_initialize()
    all_players[0].countries.append(get_country(0)) 
    print(nb_players, "players")
    game_not_finished = True
    while game_not_finished:
        user_turn(None, all_players[0])
        time.sleep(1)
        break
    #for each player launch user turn after each player played

def phase_initialize():
    #get list of players (limit: six players)
    players_lst = ["delete me"]
    while players_lst[-1] != "q":
        players_lst.append(input("Please insert a player's name or ‘q’ once finished\n"))
        if len(players_lst) > 7:
            print("""This game is limited to 6 participents.\n
                Let's start over.""")
            players_lst = ["delete me"]
    players_lst = players_lst[1:-1]
    #print(players_lst)
    
    #create object names
    players_enu = [""]
    for i, x in enumerate(range(len(players_lst))):
        players_enu.append("player_"+str(i))
    players_enu = players_enu[1:]
    nb_players = len(players_lst)
    #print(players_enu)
    
    # create objects from list of object names
    for i, x in enumerate(players_enu):
       # print(x)
        globals()[x] = Player(players_lst[i], init_soldiers(len(players_lst)))
        all_players[i] = globals()[x]
       # print(globals()[x].name)
    #print(player_1.name)
    #print(player_1.soldiers)
    return nb_players

# --------------------------------------
# BOARD SETUP
def init_soldiers(num_players):
    """
    If 2 are playing, see special instructions.If 3 are playing, each player counts out 35 Infantry.If 4 are playing, 
    each player counts out 30 Infantry.
    If 5 are playing, each player counts out 25 Infantry.If 6 are playing, each player counts out 20 Infantry.
    """
    if num_players == 2:
        return(40) # notice - it's not following the O.G rules. 
    elif num_players == 3:
        return(35)
    elif num_players == 4:
        return(30)
    elif num_players == 5:
        return(25)
    elif num_players == 6:
        return(20)


class country:
    def __init__(self, name, country_number, neighbours):
        self.name = name
        self.country_number = country_number
        self.neighbours = neighbours
        self.owner = 0
        self.soldiers = 0


#class Gameplay:
    
all_countries = [country("Afghanistan", 1, [36, 22, 16, 7, 37]), 
country("Alaska", 2, [3, 27, 20]), 
country("Alberta", 3, [2, 27, 28, 41]), 
country("Argentina", 4, [5, 29]), 
country("Brazil", 5, [4, 29, 38, 25]),
country("Central America", 6, [38, 41, 11]),
country("China", 7, [23, 33, 37, 1, 16, 32]),
country("Congo", 8, [25, 9, 34]),
country("East Africa", 9, [22, 12, 25, 8, 34, 21]),
country("Eastern Australia", 10, [24, 17,39]),
country("Eastern United States", 11, [30, 28, 41, 6]),
country("Egypt", 12, [9, 25, 35, 22]),
country("Great Britain", 13, [15, 31, 26, 40]),
country("Greenland", 14, [15, 30, 28, 27]),
country("Iceland", 15, [14, 13, 31]),
country("India", 16, [22, 1, 7, 32]),
country("Indonesia", 17, [32, 24, 39]),
country("Irkutsk", 18, [42, 20, 33, 23]),
country("Japan", 19, [20, 23]),
country("Kamchatka", 20, [2, 42, 18, 23, 19]),
country("Madagascar", 21, [9, 34]) ,
country("Middle East", 22, [16, 1, 36, 35, 12, 9]),
country("Mongolia", 23, [19, 20, 18, 33, 7]),
country("New Guinea", 24, [39, 10, 17]),
country("North Africa", 25, [5, 35, 12, 9, 8, 40]),
country("Northern Europe", 26, [36, 31, 13, 40, 35]),
country("Northwest Territory", 27, [2, 3, 14, 28]),
country("Ontario", 28, [30, 14, 27, 3, 41, 11]),
country("Peru", 29, [4, 5, 38]),
country("Quebec", 30, [11, 28, 14]),
country("Scandinavia", 31, [36, 26, 13, 15]),
country("Siam", 32, [7, 16, 17]),
country("Siberia", 33, [37, 7, 23, 18, 42]),
country("South Africa", 34, [8, 9, 21]),
country("Southern Europe", 35, [40, 26, 36, 22, 12, 25]),
country("Ukraine", 36, [37, 1, 22, 35, 26, 31]),
country("Ural", 37, [36, 1, 7, 33]),
country("Venezuela", 38, [5, 6, 29]),
country("Western Australia", 39, [10, 17, 24]),
country("Western Europe", 40, [13, 25, 26, 35]),
country("Western United States", 41, [3, 28, 11, 6]),
country("Yakutsk", 42, [33, 18, 20])]


#initiation function
#def __init__ (self):
#    return
    
def user_turn(self, player):
    print("It's", player.name ,"turn!")
    reinforcement(self, player)
    attack(self, player)
    fortify(self, player)
    print(player.name, "turn is finished!")

def print_list_countries(country_list):
    for i in country_list:
        print(i.name, i.country_number, i.neighbours, i.soldiers)




#Function reinforcement
def reinforcement(self, player):
    
    #reinforcement based of the number of countries
    new_soldiers = 0
    if len(player.countries) < 9:
        new_soldiers = 3
    else:
        new_soldiers = len(player.countries/3)+1
            
    #list of countries from a continent
    africa =  [8, 9, 12, 21, 25, 34]
    asia = [1, 7, 16, 18, 19, 20, 22, 23, 32, 33, 37, 42]
    europe = [13, 15, 26, 31, 35, 36, 40]
    north_america = [2, 3, 6, 11, 14, 27, 28, 30, 41]
    oceania = [10, 17, 24, 39]
    south_america = [4, 5, 29, 38]

    #reinforcement based of the continents owned

    for i in player.countries:
        if africa in player.countries:
            new_soldiers += 3
        elif asia in player.countries:
            new_soldiers += 7
        elif europe in player.countries:
            new_soldiers +=5
        elif north_america in player.countries:
            new_soldiers += 5
        elif oceania in player.countries:
            new_soldiers += 2
        elif south_america in player.countries:
            new_soldiers += 2

    #placing new soldiers
    
    while new_soldiers > 0:
        print_list_countries(player.countries)
        time.sleep(1)
        print("You have", new_soldiers, "soldiers to place.")
        time.sleep(2)
        placement = int(input('Where to you want to place them? '))
        
        #have to add the error handling 
        #there is a lot of cases : bad names, not your country, lower, uppercase, not complete, no space ...
        if placement not in player.countries:
            time.sleep(1)
            print("This is not one of your countries! Select one among the ones you own.")
            time.sleep(1)
            print("The list of your countries is") 
            print_list_countries(player.countries)
        else:
            continue

        placement_size = int(input('How many soldiers? '))
        if placement_size > new_soldiers:
            time.sleep(1)
            print("You don't have that many soldiers! You can only add", new_soldiers, "new soldiers to your army.")
        elif placement_size == 0:
            time.sleep(1)
            print("You have to place", new_soldiers, "not 0 if you want to win!")
        else:
            #add the soldiers to the country you choose
            get_country(placement).soldiers += placement_size
            new_soldiers -= placement_size
            
    print("Reinforcement phase is over.")



def get_country(country_number):
    return all_countries[country_number-1]


#Function Attacking    
def attack(self, player):
    
    print("Attack phase begin.")
    print("Your empire and armies are:")
    print_list_countries(player.countries)
    
    choice = input("Do you want to attack any countries? y/n : ")
    if choice == "n":
        #go to the fortifying process  
        pass
        
    elif choice == "y" :
        #go to the attacking process
        #input with which country attack
        print_list_countries(player.countries)
        country_attacking_number = int(input("With which you want to attack : "))
        country_attacking = get_country(country_attacking_number)
        
        
        #input which country, the player want to attack
        #dans la liste des pays du joueur, quel est le pays choisi + quels sont ses voisions
        print(country_attacking.neighbours)
        country_attacked_number = int(input("In the countries below, which you want to attack: "))
        country_attacked = get_country(country_attacked_number)
        
        if country_attacked_number not in country_attacking.neighbours:
            print("This is not a country next to your empire! Try again")
            #print countries

                    
        print (country_attacking.name, "attacks", country_attacked.name, "with", country_attacking.soldiers,"against", country_attacked.soldiers,".")
        #perhaps we can add the number of soldiers for each country
        
        #dices
        import random

        offence_dice1 = random.randint(1, 6)
        offence_dice2 = random.randint(1, 6)
        offence_dice3 = random.randint(1, 6)

        defense_dice1 = random.randint(1, 6)
        defense_dice2 = random.randint(1, 6)


        three_attack = sorted((offence_dice1, offence_dice2, offence_dice3),reverse = True)
        two_attack = sorted((offence_dice1, offence_dice2), reverse = True)
        two_defense = sorted((defense_dice1, defense_dice2), reverse = True)
        one_defense = [defense_dice1]


        ### Attack ###              
        if country_attacking.soldiers >= 3:
            if country_attacked.soldiers >= 2:
                print(three_attack, two_defense)
                #3 attackers vs. 2 defenders
                if two_defense[0] >= three_attack[0]:
                    country_attacking.soldiers -= 1
                    print("Attack:", country_attacking.soldiers, "Defense:", country_attacked.soldiers)
                else:
                    country_attacked.soldiers -= 1
                    print("Attack:", country_attacking.soldiers, "Defense:", country_attacked.soldiers)

                if two_defense[1] >= three_attack[1]:
                    country_attacking.soldiers -= 1
                    print("Attack:", country_attacking.soldiers, "Defense:", country_attacked.soldiers)
                else:
                    country_attacked.soldiers -= 1
                    print("Attack:", country_attacking.soldiers, "Defense:", country_attacked.soldiers)

            elif country_attacked.soldiers == 1:
                print(three_attack, one_defense)
                #3 attackers vs. 1 defender      
                if one_defense[0] >= three_attack[0]:
                    country_attacking.soldiers -= 1
                    print("Attack:", country_attacking.soldiers, "Defense:", country_attacked.soldiers)
                else:
                    country_attacked.soldiers -= 1
                    print("Attack:", country_attacking.soldiers, "Defense:", country_attacked.soldiers)

        elif (country_attacking.soldiers == 2):
            if country_attacked.soldiers >= 2:
                print(three_attack, two_defense)
                #2 attackers vs. 2 defenders
                if two_defense[0] >= two_attack[0]:
                    country_attacking.soldiers -= 1
                    print("Attack:", country_attacking.soldiers, "Defense:", country_attacked.soldiers)
                else:
                    country_attacked.soldiers -= 1
                    print("Attack:", country_attacking.soldiers, "Defense:", country_attacked.soldiers)

                if two_defense[1] >= two_attack[1]:
                    country_attacking.soldiers -= 1
                    print("Attack:", country_attacking.soldiers, "Defense:", country_attacked.soldiers)
                else:
                    country_attacked.soldiers -= 1
                    print("Attack:", country_attacking.soldiers, "Defense:", country_attacked.soldiers)

            elif country_attacked.soldiers == 1:
                print(three_attack, one_defense)
                #2 attackers vs. 1 defender      
                if one_defense[0] >= two_attack[0]:
                    country_attacking.soldiers -= 1
                    print("Attack:", country_attacking.soldiers, "Defense:", country_attacked.soldiers)
                else:
                    country_attacked.soldiers -= 1
                    print("Attack:", country_attacking.soldiers, "Defense:", country_attacked.soldiers)


        if country_attacked.soldiers == 0:
            #capturing a country
            #transfer of soldiers from attacking country to attacked country
            print("You conquer", country_attacked.name, country_attacked.country_number)
            print("There are", country_attacking.soldiers, "attacking soldiers left!")
            country_attacking.soldiers -= 1
            country_attacked.soldiers +=1
            country_attacked.owner = player
            
        elif country_attacking.soldiers == 1:
            print("You can't attack anymore", country_attacked)
            print("There are", country_attacked.soldiers, "defending soldiers left!")
        
                
                
    else:
        print("It's y for yes and n for no, and not", choice, "!")


def fortify(self, player):
    
    #print the empire and the armies
    print_list_countries(player.countries)
    destination = input('Where do you want to move soldiers? ')
    if destination not in player.countries:
        print ("This in not one of your countries! Choose among the countries below:")
        print_list_countries(player.countries)
    else:
        departure = input('From which country do you want to move soldiers to', destination, "?")
        if departure not in player.countries:
            print("This in not one of your countries! Choose among the countries below: ")
            print_list_countries(player.countries)
        elif departure.soldiers == 1:
            print("You can't divide a soldier in two, choose another country.")
            print_list_countries(player.countries)
        else:
            moving_soldiers=input('How many soldiers?')
            if moving_soldiers > soldiers.country_attacking:
                print("You don't have enough soldier, you can choose max", departure.soldiers-1)
            elif moving_soldiers == 0:
                print("You have to choose between 1 and", departure.soldiers-1)
            else:
                departure -= moving_soldiers
                destination += moving_soldiers

# --------------------------------------
# GAME PLAY
# --------------------------------------
# RUN GAME
play_game()
print(player_1.soldiers)
