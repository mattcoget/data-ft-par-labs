#!/usr/bin/env python3
#make the file exectuable 
# --------------------------------------
# INITIALIZE

from colorama import Fore
txt_fore_clr = ["Fore.RED", "Fore.GREEN", "Fore.YELLOW", "Fore.BLUE", "Fore.MAGENTA", "Fore.CYAN"]

import time
import random

all_players = [None] * 6

# create the basic classes:
class Player:
    def __init__(self, name, soldiers, color):
        self.name = name
        self.soldiers = soldiers
        self.countries = [] # connect to country
        self.color = color

class country:
    def __init__(self, name, country_number, neighbours):
        self.name = name
        self.country_number = country_number
        self.neighbours = neighbours
        self.owner = 0
        self.soldiers = 1


# list of country objects of class country    
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

def play_game():
    nb_players = phase_initialize()
    if nb_players == 2:
        for i in range(int(len(all_countries)/2)):  
            all_players[0].countries.append(get_country(i+1))
            get_country(i+1).owner = all_players[0]
        for i in range(int(len(all_countries)/2), int(len(all_countries))):
            all_players[1].countries.append(get_country(i+1))
            get_country(i+1).owner = all_players[1]
    
    elif nb_players == 3:
        for i in range(int(len(all_countries)/3)):
            all_players[0].countries.append(get_country(i+1))
            get_country(i+1).owner = all_players[0]
        for i in range(int(len(all_countries)/3), int(2*len(all_countries)/3)):
            all_players[1].countries.append(get_country(i+1))
            get_country(i+1).owner = all_players[1]
        for i in range(int(2*len(all_countries)/3), int(len(all_countries))):
            all_players[2].countries.append(get_country(i+1))
            get_country(i+1).owner = all_players[2]

    elif nb_players == 4:
        for i in range(int(len(all_countries)/4)):
            all_players[0].countries.append(get_country(i+1))
            get_country(i+1).owner = all_players[0]
        for i in range(int(len(all_countries)/4), int(2*len(all_countries)/4)):
            all_players[1].countries.append(get_country(i+1))
            get_country(i+1).owner = all_players[1]
        for i in range(int(2*len(all_countries)/4), int(3*len(all_countries)/4)):
            all_players[2].countries.append(get_country(i+1))
            get_country(i+1).owner = all_players[2]
        for i in range(int(3*len(all_countries)/4), int(len(all_countries))):
            all_players[3].countries.append(get_country(i+1))
            get_country(i+1).owner = all_players[3]

    elif nb_players == 5:
        for i in range(int(len(all_countries)/5)):
            all_players[0].countries.append(get_country(i+1))
            get_country(i+1).owner = all_players[0]
        for i in range(int(len(all_countries)/5), int(2*len(all_countries)/5)):
            all_players[1].countries.append(get_country(i+1))
            get_country(i+1).owner = all_players[1]
        for i in range(int(2*len(all_countries)/5), int(3*len(all_countries)/5)):
            all_players[2].countries.append(get_country(i+1))
            get_country(i+1).owner = all_players[2]
        for i in range(int(3*len(all_countries)/5), int(4*len(all_countries)/5)):
            all_players[3].countries.append(get_country(i+1))
            get_country(i+1).owner = all_players[3]
        for i in range(int(4*len(all_countries)/5), int(len(all_countries))):
            all_players[4].countries.append(get_country(i+1))
            get_country(i+1).owner = all_players[4]

    elif nb_players == 6:
        for i in range(int(len(all_countries)/6)):
            all_players[0].countries.append(get_country(i+1))
            get_country(i+1).owner = all_players[0]
        for i in range(int(len(all_countries)/6), int(2*len(all_countries)/6)):
            all_players[1].countries.append(get_country(i+1))
            get_country(i+1).owner = all_players[1]
        for i in range(int(2*len(all_countries)/6), int(3*len(all_countries)/6)):
            all_players[2].countries.append(get_country(i+1))
            get_country(i+1).owner = all_players[2]
        for i in range(int(3*len(all_countries)/6), int(4*len(all_countries)/6)):
            all_players[3].countries.append(get_country(i+1))
            get_country(i+1).owner = all_players[3]
        for i in range(int(4*len(all_countries)/6), int(5*len(all_countries)/6)):
            all_players[4].countries.append(get_country(i+1))
            get_country(i+1).owner = all_players[4]
        for i in range(int(5*len(all_countries)/6), int(len(all_countries))):
            all_players[5].countries.append(get_country(i+1))
            get_country(i+1).owner = all_players[5]


    print(nb_players, "players")
    game_not_finished = True
    while game_not_finished:
        for p in all_players:
            if p != None:
                user_turn(None, p)
                if len(p.countries) == len(all_countries):
                    game_not_finished = False
    #for each player launch user turn after each player played

# --------------------------------------
# INITIALIZE
def phase_initialize():
    #get list of players (min: 2 playeres, limit: six players)
    players_lst = ["delete me"]
    try:
        while players_lst[-1] != "q":
            players_lst.append(input("Please insert a player's name or ‘q’ once finished\n"))
            if len(players_lst) > 7:
                print("""This game is limited to 6 participents.\n
                    Let's start over.""")
                players_lst = ["delete me"]

    except AttributeError:
        print("Please name at least 2 players ")
        
    players_lst = players_lst[1:-1]
    
    #create object names
    players_enu = [""]
    for i, x in enumerate(range(len(players_lst))):
        players_enu.append("player_"+str(i))
    players_enu = players_enu[1:]
    nb_players = len(players_lst)
    
    # create objects from list of object names
    for i, x in enumerate(players_enu):
       # print(x)
        globals()[x] = Player(players_lst[i], init_soldiers(len(players_lst)), txt_fore_clr[i])
        all_players[i] = globals()[x]

    # assign soldiers to countries
    #nbr_countries_lst = list(range(len(all_countries)))
    for i, x in enumerate(players_enu): 
        while globals()[x].soldiers > 0:
            random_country = random.choice(all_countries)
            #print(str(random_country))
            globals()[x].soldiers = globals()[x].soldiers - 1
    # choose a random country and put a soldier there # make owner of country
    
    return (nb_players)

