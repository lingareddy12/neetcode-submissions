class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        res=""
        l,r=0,0
        while l<len(word1) and r<len(word2):
            res=res+word1[l]+word2[r]
            r=r+1
            l=l+1
        
        while(l<len(word1)):
            res=res+word1[l]
            l=l+1

        while(r<len(word2)):
            res=res+word2[r]
            r=r+1
        
        return res
        

        