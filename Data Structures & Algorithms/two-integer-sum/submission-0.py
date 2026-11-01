class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}
        for index, num in enumerate(nums):
            pair = target - num
            if pair in pairs:
                return [min(pairs[pair], index),  max(index, pairs[pair])]
            pairs[num] = index