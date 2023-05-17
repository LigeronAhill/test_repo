def main():
    test()


def test():
    print('Test 1 - ok' if max_vowels("abciiidef", 3) == 3 else 'Test 1 failed', max_vowels("abciiidef", 3))
    print('Test 2 - ok' if max_vowels("aeiou", 2) == 2 else 'Test 2 failed', max_vowels("aeiou", 2))
    print('Test 3- ok' if max_vowels("leetcode", 3) == 2 else 'Test 3 failed', max_vowels("leetcode", 3))


def max_vowels(s: str, k: int) -> int:
    """
    Given a string s and an integer k, return the maximum number of
    vowel letters in any substring of s with length k.
    Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
    Constraints:
    1 <= s.length <= 10**5
    s consists of lowercase English letters.
    1 <= k <= s.length
    :param s: string
    :param k: length of substring
    :return: the maximum number of vowel letters in any substring of s with length k
    """
    if len(s) > 10**5 or len(s) == 0 or k == 0 or k > len(s):
        raise ValueError

    vowels = set("aeiou")
    window = sum(c in vowels for c in s[:k])
    result = window

    for i in range(k, len(s)):
        window += (s[i] in vowels) - (s[i - k] in vowels)
        result = max(result, window)

    return result


if __name__ == "__main__":
    main()
