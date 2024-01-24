from datetime import datetime # Allows the use of dates and time

print('Hello! Please Enter your name and Month that you were born in.')


# get name and birth month.
Name = input("Name:")
BirthMonth = input("Month:\n")
nameLen = len(Name)
today = datetime.now()
monthName = today.strftime("%B")# converts datetime original format to month into string format time. Website docs help: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes


print(f"Hello, {Name}\n")
print(f"Happy birthday {monthName}!\n")
print(f"name length {nameLen}\n")

if BirthMonth == monthName:
    print(f"Your birthday is in {BirthMonth} {Name} with {nameLen} letters? Happy Birthmonth!!")
else:
    print(f"Birth month not the same as current month. I'm afraid it's not your birthmonth {Name}. Name length is {nameLen}... Oops.")


