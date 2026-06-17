class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # return max number of consecutive 1's
        count, max_ones = 0, 0
        for num in nums:
            if num == 0:
                count = 0
            elif num == 1:
                count+=1
                max_ones = max(max_ones, count)
        return max_ones