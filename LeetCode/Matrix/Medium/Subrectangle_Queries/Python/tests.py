
from main import SubrectangleQueries


def base_test(tests=None, expects=None, is_verbose=True):

    if tests is None:
        tests = [
            [[1, 2, 1],
             [4, 3, 4],
             [3, 2, 1],
             [1, 1, 1]],
        ]

    final_results = [
        [[5, 5, 5],
         [5, 5, 5],
         [5, 5, 5],
         [10, 10, 10]],
    ]

    if expects is None:
        expects = [1, None, 5, 5, None, 10, 5]

    actions = ["getValue", "updateSubrectangle", "getValue",
               "getValue", "updateSubrectangle", "getValue",
               "getValue"]

    commands = [[0, 2], [0, 0, 3, 2, 5], [0, 2],
                [3, 1], [3, 0, 3, 2, 10], [3, 1],
                [0, 2]]

    for test, final_result, counter in zip(tests, final_results, range(1, len(tests)+1)):

        matrix = SubrectangleQueries(test)

        for expected, action, command, command_counter in zip(expects, actions, commands, range(1, len(commands)+1)):

            result = eval(
                test_command := f"matrix.{action}({', '.join(map(str, command))})")

            assert result == expected, f"Test #{counter} failed.\n"\
                f"\tExpected: {expected} in {expects}\n"\
                f"\tReceived: {result}\n"\
                f"\tTest action: {action}\n"\
                f"\tTest input: {command}\n"\
                f"\tTest command: {test_command}\n"
            print("Command #{} passed.{}".format(
                command_counter, f"\n\tTest input: {test_command}" if is_verbose else ""))

        assert matrix.rectangle == final_result, f"Test #{counter} failed.\n"\
            f"\tExpected: {final_result}\n"\
            f"\tReceived: {matrix.rectangle}\n"
        print("Test #{} passed.{}".format(
            counter, f"\n\tTest case: {test}" if is_verbose else ""))


if __name__ == "__main__":
    base_test()
