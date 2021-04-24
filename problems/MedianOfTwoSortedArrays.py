class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        center = len(merged) // 2
        if len(merged) % 2 == 0:
            return (merged[center] + merged[center - 1]) / 2
        else:
            return merged[center]
