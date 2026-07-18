class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        vis=[]
        for m in range(0,len(strs),1):
            vis.append(0)
        final_list=[]
        for i in range(0,len(strs),1):
            if vis[i]==1:
                continue
            a=strs[i]
            list_a=[]
            list_a.append(a)
            if (i==len(strs)-1):
                final_list.append(list_a)
                break
            for j in range(i+1,len(strs),1):
                if vis[j]==1:
                    continue
                b=strs[j]
                c=("".join(sorted(a)))
                d=("".join(sorted(b)))
                if(c==d):
                    list_a.append(b)
                    vis[j]=1
            final_list.append(list_a)
        return(final_list)    