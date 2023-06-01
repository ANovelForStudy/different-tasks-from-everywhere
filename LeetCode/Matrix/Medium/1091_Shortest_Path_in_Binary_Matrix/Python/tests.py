
from main import Solution


def base_test(is_verbose=True):

    _ = Solution()

    tests = [
        [[0, 0, 0], [1, 1, 0], [1, 1, 0]],
        [[1, 0, 0], [1, 1, 0], [1, 1, 0]],
        [[0, 1], [1, 0]],
    ]

    expects = [
        4,
        -1,
        2,
    ]

    for test, expected, counter in zip(tests, expects, range(1, len(tests)+1)):
        result = _.shortestPathBinaryMatrix(test)
        assert result == expected, f"Test #{counter} failed.\n"\
            f"\tExpected: {expected}\n"\
            f"\tReceived: {test}\n"
        print("Test #{} passed.{}".format(counter,
                                          f"\n\tTest case: {test}" if is_verbose else ""))


if __name__ == "__main__":
    base_test()
