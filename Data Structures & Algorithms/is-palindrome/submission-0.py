class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_s="abcdefghijklmnopqrstuvwxyz"
        valid_s=valid_s+valid_s.upper() + "0123456789"

        new_s=""
        for i in s:
            if i in valid_s:
                new_s=new_s+i.lower()
        
        l=0
        r=len(new_s)-1
        while(l<=r):
            if new_s[l]!=new_s[r]:
                return False
            l=l+1
            r=r-1

        return True
        