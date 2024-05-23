
import random
import time
import socket

tilf_tall = random.randint(1, 100)
gjett = 0
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

print("""
------------------------------------------------
|                 VELKOMMEN                    |
| Din jobb er å gjette et tall mellom 1 og 100 |
------------------------------------------------
""")

while gjett != tilf_tall:
    print("== SKRIV UNDER ==")
    gjett = input("Gjett: ")

    tilf_tall_diff = tilf_tall - int(gjett)

    if tilf_tall_diff > 0:
        print("""
             
        Tallet er større
             
        """)
    elif tilf_tall_diff < 0:
        print("""
             
        Tallet er mindre
             
        """)
    elif tilf_tall_diff == 0:
        break

print("""
=================
Du gjettet riktig!
=================
""")


# Kilder: Copilot
