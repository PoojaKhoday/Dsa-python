class Solution:
    def Pattern12(self,n):
        for i in range(1,n+1):
            #num
            for j in range(1, i+1):
                print(j, end = " ")
            #space
            for j in range(4 * (n - i)):
                print(" ", end = "")
            #num
            for j in range(i,0,-1):
                print(j, end = " ")
            print()
n = int(input()) 
obj = Solution()
obj.Pattern12(n)                   

#sample input & output
# 5
#1                 1 
#1 2             2 1 
#1 2 3         3 2 1 
#1 2 3 4     4 3 2 1 
#1 2 3 4 5 5 4 3 2 1                     