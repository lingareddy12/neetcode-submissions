class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
    
        alphs=[0 for i in range(26)]
        for i in range(len(s)):
            alphs[ord(s[i])-ord('a')]+=1
            alphs[ord(t[i])-ord('a')]-=1
        
        for i in alphs:
            if i!=0:
                return False
        return True
        

        


        
        