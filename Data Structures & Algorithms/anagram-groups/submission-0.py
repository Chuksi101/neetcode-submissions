class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = defaultdict(list)
        result = []
        for word in strs:
            sortedWord = "".join(sorted(word))
            store[sortedWord].append(word)
        for key in store:
            result.append(store[key])

        return result