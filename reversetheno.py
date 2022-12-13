#To Reverse the Number 54321

#In Mathematical be default we divided the value like 54321 % 10 means we got the result of the last digit no

#The % symbol in Python is called the Modulo Operator. 
#It returns the remainder of dividing the left hand operand by right hand operand. It's used to get the remainder of a division problem.

#Logic



# num = 54321
# one = num % 10 
# two = one + one  
# three = two + one 
# four = three + one
# five = three + two
# print(one,two,three,four,five)
# # print(five)
# # print(four)
# # print(three)
# # print(two)
# # print(one)

# num = 54321
# f_d = num // 10
# print(f_d)

#Method 1

# number = 54321
# revers_number = 0  
# while(number >= 10):
#     remainder = number % 10 
#     revers_number = (revers_number * 10 ) + remainder 
#     number = number // 10   # // => Floor Division operator Returns the Quotient Value   
#     # print(number)
# else:
#     revers_number = (revers_number * 10 ) + number 

# print(revers_number)



#Method 2
#import pdb

number = 54321
revers_number = 0 # First Initialize the revers_number = 0  
while(number > 0): 
    remainder = number % 10 # Iteration 1 54321 % 10 => 1  
    # print(remainder)
    revers_number = (revers_number * 10 ) + remainder # revers_number => 1
    # print(revers_number)
    number = number // 10   # // => Floor Division operator Returns the Quotient Value    

print(revers_number)







