import time

input("Input time: ")
input("Radius: ")

input("Confirm?: ")
print("Initialising...")

s=1000

time.sleep(1)
for i in range(1000):
    print("Detonating in:", s, "seconds.")
    s=s-1
    time.sleep(1)
