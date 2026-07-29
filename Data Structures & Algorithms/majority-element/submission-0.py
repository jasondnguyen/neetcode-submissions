from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_freq = defaultdict(int)

        for num in nums:
            num_freq[num] += 1
        
        majority = [0,0]

        for num, freq in num_freq.items():
            if freq > majority[1]:
                majority = [num, freq]
        
        return majority[0]