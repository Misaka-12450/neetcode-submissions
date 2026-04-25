class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        result = []
        for i in range(len(nums)):
            product = None
            for j, num in enumerate(nums):
                if i != j:
                    if product == None:
                        product = num
                    else:
                        product *= num
            result.append(product)
            
        return result