#To Print the Star * Pattern in 1 to 5 

# def pyPattern(n):
#     for i in range(0, n):
#         for j in range (0, i + 1):
#                 print ("* "   , end = " ")
#         print("\r")

# n=10
# pyPattern(n)



count = int(input('enter ur number:'))

# for value in range(count):
#     print(' *' * (value + 1))

# for value in range(count):
#     print(' *' * (count - value))

for value in range(count):
    print(' ' * ( count - value - 1 ) + ' *' * (value + 1))
count = count - 1
print("Hi")
for value in range(count):   
    print( ' ' *(value + 1)  + ' *' * (count - value))   #5  #1
    
    # print(         "     *" )  
    # print(         "    **" )
    # print(         "   ***" )   
