from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort_dict = defaultdict(list)

        for s in strs:
            sort_dict[''.join(sorted(s))].append(s)
        
        return list(sort_dict.values())
