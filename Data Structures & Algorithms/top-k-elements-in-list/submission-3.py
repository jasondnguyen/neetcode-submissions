import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = defaultdict(int)

        for num in nums:
            freq_dict[num] += 1
        
        min_heap = []

        for num, freq in freq_dict.items():
            print(num, freq)
            if len(min_heap) < k:
                heapq.heappush(min_heap, (freq, num))
            else:
                if freq > min_heap[0][0]:
                    heapq.heappushpop(min_heap, (freq,num))

        return [num for _, num in min_heap]

