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
    n, m = len(word1), len(word2)
    if n > m:
        word1, word2 = word2, word1
        n, m = m, n
    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if word1[j - 1] != word2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)
    return current_row[n]


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