def get_country(country_number):
    return all_countries[country_number-1]


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

# --------------------------------------
# GAME PLAY
    
def user_turn(self, player):
    tmp_clr = (player.color)
    print(tmp_clr)
    print(exec(tmp_clr) , "It's", player.name ,"turn!") # why doesn't it show color?
    print("It's", player.name ,"turn!")
    reinforcement(self, player)
    attack(self, player)
    fortify(self, player)
    print(player.name, "turn is finished!")
    

def print_list_countries(country_list):
    for i in country_list:
        print(i.name, "- country number", i.country_number, "with", i.soldiers, "soldier(s)")

def print_list_neighbours(country_list):
    for i in country_list:
        print("The number of", i.name, "neighbours are", i.neighbours)


#Function reinforcement
def reinforcement(self, player):
    
    #reinforcement based of the number of countries
    new_soldiers = 0
    if len(player.countries) < 9:
        new_soldiers = 3
    else:
        new_soldiers = int(len(player.countries)/3+1)
            
    
    #placing new soldiers
    while new_soldiers > 0:
        print("Your empire is composed by:")
        print_list_countries(player.countries)
        time.sleep(1)
        print("You have", new_soldiers, "soldiers to place.")
        time.sleep(1)
        placement = int(input('Where to you want to place them? '))
        
        if get_country(placement) not in player.countries:
            time.sleep(1)
            print("This is not one of your countries! Select one among the ones you own.")
            time.sleep(1)
            print("The list of your countries is") 
            print_list_countries(player.countries)
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
            time.sleep(1)
            
    print("Reinforcement phase is over.")


#Function Attacking    
def attack(self, player):
    
    print("Attack phase begin.")
    time.sleep(1)
    print("Your empire and armies are:")
    print_list_countries(player.countries)
    
    choice = input("Do you want to attack any countries? y/n : ")
    if choice == "n":
        #go to the fortifying process  
        pass
        
    elif choice == "y" :
        #go to the attacking process
        #input with which country attack
        print("The list of your countries is:")
        time.sleep(1)
        print_list_countries(player.countries)
        time.sleep(1)
        country_attacking_number = int(input("With which you want to attack : "))
        country_attacking = get_country(country_attacking_number)
        
        
        #input which country, the player want to attack
        print("The number of the neighbours of this country are:")
        time.sleep(1)
        print(country_attacking.neighbours)
        country_attacked_number = int(input("In the countries below, which you want to attack: "))
        country_attacked = get_country(country_attacked_number)
        
        if country_attacked_number not in country_attacking.neighbours:
            time.sleep(1)
            print("This is not a country next to your empire! Try again.")
            
        print (country_attacking.name, "attacks", country_attacked.name, "with", country_attacking.soldiers,"against", country_attacked.soldiers,".")


        #Dices   
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
            time.sleep(1)
            print("You conquer", country_attacked.name, country_attacked.country_number)
            time.sleep(1)
            print("There are", country_attacking.soldiers, "attacking soldiers left!")
            country_attacking.soldiers -= 1
            country_attacked.soldiers +=1
            country_attacked.owner.countries.remove(country_attacked)
            country_attacked.owner = player
            country_attacked.owner.countries.append(country_attacked)
            
        elif country_attacking.soldiers == 1:
            time.sleep(1)
            print("You can't attack anymore", country_attacked)
            time.sleep(1)
            print("There are", country_attacked.soldiers, "defending soldiers left!")    
                
                
    else:
        print("It's y for yes and n for no, and not", choice, "!")
        pass

def fortify(self, player):
    
    print("The fortifying phase begins!")
    #print the empire and the armies
    time.sleep(1)
    choice_fortify = input("Do you want to move your soldiers? y/n : ")
    if choice_fortify == "n":
        #go to the next player  
        pass

    else:    
        destination = input('Where do you want to move soldiers? ')
        if destination not in player.countries:
            time.sleep(1)
            print ("This in not one of your countries! Choose among the countries below:")
            time.sleep(1)
            print_list_countries(player.countries)
        else:
            departure = input('From which country do you want to move soldiers to', destination, "?")
            if departure not in player.countries:
                time.sleep(1)
                print("This in not one of your countries! Choose among the countries below: ")
                time.sleep(1)
                print_list_countries(player.countries)
            elif departure.soldiers == 1:
                time.sleep(1)
                print("You can't divide a soldier in two, choose another country.")
                time.sleep(1)
                print_list_countries(player.countries)
            else:
                moving_soldiers=input('How many soldiers?')
                if moving_soldiers > int(departure.soldiers-1):
                    time.sleep(1)
                    print("You don't have enough soldier, you can choose max", departure.soldiers-1)
                elif moving_soldiers == 0:
                    time.sleep(1)
                    print("You have to choose between 1 and", departure.soldiers-1)
                else:
                    departure -= moving_soldiers
                    destination += moving_soldiers

# --------------------------------------
# GAME PLAY
# --------------------------------------
# RUN GAME
play_game()