def square(num):
    print(num*3) # that is num times 3

square(5)    


def square(num):
    print(num**3) # that is num raised to poer 3

square(5)    


def average(num1, num2, num3):
    sum = num1 + num2 + num3
    avg = sum/3
    print(sum)
    print(avg)

average(50, 100, 150)# meaning num1 is 50, 
                     # num2 100 and 
                     # num3 150


def change_me(v):
    print("Function got:", v)
    v = 10
    print("argument is now:", v)

change_me(10)    
