class Solution:
    def SumOfDigits(self, n):
        total = 0
        while n>0:
            digit = n%10
            total+=digit
            n=n//10
        return total
n = int(input())
obj = Solution()
print(obj.SumOfDigits(n))