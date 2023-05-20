
from main import generate_hashtag as solution


def base_test(tests=None, expects=None, is_verbose=True):

    if tests is None:
        tests = [
            " Hello there thanks for trying my Kata",
            "    Hello     World   ",
            "",
        ]

    if expects is None:
        expects = [
            "#HelloThereThanksForTryingMyKata",
            "#HelloWorld",
            False,
        ]

    for test, expected, counter in zip(tests, expects, range(1, len(tests)+1)):
        result = solution(test)
        assert result == expected, f"Test #{counter} failed.\n"\
            f"\tExpected: {expected}\n"\
            f"\tReceived: {result}\n"
        print("Test #{} passed.{}".format(
            counter, f"\n\tTest case: {test}" if is_verbose else ""))


if __name__ == "__main__":
    base_test(is_verbose=False)
