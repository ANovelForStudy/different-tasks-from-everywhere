
from main import Solution


def base_test(tests=None, expects=None, is_verbose=True):

    _ = Solution()

    if tests is None:
        tests = [
            [6, [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]],
            [5, [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]],
        ]

    if expects is None:
        expects = [
            [0, 3],
            [0, 2, 3],
        ]

    for test, expected, counter in zip(tests, expects, range(1, len(tests)+1)):
        result = _.findSmallestSetOfVertices(test[0], test[1])
        assert result == expected, f"Test #{counter} failed.\n"\
            f"\tExpected: {expected}\n"\
            f"\tReceived: {result}\n"
        print("Test #{} passed.{}".format(
            counter, f"\n\tTest case: {test}" if is_verbose else ""))


if __name__ == "__main__":
    base_test()
