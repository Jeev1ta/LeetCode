class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        start = nums.index(target)
        end = start
        while end < len(nums) and nums[end] == target:
            end += 1
        return [start, end-1]