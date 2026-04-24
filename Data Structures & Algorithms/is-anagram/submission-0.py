class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sort_1=sorted(s)
        sort_2=sorted(t)
        if(sort_1==sort_2):
            return True
        else:
            return False