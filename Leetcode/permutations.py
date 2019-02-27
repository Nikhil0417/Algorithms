class Solution:
    def dfs(self, nums, path, res):
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                self.dfs(nums[:i]+nums[i+1:],path+[nums[i]], res)
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # ol = []
        # for i in range(len(nums)):
        #     #il = []
        #     ol.append(nums[i])
        #     print(ol)
        #     ol.append(self.permute(nums[i+1:]))
        #     #ol.append(il)
        # return ol
        res = []
        self.dfs(nums, [], res)
        return res
