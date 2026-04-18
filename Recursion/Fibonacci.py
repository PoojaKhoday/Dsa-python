class Solution:
    def fib(self, n):
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)   
n = int(input())
obj=Solution()

for i in range(n+1):
    print(obj.fib(i), end = " ") 

# ctrl + / shortcut for comment 
# Input:
# n = 5

# Loop runs from i = 0 to 5

# ---------------------------------

# i = 0
# fib(0) = 0

# ---------------------------------

# i = 1
# fib(1) = 1

# ---------------------------------

# i = 2
# fib(2) = fib(1) + fib(0)
#        = 1 + 0
#        = 1

# ---------------------------------

# i = 3
# fib(3) = fib(2) + fib(1)
#        = (fib(1) + fib(0)) + 1
#        = (1 + 0) + 1
#        = 2

# ---------------------------------

# i = 4
# fib(4) = fib(3) + fib(2)
#        = 2 + 1
#        = 3

# ---------------------------------

# i = 5
# fib(5) = fib(4) + fib(3)
#        = 3 + 2
#        = 5

# ---------------------------------

# Final Output:
# 0 1 1 2 3 5     