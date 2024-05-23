
import random
from itertools import repeat

# Explanation
    # danger_level: Level of danger in the specific location
    # location: Coordinates of the specific location.

    # Center location is always 0,0

class Location:
    def __init__(self, name, danger_level, location):
        self.name = name
        self.danger_level = danger_level
        self.location = location

class Enemy:
    def __init__(self, name, health, damage, location):
        self.name = name
        self.health: int = health
        self.damage: int = damage
        self.location = location

class Locations:

    grid_min = 1
    grid_max = 100

    school_found = False

    StartPoint = Location(name="StartPoint", danger_level=0, location=[0, 0])
    Home = Location(name="Home", danger_level=0, location=[random.randint(grid_min, grid_max),  random.randint(grid_min, grid_max)])
    Forest = Location(name="Forest", danger_level=7, location=[random.randint(grid_min, grid_max), random.randint(grid_min, grid_max)])
    Cave = Location(name="Cave", danger_level=4, location=[random.randint(grid_min, grid_max), random.randint(grid_min, grid_max)])
    Beach = Location(name="Beach", danger_level=2, location=[random.randint(grid_min, grid_max), random.randint(grid_min, grid_max)])
    School = Location(name="School", danger_level=10, location=[random.randint(grid_min, grid_max), random.randint(grid_min, grid_max)])

class Enemies:
    PlasticSir = Enemy(name="Plastic Sir", health=500, damage=45, location=Locations.School.name)

class Player:
    name = ""
    health = 100
    damage = 5
    x = 0
    y = 0

class Movement:
    @staticmethod
    def north():
        Player.x += 10

    @staticmethod
    def south():
        Player.x -= 10

    @staticmethod
    def west():
        Player.y -= 10

    @staticmethod
    def east():
        Player.y += 10

def game_start():
    print("============")
    print("Game Name")
    print("============")
    start_input = input("Press 'Enter' to begin...   ")
    print("============")
    name_input = input("> What's your name?   ")

    Player.name = name_input

def game_control():
    while True:
        print("-------------------------------")
        print(Player.name, ": ", " | ", Player.health, " HP"," | ","x: ",Player.x,"y: ",Player.y)
        print("-------------------------------")

        print("[1] Go north")
        print("[2] Go south")
        print("[3] Go west")
        print("[4] Go east")

        action_input = input("> What do you want to do?    ")

        if action_input == "1":
            Movement.north()
        elif action_input == "2":
            Movement.south()
        elif action_input == "3":
            Movement.west()
        elif action_input == "4":
            Movement.east()
        elif action_input == "m":
            print(Locations.Home.name,Locations.Home.location)
            print(Locations.Forest.name,Locations.Forest.location)
            print(Locations.Cave.name,Locations.Cave.location)
            print(Locations.Beach.name,Locations.Beach.location)
            if Locations.school_found == False:
                print(Locations.School.name,": [???,???]")
            else:
                print(Locations.School.name,Locations.School.location)

        # Check if the player travels outside the grid
        if Player.x > 100:
            Player.x = 100
        if Player.y > 100:
            Player.y = 100

        print("-------------------------------")


game_start()
game_control()
