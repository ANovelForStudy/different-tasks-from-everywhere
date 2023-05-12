
from main import pig_it


def base_test(tests=None, expects=None, is_verbose=True):

    if tests is None:
        tests = [
            "Pig latin is cool",
            "Hello world !",
        ]

    if expects is None:
        expects = [
            "igPay atinlay siay oolcay",
            "elloHay orldway !",
        ]

    for test, expected, counter in zip(tests, expects, range(1, len(tests)+1)):
        result = pig_it(test)
        assert result == expected, f"Test #{counter} failed.\n"\
            f"\tExpected: {expected}\n"\
            f"\tReceived: {result}\n"
        print("Test #{} passed.{}".format(
            counter, f"\n\tTest case: {test}" if is_verbose else ""))


if __name__ == "__main__":
    base_test()
