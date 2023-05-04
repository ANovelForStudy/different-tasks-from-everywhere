
from main import Solution


def base_test(is_verbose=True):

    _ = Solution()

    tests = [
        "a123bc34d8ef34",
        "leet1234code234",
        "a1b01c001",
    ]

    expects = [
        3,
        2,
        1,
    ]

    for test, expected, counter in zip(tests, expects, range(1, len(tests)+1)):
        result = _.numDifferentIntegers(test)
        assert result == expected, f"Test #{counter} failed.\n"\
            f"\tExpected: {expected}\n"\
            f"\tReceived: {test}\n"
        print("Test #{} passed.{}".format(counter,
                                          f"\n\tTest case: {test}" if is_verbose else ""))


if __name__ == "__main__":
    base_test()
