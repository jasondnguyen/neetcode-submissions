from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)

        for s in strs:
            sorted_s = sorted(s)
            anagram_dict[''.join(sorted_s)].append(s)
        
        return list(anagram_dict.values())

