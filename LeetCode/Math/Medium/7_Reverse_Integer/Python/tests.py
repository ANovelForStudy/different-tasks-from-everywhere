
from main import Solution


def base_test(is_verbose=True):

    _ = Solution()

    tests = [
        123,
        -321,
        120,
    ]

    expects = [
        321,
        -123,
        21,
    ]

    for test, expected, counter in zip(tests, expects, range(1, len(tests)+1)):
        result = _.reverse(test)
        assert result == expected, f"Test #{counter} failed.\n"\
            f"\tExpected: {expected}\n"\
            f"\tReceived: {test}\n"
        print("Test #{} passed.{}".format(counter,
                                          f"\n\tTest case: {test}" if is_verbose else ""))


if __name__ == "__main__":
    base_test()
