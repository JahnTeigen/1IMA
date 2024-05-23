import random

WALK_SPEED = 1

class GameInfo:
    name = "2D Game"
    author = "Fredrik"

# Coordinate generator
def coordinates():
    x = random.randint(0, 100)
    y = random.randint(0, 100)
    return x,y

# Players, enemies
class Player:
    name = "Player 1"
    health = 100
    location_x, location_y = coordinates()

# Locations
class StartPoint:
    name = "Start Point"
    location_x, location_y = coordinates()

class Forest:
    name = "Forest"
    location_x, location_y = coordinates()

class Neighborhood:
    name = "Neighborhood"
    location_x, location_y = coordinates()

def north():
    Player.location_y += WALK_SPEED

def south():
    Player.location_y -= WALK_SPEED

def west():
    Player.location_x -= WALK_SPEED

def east():
    Player.location_x += WALK_SPEED

def check_location():
    if Player.location_x & Player.location_y == Forest.location_x & Forest.location_y:
        pass

def debug():
    print("---DEBUG---")
    print(f"{Forest.name} x:{Forest.location_x}, y:{Forest.location_y}")
    print(f"{Neighborhood.name} x:{Neighborhood.location_x}, y:{Neighborhood.location_y}")

    print("-----------")

# Game start
def game_action():
    Player.location_x = StartPoint.location_x
    Player.location_y = StartPoint.location_y

    while True:

        check_location()

        print(Player.name, "|| x: ", Player.location_x, "y: ", Player.location_y, "| Health: ", Player.health)
        action_input = input("[n,s,w,e] >   ")

        # Movement
        if action_input == "n":
            north()
        elif action_input == "s":
            south()
        elif action_input == "w":
            west()
        elif action_input == "e":
            east()
        elif action_input == "debug":
            debug()
        # Other
        else:
            print("== [ Turn skipped ] ==")

        # Location control



def game_start():
    print("______________________________")
    print("|  ________________________  |")
    print("|  |                      |  |")
    print("|  |                      |  |")
    print("|  |        2D Spill      |  |")
    print("|  | Trykk 'Enter' for å  |  |")
    print("|  |       forsette       |  |")
    print("|  |                      |  |")
    print("|  |______________________|  |")
    print("|____________________________|")

    continue_action = input("...")
    name_input = input("Skriv inn navn:  ")
    print("----------")
    Player.name = name_input

    game_action()

game_start()