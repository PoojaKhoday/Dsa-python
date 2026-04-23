class Solution:
    def SumOfK(self, i, s, arr, target, n):
        if i == n:
            if s == target:
                return 1
            return 0

        take = self.SumOfK(i + 1, s + arr[i], arr, target, n)

        not_take = self.SumOfK(i + 1, s, arr, target, n)

        return take + not_take


n = int(input())
arr = list(map(int, input().split()))
target = int(input())

obj = Solution()
print(obj.SumOfK(0, 0, arr, target, n))