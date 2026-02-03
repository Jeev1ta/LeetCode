def occ(haystack, j, needle, k):
    if k == len(needle):
        return 0
    if j >= len(haystack) or haystack[j] != needle[k]:
        return -1
    return occ(haystack, j + 1, needle, k + 1)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                occr = occ(haystack, i+1, needle, 1)
                if occr != -1:
                    return i
        return -1