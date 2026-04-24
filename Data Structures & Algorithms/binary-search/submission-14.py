class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(nums: List[int], target: int, left: int, right: int):
            len_nums = right - left

            if len_nums <= 2:
                if nums[left] == target:
                    return left
                elif len_nums == 2 and nums[right - 1] == target:
                    return right - 1
                else:
                    return -1

            middle = left + len_nums // 2
            num_middle = nums[middle]
            if num_middle == target:
                return middle
            elif num_middle > target:
                return binary_search(nums, target, left, middle)
            elif num_middle < target:
                return binary_search(nums, target, middle + 1, right)
                

            # Oops
            return -1

        return binary_search(nums, target, 0, len(nums))
