class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a signature for each word, store that signature as a key
        # in a dict and the words that match stored in an array that is the value
        ana_group = {}

        for word in strs:
            sig = [0] * 26
            for char in word:
                sig[ord(char) -97] += 1
            signature = tuple(sig)
            if signature in ana_group:
                ana_group[signature].append(word)
            else: ana_group[signature] = [word]
        return list(ana_group.values())
