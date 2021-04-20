class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index, num in enumerate(nums):
            if target - num not in d:
                d[num] = index
            else:
                return [index, d[target - num]]