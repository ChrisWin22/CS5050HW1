import time
import matplotlib.pyplot as plt

def nim2(n):
    if n == 0:
        return True
    if n == 1:
        return False
    return not(nim2(n-1) and nim2(n-2))

def timeFunction2(n):
    start = time.time()
    nim2(n)
    return time.time() - start


def nim(n, array, boolArray):
    if n == 0:
        return True
    if n == 1:
        return False
    if boolArray[n] != None:
        return boolArray[n]
    return not(nim(n-1, array, boolArray) and nim(n-2, array, boolArray))

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
        if nim2(stones - 1) and stones > 1:
            print("Computer took 2 stones")
            stones = stones - 2
        else:
            print("Computer took 1 stones")
            stones = stones - 1
        print("There are " + str(stones) + " stones left")

def timeFunction(n, array, boolArray):
    start = time.time()
    boolArray[n] = nim(n, array, boolArray)
    return time.time() - start

#stonesToPlayWith = int(input("Max number of stones you want to play with: "))
#play(stonesToPlayWith)

def createTimeArray2():
    array = []
    n = 0
    while True:
        timeToComplete = timeFunction2(n)
        print (timeToComplete)
        if timeToComplete > 600:
            array.append(timeToComplete)
            return array
        else:
            array.append(timeToComplete)
            n = n + 1



def createTimeArray():
    array = []
    boolArray = []
    memArray = []
    n = 0
    while True:
        boolArray.append(None)
        timeToComplete = timeFunction(n, memArray, boolArray)
        boolArray[n] = True
        memArray.append(timeToComplete)
        if n > 61:
            array.append(timeToComplete)
            return array
        else:
            print (memArray[n])
            array.append(timeToComplete)
            n = n + 1

print("Booting Up...")
arrayOfTimes = createTimeArray()
length = len(arrayOfTimes)
print (length)
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







