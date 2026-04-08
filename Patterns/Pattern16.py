class Solution:
    def Pattern16(self,n):
        for i in range(1,n+1):
            for j in range(i):
                print(chr(65+i-1), end = " ")
            print()
n = int(input()) 
obj = Solution()
obj.Pattern16(n)                                      