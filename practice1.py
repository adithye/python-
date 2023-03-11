
# country and its population dictionary
popDict={}

def printDict():
    print(popDict)

def addDict():
    country = input('Enter the country')
    if country in popDict.keys():
        print('Country Exists in Dictionary')
    else:
        population = int(input('Enter the population'))
        popDict.update({country: population})
        printDict()

def remDict():
    country = input('Enter the country')
    if country in popDict.keys():
        del popDict[country]
        printDict()


while True:
    n = int(input('choose options \n1. PRINT \n2.ADD  \n3.REMOVE \n'))
    match n:
        case 1:
            printDict()
        case 2:
            addDict()
        case 3:
            remDict()
    tryAgain = input("if you want to continue: yes/no")
    if tryAgain == 'no':
        break

