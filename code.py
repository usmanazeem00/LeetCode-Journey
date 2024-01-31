class Solution(object):
    def twoSum(self, nums, target):
        rtype=[]
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(nums)-1):
            for j in range(1,len(nums)):
                if i!=j and nums[j]+nums[i]==target:
                    rtype=[i,j]
                    break
        return rtype

sol=Solution()
sol.twoSum([1,2,3],3)
