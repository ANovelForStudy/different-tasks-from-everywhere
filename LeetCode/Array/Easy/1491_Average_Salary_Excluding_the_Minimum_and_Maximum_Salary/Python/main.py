
from typing import List


class Solution:

    def average(self, salary: List[int]) -> float:

        def quick_sort(array):
            length = len(array)
            if length < 2:
                return array

            pivot_index = length // 2 if length % 2 != 0 else length // 2 - 1
            pivot = array[pivot_index]

            less = [i for i in array[:pivot_index] +
                    array[pivot_index+1:] if i <= pivot]
            greater = [i for i in array[:pivot_index] +
                       array[pivot_index+1:] if i > pivot]

            return quick_sort(less) + [pivot] + quick_sort(greater)

        salary = quick_sort(salary)[1:-1]
        return sum(salary) / len(salary)
