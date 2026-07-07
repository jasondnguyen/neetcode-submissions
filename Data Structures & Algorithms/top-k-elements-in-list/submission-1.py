import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {}

        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1
        
        max_heap = []

        for i, freq in num_freq.items():
            heapq.heappush_max(max_heap, (freq, i))
        
        res = []
        
        for i in range(k):
            res.append(heapq.heappop_max(max_heap)[1])
        
        return res