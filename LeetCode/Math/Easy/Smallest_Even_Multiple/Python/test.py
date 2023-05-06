
from main import Solution


def base_test(tests=None, expects=None, is_verbose=True):

    _ = Solution()

    if tests is None:
        tests = [
            5,
            6,
        ]

    if expects is None:
        expects = [
            10,
            6,
        ]

    for test, expected, counter in zip(tests, expects, range(1, len(tests)+1)):
        result = _.smallestEvenMultiple(test)
        assert result == expected, f"Test #{counter} failed.\n"\
            f"\tExpected: {expects}\n"\
            f"\tReceived: {test}\n"
        print("Test #{} passed.{}".format(
            counter, f"\n\tTest case: {test}" if is_verbose else ""))


if __name__ == "__main__":
    base_test()
