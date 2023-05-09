
from main import Solution


def base_test(tests=None, expects=None, is_verbose=True):

    _ = Solution()

    if tests is None:
        tests = [
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
        ]

    if expects is None:
        expects = [
            [1, 2, 3, 6, 9, 8, 7, 4, 5],
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        ]

    for test, expected, counter in zip(tests, expects, range(1, len(tests)+1)):
        result = _.spiralOrder(test)
        assert result == expected, f"Test #{counter} failed.\n"\
            f"\tExpected: {expected}\n"\
            f"\tReceived: {result}\n"
        print("Test #{} passed.{}".format(
            counter, f"\n\tTest case: {test}" if is_verbose else ""))


if __name__ == "__main__":
    base_test(is_verbose=False)
