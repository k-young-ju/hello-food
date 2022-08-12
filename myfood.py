import random
#화면에 음식리스트를 출력을 하는 기능
def print_list(foodlist):
    str = ""
    for i, food in enumerate(foodlist):
        print(f"{i+1}. {food}")
        str = str + f"{i+1}. {food}  "
    print(str)

# 음식 리스트중 하나를 추천해주는 기능
def print_random(foodlist):
    for i in range(5) : 
        food = random.choice(foodlist)
        print(f"{i+1}. {food}")