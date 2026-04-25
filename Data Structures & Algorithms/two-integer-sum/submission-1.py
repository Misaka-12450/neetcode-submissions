class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {} # Stores index of a number

        for index, num in enumerate(nums):
            if (diff := target - num) in num_map.keys():
                return [num_map[diff], index]
            num_map[num] = index

        return []
        