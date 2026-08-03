class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        # prefix = [1,1,2,4]
        # suffix = [48,24,6,1]

        for i in range(len(nums)-1):
            prefix[i+1] *= prefix[i] * nums[i]
        
        for i in range(len(nums)-1, 0, -1):
            suffix[i-1] = suffix[i] * nums[i]
        
        print(prefix)


        return [prefix[i] * suffix[i] for i in range(len(nums))]