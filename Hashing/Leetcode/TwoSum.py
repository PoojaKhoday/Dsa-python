from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1 , len(nums)):
                if nums[i] + nums[j] == target:
                    return[i, j]
nums = list(map(int, input().strip('[]').split(',')))
target = int(input())
obj = Solution()
print(obj.twoSum(nums,target))

#sample input & output
#[1,2,3,4]
#3
#[0, 1]