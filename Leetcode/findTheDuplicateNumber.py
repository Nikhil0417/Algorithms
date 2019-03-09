class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        occurence = 0
        # if(len(nums)<=1):
        #     return 0
        while(i<len(nums)):
            if(occurence & (1<<nums[i])):
                return nums[i]
            else:
                occurence |= 1<<nums[i]
                i +=1
