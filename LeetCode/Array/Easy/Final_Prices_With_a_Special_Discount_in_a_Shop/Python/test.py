
from main import Solution


def base_test(tests=None, expects=None, is_verbose=True):

    _ = Solution()

    if tests is None:
        tests = [
            [1, 2, 3, 4, 5],
            [8, 4, 6, 2, 3],
            [10, 1, 1, 6],
        ]

    if expects is None:
        expects = [
            [1, 2, 3, 4, 5],
            [4, 2, 4, 2, 3],
            [9, 0, 1, 6],
        ]

    for test, expected, counter in zip(tests, expects, range(1, len(tests)+1)):
        result = _.finalPrices(test)
        assert result == expected, f"Test #{counter} failed.\n"\
            f"\tExpected: {expected}\n"\
            f"\tReceived: {result}\n"
        print("Test #{} passed.{}".format(
            counter, f"\n\tTest case: {test}" if is_verbose else ""))


if __name__ == "__main__":
    base_test()
