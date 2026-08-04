class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set()
        longest_sequence = 0

        for num in nums:
            num_set.add(num)
        
        for num in num_set:
            if num-1 in num_set:
                continue

            running = 1
            while num+1 in num_set:
                running += 1
                num += 1
        
            longest_sequence = max(running, longest_sequence)
        
        return longest_sequence