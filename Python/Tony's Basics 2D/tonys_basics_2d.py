import random
import time

class Text:

    help_text = "Velg 1,2,3 eller 4 for å utføre en handling. Det du gjør avhenger av det du valgte.\n Målet er å samle inn ethernet-kabler og slippe unna Tony."

    main_title = """
    ████████╗ ██████╗ ███╗   ██╗██╗   ██╗███████╗
    ╚══██╔══╝██╔═══██╗████╗  ██║╚██╗ ██╔╝██╔════╝
       ██║   ██║   ██║██╔██╗ ██║ ╚████╔╝ ███████╗
       ██║   ██║   ██║██║╚██╗██║  ╚██╔╝  ╚════██║
       ██║   ╚██████╔╝██║ ╚████║   ██║   ███████║
       ╚═╝    ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝

    ██████╗  █████╗ ███████╗██╗ ██████╗███████╗  
    ██╔══██╗██╔══██╗██╔════╝██║██╔════╝██╔════╝  
    ██████╔╝███████║███████╗██║██║     ███████╗  
    ██╔══██╗██╔══██║╚════██║██║██║     ╚════██║  
    ██████╔╝██║  ██║███████║██║╚██████╗███████║  
    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝ ╚═════╝╚══════╝  
    """

    death_screen = """
    ██╗   ██╗ ██████╗ ██╗   ██╗    ██████╗ ██╗███████╗██████╗ 
    ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██╔══██╗██║██╔════╝██╔══██╗
     ╚████╔╝ ██║   ██║██║   ██║    ██║  ██║██║█████╗  ██║  ██║
      ╚██╔╝  ██║   ██║██║   ██║    ██║  ██║██║██╔══╝  ██║  ██║
       ██║   ╚██████╔╝╚██████╔╝    ██████╔╝██║███████╗██████╔╝
       ╚═╝    ╚═════╝  ╚═════╝     ╚═════╝ ╚═╝╚══════╝╚═════╝ 
    """

    hide_text = """
#########################################################
#########################################################
######                                             ######
######                                             ######
#########################################################
#########################################################
#########################################################
######               / __       __ \               ######
######              (|  o   |   o  |)              ######
#########################################################
#########################################################
#########################################################
######             /                \              ######
######             | |            | |              ######
#########################################################
#########################################################
#########################################################
######            (((              )))             ######
######               |     ||     |                ######
#########################################################
#########################################################
#########################################################
    """

# Klasser
# Spiller
class Player:
    name = ""
    attack: int = 8
    ethernet_kabel: int = 0
    health: int = 100
    speed: float = 0.5


# Tony H
class TonyH:
    name = "Tony H Korsvik"
    default_name = ""
    attack: int = 10
    attacking = False
    health: int = 100
    speed: float = 0.4


#  Plastic Sir Morph
class PlasticSir:
    attack: int = 15
    health: int = 500
    speed: float = 1.0

    tonyh_attack_probability: int = 0

def PlayerKilled():
    # Main text
    print(Text.death_screen)

    quit()

# Funksjoner

plastic_sir_morphed = False
def PlasticSirMorph():
    plastic_sir_morphed = True
    TonyH.default_name = TonyH.name
    TonyH.name = "Plastic Sir"
    print("-~-~-~-~-~-~-~-~-~-~")
    print(TonyH.default_name," har blitt transformert til ",TonyH.name,"!")
    print("-~-~-~-~-~-~-~-~-~-~")

    TonyH.attack = PlasticSir.attack
    TonyH.health = PlasticSir.health
    TonyH.speed = PlasticSir.speed

    time.sleep(3)
    Action()


def TonyAttackRandomiser():
    tonyh_attack_probability = random.randint(1, tonyh_attack_difficulty)
    if tonyh_attack_probability == tonyh_attack_difficulty:
        TonyH.attacking = True
    else:
        TonyH.attacking = False

ethernet_acquire_difficulty: int = 5
def EthernetAcquireRandomiser():
    if random.randint(1, ethernet_acquire_difficulty) == 1:
        Player.ethernet_kabel += 1
    if Player.ethernet_kabel == 8:
        PlasticSirMorph()

tonyh_attack_difficulty: int = 4
def TonyHDamageRandomiser():
    tonyh_attack_probability = random.randint(1,2)
    if tonyh_attack_probability == 1:
        TonyH.health -= Player.attack
    elif tonyh_attack_probability == 2:
        Player.health -= TonyH.attack

action1 = True
action2 = True
action3 = True
action4 = True

def Action():

    while True:
        TonyAttackRandomiser()

        print("------------------")
        if TonyH.attacking == True:
            pass
        print(f"{TonyH.name}: {TonyH.health}HP")

        print(f"{Player.name}: {Player.health}HP | {Player.ethernet_kabel} Ethernet-kabler")

        print("------------------")
        if plastic_sir_morphed == False:
            print("[1] Lete etter ethernet-kabel")
        else:
            print("Alle kabler funnet")
        print("[2] Gjemme deg")
        if TonyH.attacking == True:
            action3 = False
            action4 = False

            print("[3] Løp fra Tony")
            print("[4] Forsvar deg selv")
        else:
            action3 = False
            action4 = False

            print("")
            print("[?] Hjelp")

        action_input = input(" > Hva vil du gjøre? ")
        if action_input == "1":
            if plastic_sir_morphed == False:
                EthernetAcquireRandomiser()
            else:
                quit()
        elif action_input == "2":
            if action1 == True:
                TonyH.attacking = False
                print(Text.hide_text)
                print("""
                      ==========
                      Du gjemte deg i et skap. Tony så deg ikke.
                      ==========
                      """)
            else:
                quit()
        elif action_input == "3":
            if action1 == True:
                TonyH.attacking = False
            else:
                quit()
        elif action_input == "4":
            if action1 == True:
                TonyHDamageRandomiser()
            else:
                quit()
        elif action_input == "?":
            print(Text.help_text)
        else:
            quit()

        if Player.health <= 0:
            PlayerKilled()

    while plastic_sir_morphed == True:
        TonyH.attacking = True

def GameStart():
    print("===============================")
    print(" ")
    print(Text.main_title)
    print(" ")
    print("===============================")
    start_game = input("Trykk på 'Enter' for å starte spillet...    ")

    player_name_input = input("Skriv inn navn: ")
    Player.name = player_name_input

    Action()


GameStart()