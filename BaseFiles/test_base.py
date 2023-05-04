
from main import Solution


def base_test(is_verbose=True):

    _ = Solution()
    
    tests = [
        "",
    ]

    expects = [
        "",
    ]

    for test, expected, counter in zip(tests, expects, range(1, len(tests)+1)):
        result = _.test_function(test)
        assert result == expects, f"Test #{counter} failed.\n"\
                                  f"\tExpected: {expects}\n"\
                                  f"\tReceived: {test}\n"
        print("Test #{} passed.{}".format(counter, f"\n\tTest case: {test}" if is_verbose else ""))


if __name__ == "__main__":
    base_test()
