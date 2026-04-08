class Solution:
    def Pattern17(self, n):
        for i in range(n):

            # spaces
            for j in range(n - i - 1):
                print(" ", end=" ")

            # increasing part
            for j in range(i + 1):
                print(chr(65 + j), end=" ")

            # decreasing part
            for j in range(i - 1, -1, -1):
                print(chr(65 + j), end=" ")

            print()

n = int(input())
obj = Solution()
obj.Pattern17(n)