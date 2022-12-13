#To print the * Pattern in Reverse 

#import pdb
def patternReverse(n):
    for i in range(n, 0, -1):
            for j in range(0, i):
                print("* ",  end="")

            print("\n")

#pdb.set_trace()
n=5

patternReverse(n)