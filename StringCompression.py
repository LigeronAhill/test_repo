def main():
    test()


chars1 = ["a", "a", "b", "b", "c", "c", "c"]
chars2 = ["a"]
chars3 = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]


def test():
    if Solution.compress(Solution(), chars1) == 6:
        print("Test 1 -ok")
    else:
        print(f"Test 1 failed with {Solution.compress(Solution(), chars1)}")
    if Solution.compress(Solution(), chars2) == 1:
        print("Test 2 -ok")
    else:
        print(f"Test 2 failed with {Solution.compress(Solution(), chars2)}")
    if Solution.compress(Solution(), chars3) == 4:
        print("Test 3 -ok")
    else:
        print(f"Test 3 failed with {Solution.compress(Solution(), chars3)}")


class Solution:
    def compress(self, chars: list[str]) -> int:
        """
        Given an array of characters chars, compress it using the following algorithm:
        Begin with an empty string s. For each group of consecutive repeating characters in chars:
        If the group's length is 1, append the character to s.
        Otherwise, append the character followed by the group's length.
        The compressed string s should not be returned separately, but instead, be stored in the input
        character array chars. Note that group lengths that are 10 or longer will be split into multiple
        characters in chars.
        After you are done modifying the input array, return the new length of the array.
        You must write an algorithm that uses only constant extra space.
        :param chars: list(str)
        :return: len(compressed_list) & compressed_list
        """
        n = len(chars)
        if n == 0:
            return 0

        i, j, k = 0, 0, 0

        while j < n:
            while j < n and chars[j] == chars[i]:
                j += 1

            chars[k] = chars[i]
            k += 1

            if j - i > 1:
                count = str(j - i)
                for c in count:
                    chars[k] = c
                    k += 1

            i = j

        return k


if __name__ == "__main__":
    main()

'''
Here's the Python code to solve the problem:

```
def compress(chars: List[str]) -> int:
    n = len(chars)
    if n == 0:
        return 0
    
    i, j, k = 0, 0, 0
    
    while j < n:
        while j < n and chars[j] == chars[i]:
            j += 1
        
        chars[k] = chars[i]
        k += 1
        
        if j - i > 1:
            count = str(j - i)
            for c in count:
                chars[k] = c
                k += 1
        
        i = j
    
    return k
```

The function receives a list of characters `chars` as input and returns an integer,
which is the length of the compressed string. Inside the function, we use three pointers 
`i`, `j`, and `k` to keep track of the current character, the end of the current group,
and the position to write the compressed string, respectively.

Then, we iterate through the characters in `chars`, and for each group of consecutive 
repeating characters, we check if the group's length is greater than 1. If it is, we
convert the length to a string and write it to `chars`.

Finally, we return the length of the compressed string `k`.
'''
