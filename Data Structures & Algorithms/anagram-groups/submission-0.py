import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words_dict = collections.defaultdict(list)
        for word in strs:
            sorted_w = ''.join(sorted(word))
            words_dict[sorted_w].append(word)
        return list(words_dict.values())