class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_counts = [0] * 26
        for c in chars:
            char_counts[ord(c) - ord('a')] += 1        
        result = 0
        for word in words:
            counts = char_counts.copy()
            for c in word:
                idx = ord(c) - ord('a')
                if counts[idx] > 0:
                    counts[idx] -= 1
                else:
                    break
            else:
                result += len(word)
        return result