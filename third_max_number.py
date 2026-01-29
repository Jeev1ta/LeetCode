class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sorted_lst = []
        for i in nums:
            if i not in sorted_lst:
                sorted_lst.append(i)
        sorted_lst.sort()
        if len(sorted_lst) >= 3:
            return sorted_lst[-3]
        else:
            return max(sorted_lst)