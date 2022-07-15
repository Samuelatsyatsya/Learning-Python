
print("A PROGRAM TO DISPLAY YOUR YEAR OF BIRTH")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
current = 2022

def sub():
    return(current - age)
print("Hello, " +name, "You were born in the year" ,sub())
