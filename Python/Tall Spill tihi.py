import random
import time as t
import socket as s

hostname = s.gethostname()
IPaddr = s.gethostbyname(hostname)
def spill():
    print("Jeg tenker på et tall mellom 1 og 100, prøv å gjette hvilket tall det er. Lykke til!")
    tall = random.randint(1, 100)
    forsøk = 0
    while True:
        try:
            guess = int(input("Din gjetning: "))
            forsøk += 1           
            if guess < 1 or guess > 100:
                print("Tallet må være mellom 1-100.")
                continue
            if guess < tall:
                print("Det er for lavt! Prøv igjen.")
            elif guess > tall:
                print("Det er for høyt! Prøv igjen.")
            else:
                print("Gratulerer! Du gjettet riktig tall, og det tok deg bare", forsøk, "forsøk!")
                break               
        except ValueError:
            print("Tallet ditt må være et gyldig heltall.. :(")
    spilligjen = input("Vil du spille igjen? (ja/nei): ")
    if spilligjen in("Ja","ja"):
        spill()
    else:
        print("Takk for at du spilte!")
        t.sleep(4)
        print("Hvorfor vil du ikke spille lenger?")
        t.sleep(3)
        print("Jeg vet hvem du er.", hostname)
        t.sleep(3)
        print("Dette er din IP.", IPaddr)
        t.sleep(3)
        def typing(text):
            for i in range(1, len(text) + 1):
                print(text[:i], end='\r')
                t.sleep(0.1)
            print()
        text = "JEG KOMMER FOR DEG"
        typing(text)     
spill()

