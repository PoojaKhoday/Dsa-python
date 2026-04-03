class Solution:
    def Pattern4(self, n):
        for i in range(n):
            for j in range(i+1):
                print(i+1, end = " ")
            print()
n = int(input())
obj = Solution()
obj.Pattern4(n)