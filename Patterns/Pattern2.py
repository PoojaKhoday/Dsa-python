class Solution:
    def pattern1(self, n):
        for i in range(n):
            for j in range(i+1):
                print("*", end="")
            print() 
#n = 7  
n = int(input())
obj = Solution()
obj.pattern1(n)