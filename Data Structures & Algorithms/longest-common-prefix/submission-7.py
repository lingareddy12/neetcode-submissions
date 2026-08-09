class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        first_str=strs[0]
        for i in range(len(first_str)): 
            for string in strs[1:]:
                if i>=len(string):
                    return first_str[:i]
                if i<len(string) and string[i]!=first_str[i]:
                    return first_str[:i]

        return first_str
                

        