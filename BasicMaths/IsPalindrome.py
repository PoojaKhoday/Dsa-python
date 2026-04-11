class Solution:
    def isPalindrome(self, n):
        rev = 0
        num = n
        while(n>0):
            ld = n%10
            rev = rev*10 + ld
            n = n//10
        if num == rev:
            return True
        else:
            return False
n = int(input())  
obj = Solution()
print(obj.isPalindrome(n))
        