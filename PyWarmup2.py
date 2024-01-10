#get number of classes you are taking and converts them to an integer
numOfClasses = int(input('How many classes are you taking this semester?'))

classes = [] #List

#Loops while numOfClasses is greater than 0 and asks the user to input class names
while numOfClasses > 0:
    ClassName = input("What are the class names?")
    classes.append(ClassName) #appends to List
    numOfClasses -= 1
    

print("\nThe classes you are taking are:")
#iterate over classes list and print its content 'x'
for x in classes:
    print(x)



"""
# initialize an empty array
classesTaken = []

# Grab class count from user input, string -> int -> range so we can iterate over that.
for classTaken in range(int(input("How many classes are you taking this semester? "))):
    # grab class name
    localClass = input("Enter the name of your class: ")
    # add class name to array
    classesTaken.append(localClass)

print("The classes you are taking are:")

# print out the class name by iterating over the array
for className in classesTaken:
    print(className)
    
    Josh Mathhews better code for reference
"""
















