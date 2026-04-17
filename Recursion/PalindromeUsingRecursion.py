class Solution:    
    def palindromeCheck(self, s):
        n = len(s)
        def helper(i):
            if i >= n//2:
                return True
            if s[i] != s[n - i - 1]:
                return False
            return helper(i + 1)
        return helper(0)    
s = input().strip()
obj=Solution()
print(obj.palindromeCheck(s))
     