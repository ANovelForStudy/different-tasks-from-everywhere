
from main import Solution


def base_test(tests=None, expects=None, is_verbose=True):

    _ = Solution()

    if tests is None:
        tests = [
            [10, 6, 8, 5, 11, 9],
            [5, 1, 2, 3, 10],
        ]

    if expects is None:
        expects = [
            [3, 1, 2, 1, 1, 0],
            [4, 1, 1, 1, 0],
        ]

    for test, expected, counter in zip(tests, expects, range(1, len(tests)+1)):
        result = _.canSeePersonsCount(test)
        assert result == expected, f"Test #{counter} failed.\n"\
            f"\tExpected: {expected}\n"\
            f"\tReceived: {result}\n"
        print("Test #{} passed.{}".format(
            counter, f"\n\tTest case: {test}" if is_verbose else ""))


if __name__ == "__main__":
    base_test()
