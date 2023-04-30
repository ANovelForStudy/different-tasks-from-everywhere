
import solution_with_an_additional_class as solution_class
import solution_via_a_list as solution_list


def first_test():
    commands = ["visit", "visit", "visit", "back",
                "back", "forward", "visit", "forward", "back", "back"]
    values = [["google.com"], ["facebook.com"], [
        "youtube.com"], [1], [1], [1], ["linkedin.com"], [2], [2], [7]]

    output = [None, None, None, "facebook.com", "google.com",
              "facebook.com", None, "linkedin.com", "google.com", "leetcode.com"]

    solutions = [solution_class, solution_list]

    for solution in solutions:
        result = []
        obj = solution.BrowserHistory("leetcode.com")
        for command, value in zip(commands, values):
            if isinstance(value[0], int):
                result.append(eval(f'obj.{command}({value[0]})'))
            else:
                result.append(eval(f'obj.{command}("{value[0]}")'))

        assert result == output, f"\n\tExpected: {output}\n\tReceived: {result}"

        print(f"Test 1 ('{solution.__name__}') completed successfully...")


def second_test():
    commands = []
    values = []

    output = []

    solutions = [solution_class, solution_list]

    for solution in solutions:
        result = []
        obj = solution.BrowserHistory("leetcode.com")
        for command, value in zip(commands, values):
            if isinstance(value[0], int):
                result.append(eval(f'obj.{command}({value[0]})'))
            else:
                result.append(eval(f'obj.{command}("{value[0]}")'))

        assert result == output, f"\n\tExpected: {output}\n\tReceived: {result}"

        print(f"Test 2 ('{solution.__name__}') completed successfully...")


if __name__ == "__main__":
    first_test()
    second_test()
