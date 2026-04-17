class Solution:
    def fib(self, n):
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)   
n = int(input())
obj=Solution()
for i in range(n+1):
    print(obj.fib(i), end = " ") 
