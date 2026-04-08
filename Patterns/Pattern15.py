class Solution:
    def Pattern15(self,n):
        for i in range(1,n+1):
            for j in range(n-i+1):
                print(chr(65+j), end = " ")
            print()
n = int(input()) 
obj = Solution()
obj.Pattern15(n)                                      