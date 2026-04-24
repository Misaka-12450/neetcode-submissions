class Solution:
    def search(self, nums: List[int], target: int) -> int:
        len_nums = len(nums)
        
        if len_nums == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        
        middle = len_nums // 2
        num_middle = nums[middle]
        if num_middle == target:
            return middle
        elif num_middle > target:
            # Target in the left?
            if (index := self.search(nums[:middle], target)) != -1:
                return index
        elif num_middle < target:
            # Target in the right?
            if (index := self.search(nums[middle:], target)) != -1:
                return index + middle

        # Oops
        return -1