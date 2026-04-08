class Solution:
    def Pattern14(self,n):
        for i in range(1,n+1):
            for j in range(i):
                print(chr(65+j), end = " ")
            print()
n = int(input()) 
obj = Solution()
obj.Pattern14(n)                   

                    