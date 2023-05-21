
from main import make_readable as solution


def base_test(tests=None, expects=None, is_verbose=True):

    if tests is None:
        tests = [
            0,
            5,
            60,
            86399,
            359999,
        ]

    if expects is None:
        expects = [
            "00:00:00",
            "00:00:05",
            "00:01:00",
            "23:59:59",
            "99:59:59",
        ]

    for test, expected, counter in zip(tests, expects, range(1, len(tests)+1)):
        result = solution(test)
        assert result == expected, f"Test #{counter} failed.\n"\
                                   f"\tExpected: {expected}\n"\
                                   f"\tReceived: {result}\n"
        print("Test #{} passed.{}".format(
            counter, f"\n\tTest case: {test}" if is_verbose else ""))


if __name__ == "__main__":
    base_test()
