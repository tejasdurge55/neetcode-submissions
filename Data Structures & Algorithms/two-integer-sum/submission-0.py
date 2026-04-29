class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)-1,1):
            print(i)
            sub_num=target-nums[i]
            for j in range(i+1,len(nums),1):
                print("j: "+str(j))
                if (sub_num==nums[j]):
                    return [i,j]