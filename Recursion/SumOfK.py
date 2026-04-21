class Solution:
    def SumOfK(self, i, ds, s, arr, target, n):
        if i == n:
            if s == target:
                print(ds)
            return

        # PICK
        ds.append(arr[i])
        s += arr[i]
        self.SumOfK(i + 1, ds, s, arr, target, n)

        # BACKTRACK
        ds.pop()
        s -= arr[i]

        # NOT PICK
        self.SumOfK(i + 1, ds, s, arr, target, n)


# Input
n = int(input())
arr = list(map(int, input().split()))
target = int(input())

obj = Solution()
obj.SumOfK(0, [], 0, arr, target, n)