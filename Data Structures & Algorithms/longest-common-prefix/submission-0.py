class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        i = 0

        while True:
            if i < len(strs[0]):
                prefix += strs[0][i]
            else:
                break

            for j in range(len(strs)):
                if i >= len(strs[j]) or strs[j][i] != prefix[-1]:
                    return prefix[:len(prefix)-1]
            
            i += 1
            
        return prefix