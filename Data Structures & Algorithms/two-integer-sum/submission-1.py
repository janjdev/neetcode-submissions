class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}
        for index, num in enumerate(nums):
            pair = target - num
            if pair in pairs:
                return [pairs[pair], index]
            pairs[num] = index