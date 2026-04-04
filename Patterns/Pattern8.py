class Solution:
    def Pattern8(self, n):
        for i in range(n):
            for j in range(i):
                print(" ",end = " ")
            for j in range(2*n - (2*i+1)):
                print("*",end = " ") 
            for j in range(i):
                print(" ",end = " ")    
            print()
n = int(input())
obj = Solution()
obj.Pattern8(n)