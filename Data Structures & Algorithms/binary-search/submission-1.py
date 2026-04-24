class Solution:
    def search(self, nums: List[int], target: int) -> int:
        len_nums = len(nums)

        if len_nums == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        middle = len_nums // 2

        if nums[middle] == target:
            return middle
        
        left = nums[:middle]
        print(left)
        right = nums[middle:]
        print(right)
        index = -1

        if (index := self.search(left, target)) != -1:
            return index
        
        if (index := self.search(right, target)) != -1:
            return index + middle
        
        return -1