class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_s = ''

        for s in strs:
            s_len = len(s)
            encoded_s += str(s_len) + '#' + s
        
        return encoded_s


    def decode(self, s: str) -> List[str]:
        i = 0
        decoded_s = []

        while i < len(s):
            j = i
            s_len = []

            while s[j] != '#':
                s_len.append(s[j])
                j += 1
            
            s_len = int(''.join(s_len))
            decoded_s.append(s[j+1:j+1+s_len])

            i = j+1+s_len
        
        return decoded_s
