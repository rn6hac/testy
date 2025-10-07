class Solution:
    def are_anagrams(self, str1: str, str2: str) -> bool:
        str1 = str1.replace(" ", "").lower()
        str2 = str2.replace(" ", "").lower()
        return sorted(str1) == sorted(str2)


solution = Solution()
result1 = solution.are_anagrams("listen", "silent")
result2 = solution.are_anagrams("hello", "world")
print(result1)
print(result2)
