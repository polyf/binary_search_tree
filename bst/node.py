from typing import Optional

class Node:
    def __init__(self, key: object, value: object) -> None:
        self.key = key
        self.value = value
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None

    def __str__(self) -> str:
        return str(self.key)

    def next(self, other_key: object) -> Optional['Node']:
        return self.left if other_key < self.key else self.right
