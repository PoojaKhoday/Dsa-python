class Solution:
    def Pattern7(self, n):
        for i in range(n):
            for j in range(n-i):
                print(" ",end = " ")
            for j in range(2*i+1):
                print("*",end = " ") 
            for j in range(n-i):
                print(" ",end = " ")    
            print()
n = int(input())
obj = Solution()
obj.Pattern7(n)