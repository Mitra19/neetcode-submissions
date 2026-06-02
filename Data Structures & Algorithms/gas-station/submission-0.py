class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        start = 0
        remain_cost = 0
        for i in range(len(gas)):
            remain_cost += (gas[i] - cost[i])
            if remain_cost < 0:
                start = i + 1
                remain_cost = 0
        return start