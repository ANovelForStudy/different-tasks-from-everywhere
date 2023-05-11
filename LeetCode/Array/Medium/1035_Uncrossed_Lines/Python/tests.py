
from main import Solution


def base_test(tests=None, expects=None, is_verbose=True):

    _ = Solution()

    if tests is None:
        tests = [
            [[1, 4, 2], [1, 2, 4]],
            # [[2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2]],
            # [[1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1]]
        ]

    if expects is None:
        expects = [
            2,
            # 3,
            # 2,
        ]

    for test, expected, counter in zip(tests, expects, range(1, len(tests)+1)):
        result = _.maxUncrossedLines(test[0], test[1])
        assert result == expected, f"Test #{counter} failed.\n"\
            f"\tExpected: {expected}\n"\
            f"\tReceived: {result}\n"
        print("Test #{} passed.{}".format(
            counter, f"\n\tTest case: n = {test}" if is_verbose else ""))


if __name__ == "__main__":
    base_test(is_verbose=True)
