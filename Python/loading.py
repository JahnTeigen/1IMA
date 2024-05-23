import time
import random

#Sorting interface function
def InterfaceLoader():
    if hasLoaded == True:
        print(lineBreak)
        print("==JewSorter 6000000==")
        startSequence = input("Start (Yes/No): ")

        if startSequence == "Yes":
            locationSelection = input(" ")
            if locationSelection == "" or "":
                print("Loading...")
                time.sleep(random.randint(1,3))
                print("Error")
            else:
                print("Preparing...")
                time.sleep(1)
                for p in range(0, 50):


#---------------------------------------------------#
#Loading sequence
numSteps = random.randint(3, 23)
increment = 100 / numSteps
lineBreak = " "

for x in range(0, 101, numSteps):
    hasLoaded = False
    sleepDuration = random.randint(1, 9) / 10
    time.sleep(sleepDuration)
    print("Loading... ",x,"%")

hasLoaded = True
print("Finished!")
time.sleep(random.randint(2,3))
InterfaceLoader()