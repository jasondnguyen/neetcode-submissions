class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        i= 0 

        while i < len(strs[0]):
            prefix += strs[0][i]
            print(prefix)
            for s in strs:
                print(s[:len(prefix)])
                if i > len(s) or prefix != s[:len(prefix)]:
                    return prefix[:len(prefix)-1]
            
            i += 1
        
        return prefix
