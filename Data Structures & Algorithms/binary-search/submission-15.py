class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bin_search(nums, target, left, right):
            middle = (left + right) // 2

            while left <= right:
                num = nums[middle]
                if num == target:
                    return middle
                elif num < target:
                    # Right
                    return bin_search(nums, target, middle + 1, right)
                elif num > target:
                    # Left
                    return bin_search(nums, target, left, middle - 1)

            return -1

        return bin_search(nums, target, 0, len(nums) - 1)
