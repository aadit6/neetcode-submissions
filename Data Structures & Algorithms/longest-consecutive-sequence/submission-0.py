class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(nums) # O(n * logn). Doing naive solution first
        maxCon = [1]
        for i in range (1, len(nums)):
            if nums[i] == nums[i-1]:
                continue #skip dupes
            if nums[i] == nums[i-1] + 1:
                maxCon[-1] += 1
            else:
                maxCon.append(1)     
        return max(maxCon)