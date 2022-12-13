#To Print the Pyramid Pattern 

n=5
for i in range(0, n):
        for s in range(-6, -i):
            print(" ", end=" " )
        for j in range(i+1):    
            print("* ", end=" ")
        print()



