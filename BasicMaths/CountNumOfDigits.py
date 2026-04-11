class Solution:
    def countDigit(self, n):
        count = 0
        while (n>0):
            lastdigit = n%10
            count += 1
            n = n//10
        return count            
n = int(input())  
obj = Solution()
print(obj.countDigit(n))
        