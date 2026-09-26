class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        one, two=cost[0], cost[1]
        for i in range(2,len(cost)):
           current = cost[i] + min(one,two) 
           one = two 
           two = current
        return min(one,two)   
