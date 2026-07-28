class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        anchor = 0
        search = 0

        while True:
            while search < len(nums) and nums[search] == val:
                search += 1
            
            if search >= len(nums):
                break
                
            nums[anchor] = nums[search]
            search += 1
            anchor += 1

        return anchor

