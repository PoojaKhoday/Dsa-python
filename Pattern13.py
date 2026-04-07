class Solution:
    def Pattern13(self,n):
        num = 1
        for i in range(n):
            for j in range(i+1):
                print(num, end = " ")
                num = num+1
            print()
n = int(input()) 
obj = Solution()
obj.Pattern13(n)                   

                    