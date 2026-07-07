class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            s_len = len(s)
            res += f'{s_len}#{s}'
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            s_len = ''

            while j < len(s) and s[j] != '#':
                s_len += s[j]
                j += 1

            s_len = int(s_len)
            res.append(s[j+1:j+s_len+1])
            i = j + s_len + 1
        
        return res