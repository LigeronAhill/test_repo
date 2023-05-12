Example_1 = ("hello", "holle")
Example_2 = ("leetcode", "leotcede")


def revers_vowels(s: str):
    """
    Given a string s, reverse only all the vowels in the string and return it.
    The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower
    and upper cases, more than once.
    :param s: string
    :return: string with reversed vowels
    """
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    temp = list(s)
    stack = []

    for i in range(len(temp)):
        if temp[i] in vowels:
            stack.append(temp[i])
    for i in range(len(temp)):
        if temp[i] in vowels:
            temp[i] = stack[-1]
            stack.pop(-1)

    result = "".join(temp)
    return result


def test(example: tuple):
    if revers_vowels(example[0]) == example[1]:
        return f"Test with {example[0]} - ok"
    else:
        return f"Test with {example[0]} - failed. Result = {revers_vowels(example[0])}"


def main():
    print(test(Example_1))
    print(test(Example_2))


if __name__ == "__main__":
    main()
