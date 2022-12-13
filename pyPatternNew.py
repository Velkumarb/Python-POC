# To Print the Star pattern 1 to 5 

def pyStarReverse(n):
    for i in range(0, n):      #n End      #Start Stop(-1) End
        for j in range(0, i+1):
            # print("* ", end="") 
            print(" *",  end="") 
            
        print("\r") 

n = 5
pyStarReverse(n)          
