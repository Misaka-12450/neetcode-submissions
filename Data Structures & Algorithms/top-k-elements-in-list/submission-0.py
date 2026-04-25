class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        len_nums = len(nums)
        buckets = [[] for _ in range(len_nums + 1)]

        for num in nums:
            freqs[num] += 1

        for num, freq in freqs.items():
            buckets[freq].append(num)

        result = []
        j = 0
        print(buckets)

        for i in range(len_nums, 0, -1):
            for num in buckets[i]:
                if not j < k:
                    return result
                j += 1

                result.append(num)

        print(result)
        return result
