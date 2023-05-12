
from main import permutations


# тест на правильность работы функции permutations
def test_permutations():
    s = 'abc'
    expected = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    result = permutations(s)
    assert sorted(result) == sorted(
        expected), f"Ожидаемый результат: {expected}, Фактический результат: {result}"


# тест на обработку пустого входного значения
def test_empty_input():
    s = ''
    expected = ['']
    result = permutations(s)
    assert sorted(result) == sorted(
        expected), f"Ожидаемый результат: {expected}, Фактический результат: {result}"


# тест на обработку входных данных, которые включают только один символ
def test_single_char_input():
    s = 'a'
    expected = ['a']
    result = permutations(s)
    assert sorted(result) == sorted(
        expected), f"Ожидаемый результат: {expected}, Фактический результат: {result}"


# тест на обработку входных данных, которые включают четыре символа
def test_four_chars_input():
    s = 'aabb'
    expected = ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
    result = permutations(s)
    assert sorted(result) == sorted(
        expected), f"Ожидаемый результат: {expected}, Фактический результат: {result}"


if __name__ == "__main__":
    test_permutations()
    test_empty_input()
    test_single_char_input()
    test_four_chars_input()
