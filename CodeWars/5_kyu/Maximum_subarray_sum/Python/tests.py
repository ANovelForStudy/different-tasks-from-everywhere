
from main import max_sequence as solution


def base_test(tests=None, expects=None, is_verbose=True):

    if tests is None:
        tests = [
            [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        ]

    if expects is None:
        expects = [
            6,
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
