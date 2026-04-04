class Solution:
    def Pattern6(self, n):
        for i in range(n):
            for j in range(n - i):
                print(j+1, end = " ")
            print()
n = int(input())
obj = Solution()
obj.Pattern6(n)