
from main import Solution


def base_test(tests=None, expects=None, is_verbose=True):

    _ = Solution()

    if tests is None:
        tests = [
            [["c", "f", "j"], 'a'],
            [["c", "f", "j"], 'c'],
            [["x", "x", "y", "y"], 'z'],
            [["e", "e", "e", "k", "q", "q", "q", "v", "v", "y"], 'k'],
            [["c", "f", "j"], 'g'],
        ]

    if expects is None:
        expects = [
            'c',
            'f',
            'x',
            'q',
            'j',
        ]

    for test, expected, counter in zip(tests, expects, range(1, len(tests)+1)):
        result = _.nextGreatestLetter(*test)
        assert result == expected, f"Test #{counter} failed.\n"\
            f"\tExpected: {expected}\n"\
            f"\tReceived: {result}\n"
        print("Test #{} passed.{}".format(
            counter, f"\n\tTest case: {test}" if is_verbose else ""))


if __name__ == "__main__":
    base_test()
