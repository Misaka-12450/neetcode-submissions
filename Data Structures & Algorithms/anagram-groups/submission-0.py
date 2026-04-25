class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_letter_freq(s):
            chars = [0] * 26
            for c in s:
                i = ord(c.upper()) - 65 # ASCII
                chars[i] += 1
            return tuple(chars)
        
        anagrams = defaultdict(list)
        for s in strs:
            key = get_letter_freq(s)
            anagrams[key].append(s)

        return list(anagrams.values())

