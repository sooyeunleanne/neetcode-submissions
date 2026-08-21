class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        # store sorted_string : [list of anagrams] format
        for string in strs:
            sorted_string = str(sorted(string))
            anagrams.setdefault(sorted_string, []).append(string)
        
        return list(anagrams.values())