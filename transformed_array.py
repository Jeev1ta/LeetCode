class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [0] * length
        for i in range(length):
            if nums[i] == 0:
                result[i] = nums[i]
            else:
                result[i] = nums[(i + nums[i]) % length]
        return result