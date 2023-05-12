Example_1 = ("the sky is blue", "blue is sky the")
Example_2 = ("  hello world  ", "world hello")
Example_3 = ("a good   example", "example good a")


def revers_words(s: str):
    """
    Given an input string s, reverse the order of the words.
    A word is defined as a sequence of non-space characters.
    The words in s will be separated by at least one space.
    Return a string of the words in reverse order concatenated by a single space.
    Note that s may contain leading or trailing spaces or multiple spaces between
    two words. The returned string should only have a single space separating the words.
    Do not include any extra spaces.
    :param s: string
    :return: string with reversed words
    Constraints:
    1 <= s.length <= 10**4
    s contains English letters (upper-case and lower-case), digits, and spaces ' '.
    There is at least one word in s.
    """

    result = s.split()
    result.reverse()
    result = " ".join(result)

    return result


def test(example: tuple):
    if revers_words(example[0]) == example[1]:
        return f"Test with {example[0]} - ok"
    else:
        return f"Test with {example[0]} - failed. Result = {revers_words(example[0])}"


def main():
    print(test(Example_1))
    print(test(Example_2))
    print(test(Example_3))


if __name__ == "__main__":
    main()
