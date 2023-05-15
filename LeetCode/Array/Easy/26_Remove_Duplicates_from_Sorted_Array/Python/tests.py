
from main import Solution


def base_test(tests=None, expects=None, is_verbose=True):

    _ = Solution()

    if tests is None:
        tests = [
            [1, 1, 2],
            [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
        ]

    if expects is None:
        expects = [
            2,
            5,
        ]

    for test, expected, counter in zip(tests, expects, range(1, len(tests)+1)):
        result = _.removeDuplicates(test)
        assert result == expected, f"Test #{counter} failed.\n"\
            f"\tExpected: {expected}\n"\
            f"\tReceived: {result}\n"
        print("Test #{} passed.{}".format(
            counter, f"\n\tTest case: {test}" if is_verbose else ""))


if __name__ == "__main__":
    base_test()
