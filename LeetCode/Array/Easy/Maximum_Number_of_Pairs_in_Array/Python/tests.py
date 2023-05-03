
from main import Solution


def base_test(nums, expected, test_number):
    _ = Solution()
    result = _.numberOfPairs(nums)

    assert result == expected, f"Test {test_number} is failed:\n\t"\
                               f"Expected: {expected}\n\t"\
                               f"Got: {result}\n\tFor: {nums}"

    print(f"Test {test_number} is passed")


def tests():
    nums = [
        [1, 3, 2, 1, 3, 2, 2],
        [1, 1],
        [0],
        [4, 4, 3, 3, 2, 2, 1, 1, 5, 5, 6, 6, 7, 7],
    ]

    expecteds = [
        [3, 1],
        [1, 0],
        [0, 1],
        [7, 0],
    ]

    for number, expected, count in zip(nums, expecteds, range(len(nums))):
        base_test(number, expected, count + 1)


if __name__ == "__main__":
    tests()
