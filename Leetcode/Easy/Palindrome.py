class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = str(x)
        if a == a[::-1]:
            return True
        return False     
x = int(input())
obj = Solution()
print(obj.isPalindrome(x))      
  
#Time Complexity : O(n)
#Space Complexity : O(n)
