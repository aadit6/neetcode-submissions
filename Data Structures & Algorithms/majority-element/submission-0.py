from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for x in nums:
            counts[x] += 1
            if counts[x] > len(nums) // 2:
                return x