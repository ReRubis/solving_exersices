from curses.ascii import SP


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged_array = nums1 + nums2
        summ = 0
        count = 0
        for i in merged_array:
            summ = summ + i 
            count = count + 1
        return summ/count

incurso = Solution
answer = incurso.findMedianSortedArrays(Solution,[1,2,5],[1,2,3])
print(answer)