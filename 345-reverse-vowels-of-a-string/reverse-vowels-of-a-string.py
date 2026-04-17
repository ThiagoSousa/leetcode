class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u"]
        s = [c for c in s]
        order_vowels = [c for c in s if c.lower() in vowels]
        index = -1
        for i in range(len(s)):
            if s[i].lower() in vowels:
                s[i] = order_vowels[index]
                index -= 1
        return "".join(s)