'''def message():
    print ("Enter next value")
    
print ("We start here")
message()

print("The end is here")


def hi(name):
    print ("Hi,", name)
    
    
hi('María')


def hiAll(name1, name2):
    print("Hi", name2)
    print("Hi", name1)
    
hiAll("María", "Tohabanda")


def address(street, city, postalCode):
    print("You address is:", street, "St.", city, postalCode)
    
s = input("Street: ")
pc = input("Postal Code: ")
c = input("City: ")

address(s, c, pc)
'''


'''
def subtra(a,b):
    print(a-b)

    
subtra(a=5,b=2)
subtra(2,b=5)

'''

'''---- substra(a=2, 5) da error por tema de posición, python necesita que el parámetro de la derecha se asgine primero.'''

'''def multiply(a,b):
    return a *b

print (multiply(3,4))
'''

'''
def multiply(a, b):
    return 

print(multiply(5,4))
'''

'''
def wishes():
    print("My Wishes")
    return "Happy Birthdaay"

wishes()
'''

'''
def wishes():
    print ("My Wishes")
    return ("Happy Bithday")

print(wishes()) '''


'''

def hiEveryBody(myList):
    for name in myList:
        print("Hi,", name)
        
        
hiEveryBody(["Pepito", "William",154])'''

def createList(n):
    myList = []
    for i in range(n):
        myList.append(i)
    return myList

print(createList(100))













































