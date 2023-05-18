
from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        nodes = []
        for edge in edges:
            nodes += edge
        nodes = list(set(nodes))

        result = {}

        for node in nodes:
            result[node] = 0

        for edge in edges:
            result[edge[1]] += 1

        return [l[0] for l in result.items() if l[1] == 0]
