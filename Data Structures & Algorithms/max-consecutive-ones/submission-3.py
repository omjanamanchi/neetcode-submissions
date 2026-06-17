class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = consecutiveOnes = 0
        for num in nums:
            if num == 1:
                count+=1
                consecutiveOnes = max(count, consecutiveOnes)
            else:
                count = 0
        return consecutiveOnes