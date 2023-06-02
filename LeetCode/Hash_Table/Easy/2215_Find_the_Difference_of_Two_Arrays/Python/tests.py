
from main import Solution


def base_test(is_verbose=True):

    _ = Solution()

    tests = [
        [[1, 2, 3], [2, 4, 6]],
        [[1, 2, 3, 3], [1, 1, 2, 2]],
    ]

    expects = [
        [[1, 3], [4, 6]],
        [[3], []],
    ]

    for test, expected, counter in zip(tests, expects, range(1, len(tests)+1)):
        result = _.findDifference(test[0], test[1])
        assert result == expected, f"Test #{counter} failed.\n"\
            f"\tExpected: {expected}\n"\
            f"\tReceived: {test}\n"
        print("Test #{} passed.{}".format(counter,
                                          f"\n\tTest case: {test}" if is_verbose else ""))


if __name__ == "__main__":
    base_test()
