
from main import rgb as solution


def base_test(tests=None, expects=None, is_verbose=True):

    if tests is None:
        tests = [
            (255, 255, 255),
            (255, 255, 300),
            (0, 0, 0),
            (148, 0, 211),
        ]

    if expects is None:
        expects = [
            "FFFFFF",
            "FFFFFF",
            "000000",
            "9400D3",
        ]

    for test, expected, counter in zip(tests, expects, range(1, len(tests)+1)):
        result = solution(*test)
        assert result == expected, f"Test #{counter} failed.\n"\
            f"\tExpected: {expected}\n"\
            f"\tReceived: {result}\n"
        print("Test #{} passed.{}".format(
            counter, f"\n\tTest case: {test}" if is_verbose else ""))


if __name__ == "__main__":
    base_test()
