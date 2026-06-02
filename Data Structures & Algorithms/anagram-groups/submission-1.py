class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        result = []
        for word in strs:
            alphabet_set = [0] * 26
            for ch in word:
                alphabet_set[ord(ch) - ord('a')] += 1
            ans[tuple(alphabet_set)].append(word)
        for key, item in ans.items():
            result.append(item)
        return result
            
