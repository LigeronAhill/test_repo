def min_distance(word1: str, word2: str) -> int:
    """
    Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
    You have the following three operations permitted on a word:
    Insert a character
    Delete a character
    Replace a character
    :param word1: str
    :param word2: str
    :return: Levenshtein distance =)
    """
    pass


def test():
    if min_distance("horse", "ros") == 3:
        print("Test 1 - ok")
    else:
        print(f"Test 1 failed with {min_distance('horse', 'ros')}")
    if min_distance("intention", "execution") == 5:
        print("Test 2 - ok")
    else:
        print(f"Test 2 failed with {min_distance('intention', 'execution')}")


def main():
    test()


if __name__ == "__main__":
    main()