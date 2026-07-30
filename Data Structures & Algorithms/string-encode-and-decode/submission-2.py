class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_s = ""

        for s in strs:
            encoded_s += f"{len(s)}#{s}"
        
        return encoded_s

    def decode(self, s: str) -> List[str]:
        print(s)
        i = 0
        j = 0
        decoded_s = []

        while i < len(s) and j < len(s):
            while s[j] != '#':
                j += 1
            
            s_len = int(s[i:j])
            decoded_s.append(s[j+1:j+s_len+1])
            i = j + s_len + 1
            j = i
        
        return decoded_s
