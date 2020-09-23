def hello():
    print ("Hi there!")
    print("I'm a function")

print("Good morning!")    
print("Welcome to class.")

hello()

print("And now we are done!!!")


def hi():
    print("Hello there!")

def goodbye():
    print("See ya!")

hi()
goodbye()    




name = "Obama"

def showname():
     print("Function: ", name)

print("Main program: ", name)     

showname()


def show_name():
    global name
    print("Function 1:", name)
    name = 'John'
    print("Function 2:", name)

print("Main program 1:", name)   

show_name()

print("Main program 2:", name)