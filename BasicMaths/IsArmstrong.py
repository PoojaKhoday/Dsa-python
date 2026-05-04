class Solution:
    def isArmstrong(self, n):
        sum = 0
        num = n
        while(n>0):
            ld = n%10
            sum = sum + (ld*ld*ld)
            n = n//10
        if num == sum:
            return True
        else:
            return False
n = int(input())  
obj = Solution()
print(obj.isArmstrong(n))

#sample i/p & o/p
# 153 ((1^3 + 5^3 + 3^3 = 153))
# True
