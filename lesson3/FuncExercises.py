# Write a Python function 
# to sum all the numbers in a list

def sum(num1, num2, num3, num4, num5):
    sum = num1 + num2 + num3 + num4 + num5
    print(sum)

sum(8, 2, 3, 0, 7)    


# Write a Python function to multiply 
# all the numbers in a list

def multiply_nums():
    print(8*2*3*-1*7)

multiply_nums()    


# Write a function that accepts a
#restaurant check and a tip % 

def bill(total_amount):
    tip = 15/100* total_amount
    total_bill = (tip + total_amount)

#Print out the tip that should be
#left on the table as well as the
#total bill     

    # print(total_amount)
    # print(tip)
    print(total_bill)

bill(12)      


# If the tip is less than 15% you
#should tell the user that they
#might want to leave a little
#more on the table 
