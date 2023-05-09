def merge_alternately(word1: str, word2: str) -> str:
    """
    You are given two strings word1 and word2. Merge the strings by adding
    letters in alternating order, starting with word1. If a string is longer
    than the other, append the additional letters onto the end of the merged string.

    Return the merged string.
    :param word1: string
    :param word2: string
    :return: merged string.
    """
    w1 = [" "] * (len(word1) * 2 - 1)
    w2 = [" "] * len(word2) * 2
    count = 0
    count2 = 0
    rs = [" "] * max(len(w1), len(w2))

    for i in range(len(w1)):
        if i % 2 == 0:
            w1[i] = word1[count]
        else:
            w1[i] = " "
            count += 1

    for i in range(len(w2)):
        if i % 2 == 0:
            w2[i] = " "
        else:
            w2[i] = word2[count2]
            count2 += 1

    for i in range(len(w1)):
        if i % 2 == 0:
            rs[i] = w1[i]
    for i in range(len(w2)):
        if i % 2 == 1:
            rs[i] = w2[i]

    rs = "".join(str(char) for char in rs)
    result = rs.replace(" ", "")
    return result


def test(word1, word2, res):
    if merge_alternately(word1, word2) == res:
        print(f"test with {word1} and {word2} - ok, {merge_alternately(word1, word2)}")
    else:
        print(f"test failed, {merge_alternately(word1, word2)}")


test("abc", "pqr", "apbqcr")
test("ab", "pqrs", "apbqrs")
test("abcd", "pq", "apbqcd")
