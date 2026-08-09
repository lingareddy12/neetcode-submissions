class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        s_dicts={}
        for i,s in enumerate(strs):
            v=",".join(sorted(s))
            if v not in s_dicts:
                s_dicts[v]=[s]
            else:
                s_dicts[v]=s_dicts[v]+[s]

        res=[]
        for i in s_dicts.values():
            res.append(i)
        return res      
            
          

        



            

        