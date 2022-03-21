import random

def getFakeTemp():
    return random.randrange(10, 30)

def getFakeHumi():
    return random.randrange(0, 100)

def getFakeLumi():
    return random.randrange(0, 1)

#BigList = ["phone", "tablet", "laptop", "Desktop", "Smart TV", "AEMI", "headphone", "keyboard", "mouse", "projector", "printer", "speaker", "spy camera", "car", "air conditioner", "smart fridge", "smart window", "smart oven", "smart coffe machine"]

def getFakeBlueList():
    fakeList = []
    BigList = ["phone", "tablet", "laptop", "Desktop", "Smart TV", "AEMI", "headphone", "keyboard", "mouse", "projector", "printer", "speaker", "spy camera", "car", "air conditioner", "smart fridge", "smart window", "smart oven", "smart coffe machine"]
    num = random.randint(2, 5)
    for i in range(num):
        j = random.choice(BigList)
        fakeList.append(j)
        BigList.remove(j)
    return fakeList