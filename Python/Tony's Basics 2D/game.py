import random
import time

loading_time = 0
loading_bar_visual = [""]
loading = True

while loading:
    while loading % 10 == 0:
        loading_bar_visual.append("#")
    loading_time += random.randint(1,16)
    print(f"{loading_time}%     {loading_bar_visual}")
    time.sleep(random.randint(1,3)/random.randint(1,6))

    if loading_time >= 100:
        loading_time = 100
        loading = False