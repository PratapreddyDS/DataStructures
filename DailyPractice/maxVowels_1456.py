import unittest

class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        count = 0

        vowels = ['a','e','i','o','u']

        for i in s[:k]:

            if i in vowels:
                count += 1

        temp = count

        for j in range(k,len(s)):

            if s[j] in vowels and s[j-k] in vowels:
                continue
            elif s[j] in vowels and s[j-k] not in vowels:
                temp += 1

            elif s[j] not in vowels and s[j-k] in vowels:
                temp -= 1

            count = max(count, temp)


        return count
            


class TestMaxVowels(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """
        Input: s = "abciiidef", k = 3
        Output: 3
        """
        self.assertEqual(self.solution.maxVowels("abciiidef", 3), 3)

    def test_example_2(self):
        """
        Input: s = "aeiou", k = 2
        Output: 2
        """
        self.assertEqual(self.solution.maxVowels("aeiou", 2), 2)

    def test_example_3(self):
        """
        Input: s = "leetcode", k = 3
        Output: 2
        """
        self.assertEqual(self.solution.maxVowels("leetcode", 3), 2)

    def test_no_vowels(self):
        """
        Input: s = "rhythms", k = 4
        Output: 0
        """
        self.assertEqual(self.solution.maxVowels("rhythms", 4), 0)

    def test_all_vowels_k_equals_length(self):
        """
        Input: s = "aeiou", k = 5
        Output: 5
        """
        self.assertEqual(self.solution.maxVowels("aeiou", 5), 5)

    def test_k_is_one(self):
        """
        Input: s = "tryhard", k = 1
        Output: 1
        """
        self.assertEqual(self.solution.maxVowels("tryhard", 1), 1)

if __name__ == '__main__':
    unittest.main()
