class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longprefix=""

        for i in range(len(min(strs))): 
            ith_char=strs[0][i]
            for j in strs[1:]:
                while(j[i]!=ith_char):
                    return longprefix
            longprefix+=ith_char
        return longprefix
                

        