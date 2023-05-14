def main():
    test()


def test():
    if increasing_triplet(example_1):
        print("Test 1 - ok")
    else:
        print(f"Test 2 failed. Return: {increasing_triplet(example_1)}")
    if not increasing_triplet(example_2):
        print("Test 2 - ok")
    else:
        print(f"Test 2 failed. Return: {increasing_triplet(example_2)}")
    if increasing_triplet(example_3):
        print("Test 3 - ok")
    else:
        print(f"Test 3 filed. Return: {increasing_triplet(example_3)}")


def increasing_triplet(nums: list) -> bool:
    return True


example_1 = [1, 2, 3, 4, 5]
example_2 = [5, 4, 3, 2, 1]
example_3 = [2,1,5,0,4,6]

if __name__ == "__main__":
    main()
