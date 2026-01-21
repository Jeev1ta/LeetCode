def findMedianSortedArrays(nums1, nums2):
        num = (nums1 + nums2)
        num.sort()
        if len(num) % 2 != 0:
            return (num[len(num)//2])
        else:
            return (num[len(num)//2 - 1] + num[len(num)//2])/2
        


print(findMedianSortedArrays([1,2], [3,4]))