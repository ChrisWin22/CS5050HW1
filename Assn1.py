import time
import matplotlib.pyplot as plt


def nim(n):
    if n == 0:
        return True
    if n == 1:
        return False
    return not(nim(n-1) and nim(n-2))

def play(stones):
    while stones >= 0:
        if stones == 0:
            print("You Won!")
            break
        stonesToTake = int(input("How many stones will you take: "))
        stones = stones - stonesToTake
        if stones == 0:
            print("The computer won...")
            break
        if nim(stones - 1) and stones > 1:
            print("Computer took 2 stones")
            stones = stones - 2
        else:
            print("Computer took 1 stones")
            stones = stones - 1
        print("There are " + str(stones) + " stones left")

def timeFunction(n):
    start = time.time()
    nim(n)
    return time.time() - start

#stonesToPlayWith = int(input("Max number of stones you want to play with: "))
#play(stonesToPlayWith)

def createTimeArray():
    array = []
    boolArray = []
    memArray = []
    n = 0
    while True:
        if(boolArray[n] == True):
            timeToComplete = memArray[n]
        else:
            timeToComplete = timeFunction(n)
            boolArray[n] = True
            memArray[n] = timeToComplete
        if timeToComplete > 5:
            array.append(timeToComplete)
            return array
        else:
            array.append(timeToComplete)
            n = n + 1

print("Booting Up...")
arrayOfTimes = createTimeArray()
length = len(arrayOfTimes)
x = []
i = 0
while i < length:
    x.append(i)
    i = i + 1
plt.plot(x, arrayOfTimes)
plt.yscale('log')
plt.xlabel('N-Values')
plt.ylabel('Time To Run')
plt.title('Nim Run Times')
plt.show()







