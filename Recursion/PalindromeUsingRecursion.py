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

# Input:
# s = "madam"

# n = 5

# Call:
# helper(0)

# ---------------------------------

# helper(0):
# i = 0
# s[0] == s[4] → m == m → True
# Call helper(1)

# ---------------------------------

# helper(1):
# i = 1
# s[1] == s[3] → a == a → True
# Call helper(2)

# ---------------------------------

# helper(2):
# i = 2
# i >= n//2 → 2 >= 2 → True
# Return True

# ---------------------------------

# Backtracking:

# helper(2) → True
# helper(1) → True
# helper(0) → True

# ---------------------------------

# Final Output:
# True     