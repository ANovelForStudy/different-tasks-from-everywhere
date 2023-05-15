
from typing import Optional


class BrowserHistory:

    class HistoryEntry:

        link_type = Optional["HistoryEntry"]

        def __init__(self, value: str, next_entry: link_type = None, prev_entry: link_type = None):
            self.value = value
            self.next_entry = next_entry
            self.prev_entry = prev_entry

    def __init__(self, homepage: str):
        self.homepage = self.HistoryEntry(homepage)

    def visit(self, url: str) -> None:
        new_entry = self.HistoryEntry(url)
        self.homepage.next_entry = new_entry
        new_entry.prev_entry = self.homepage
        self.homepage = new_entry

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.homepage.prev_entry is None:
                break

            self.homepage = self.homepage.prev_entry
        return self.homepage.value

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.homepage.next_entry is None:
                break

            self.homepage = self.homepage.next_entry
        return self.homepage.value


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
