class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxi = float('-inf')
        i = 0
        j = 0
        sum = 0
        while j < len(nums):
            sum = sum + nums[j]
            if j - i + 1 < k:
                j += 1
            elif j - i + 1 == k:
                avg = sum/k
                maxi = max(maxi,avg)
                sum = sum - nums[i]
                j += 1
                i += 1
        return maxi            
