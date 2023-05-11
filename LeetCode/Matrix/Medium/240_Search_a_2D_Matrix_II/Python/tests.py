
from main import Solution


def base_test(tests=None, expects=None, is_verbose=True):

    _ = Solution()

    if tests is None:
        tests = [
            ([[1, 4, 7, 11, 15],
              [2, 5, 8, 12, 19],
              [3, 6, 9, 16, 22],
              [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]], 5),
            ([[1, 4, 7, 11, 15],
              [2, 5, 8, 12, 19],
              [3, 6, 9, 16, 22],
              [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]], 20),
            ([[1, 4, 7, 11, 15],
              [2, 5, 8, 12, 19],
              [3, 6, 9, 16, 22],
              [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]], 0),
            ([[1, 1]], 2),
        ]

    if expects is None:
        expects = [
            True,
            False,
            False,
            False,
        ]

    for test, expected, counter in zip(tests, expects, range(1, len(tests)+1)):
        result = _.searchMatrix(test[0], test[1])
        assert result == expected, f"Test #{counter} failed.\n"\
            f"\tExpected: {expected}\n"\
            f"\tReceived: {result}\n"
        print("Test #{} passed.{}".format(
            counter, f"\n\tTest case: n = {test}" if is_verbose else ""))


if __name__ == "__main__":
    base_test(is_verbose=True)
