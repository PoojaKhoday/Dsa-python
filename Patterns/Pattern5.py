class Solution:
    def Pattern5(self, n):
        for i in range(n):
            for j in range(n - i):
                print("*", end = " ")
            print()
n = int(input())
obj = Solution()
obj.Pattern5(n)