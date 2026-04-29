class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sub_num=0
        for i in range(0,len(nums)-1,1):
            sub_num=target-nums[i]
            for j in range(i+1,len(nums),1):
                if (sub_num==nums[j]):
                    return [i,j]