class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(nums: List[int], target: int, left: int, right: int):
            len_nums = right - left
            print(f"nums: {nums[left:right]}, left: {left}, right: {right}")

            if len_nums <= 2:
                if nums[left] == target:
                    return left
                elif len_nums == 2 and nums[right - 1] == target:
                    return right - 1
                else:
                    return -1

            middle = left + len_nums // 2
            print(f"Middle: {middle}")
            num_middle = nums[middle]
            print(f"num_middle: {num_middle}")
            if num_middle == target:
                return middle
            elif num_middle > target:
                index = binary_search(nums, target, left, middle)
                print(f"Left. Index: {index}")
                # Target in the left?
                if index != -1:
                    return index
            elif num_middle < target:
                # Target in the right?
                index = binary_search(nums, target, middle + 1, right)
                print(f"Right. Index: {index}")
                if index != -1:
                    return index

            # Oops
            return -1

        return binary_search(nums, target, 0, len(nums))
