class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a=len(nums)
        set_a=set(nums)
        if (len(set_a)==a):
            return False
        else:
            return True