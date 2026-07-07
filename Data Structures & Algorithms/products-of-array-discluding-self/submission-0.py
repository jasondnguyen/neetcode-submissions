class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for i in range(len(nums))]
        suffix = [1 for i in range(len(nums))]

        [1,2,4,6]
        [1,1,2,8]
        [48,24,6,1]
        
        for i in range(len(nums)-1):
            prefix[i+1] = nums[i] * prefix[i]

        for i in range(len(nums)-1, 0, -1):
            suffix[i-1] = nums[i] * suffix[i]

        return [suffix[i] * prefix[i] for i in range(len(nums))]