class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        existing = {}
        for num in nums:
            if existing.get(num):
                return True
            existing[num] = True
        return False