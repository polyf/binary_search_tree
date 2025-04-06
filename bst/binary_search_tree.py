from bst.binary_search_tree_adt import BinarySearchTreeADT
from bst.node import Node


class BinarySearchTree(BinarySearchTreeADT):
    def __init__(self) -> None:
        self._root: Node = None

    def clear(self) -> None:
        self._root = None

    def is_empty(self) -> bool:
        return self._root is None

    def _get_parent(self, key: object) -> Node:
        parent: Node = None
        current: Node = self._root
        while current and key != current.key:
            parent = current
            current = current.next(key)
        return parent, current

    def search(self, key: object) -> object:
        def search(current: Node, key: object) -> object:
            if current is None:
                return None
            elif key == current.key:
                return current.value
            return search(current.next(key), key)

        return search(self._root, key)

    def insert(self, key: object, value: object) -> None:
        def insert(current: Node, key: object, value: object) -> Node:
            if current is None:
                return Node(key, value)
            elif key > current.key:
                current.right = insert(current.right, key, value)
            elif key < current.key:
                current.left = insert(current.left, key, value)
            return current

        self._root = insert(self._root, key, value)

    def __str__(self) -> str:
        return '[empty]' if self.is_empty() else self._str_tree()

    def _str_tree(self) -> str:
        def _str_tree(current: Node, is_right: bool, tree: str, ident: str) -> str:
            if current.right:
                tree = _str_tree(current.right, True, tree, ident + (' ' * 8 if is_right else ' |' + ' ' * 6))
            tree += ident + (' /' if is_right else ' \\') + "----- " + str(current) + '\n'
            if current.left:
                tree = _str_tree(current.left, False, tree, ident + (' |' + ' ' * 6 if is_right else ' ' * 8))
            return tree

        tree: str = ''
        if self._root.right:
            tree = _str_tree(self._root.right, True, tree, '')
        tree += str(self._root) + '\n'
        if self._root.left:
            tree = _str_tree(self._root.left, False, tree, '')

        return tree

    def _delete_by_copying(self, key: object) -> bool:
        parent: Node; current: Node
        parent, current = self._get_parent(key)
        if current is None:
            return False
        # Case 3
        elif current.left and current.right:
            at_the_right: Node = current.left
            while at_the_right.right:
                at_the_right = at_the_right.right
            self._delete_by_copying(at_the_right.key)
            current.key, current.value = at_the_right.key, at_the_right.value
        # Case 1/2
        else:
            next_node: Node = current.left or current.right
            if current == self._root:
                self._root = next_node
            elif current == parent.left:
                parent.left = next_node
            else:
                parent.right = next_node
        return True

    def delete(self, key: object) -> bool:
        return self._delete_by_copying(key)

    def _delete_by_merging(self, key: object) -> bool:
        parent: Node; current: Node
        parent, current = self._get_parent(key)
        if current is None:
            return False
        # Case 3
        elif current.left and current.right:
            at_the_right: Node = current.left
            while at_the_right.right:
                at_the_right = at_the_right.right
            at_the_right.right = current.right
            if current == self._root:
                self._root = current.left
            elif parent.left == current:
                parent.left = current.left
            else:
                parent.right = current.left
        # Case 1/2
        else:
            next_node: Node = current.left or current.right
            if current == self._root:
                self._root = next_node
            elif current == parent.left:
                parent.left = next_node
            else:
                parent.right = next_node
        return True

    def delete(self, key: object) -> bool:
        return self._delete_by_merging(key)

    def pre_order_traversal(self) -> None:
        def pre_order_traversal(current: Node) -> None:
            if current:
                print(current.key, end=' ')
                pre_order_traversal(current.left)
                pre_order_traversal(current.right)
        pre_order_traversal(self._root)

    def in_order_traversal(self) -> None:
        def in_order_traversal(current: Node) -> None:
            if current:
                in_order_traversal(current.left)
                print(current.key, end=' ')
                in_order_traversal(current.right)
        in_order_traversal(self._root)

    def post_order_traversal(self) -> None:
        def post_order_traversal(current: Node) -> None:
            if current:
                post_order_traversal(current.left)
                post_order_traversal(current.right)
                print(current.key, end=' ')
        post_order_traversal(self._root)

    def level_order_traversal(self) -> None:
        if self._root:
            queue = [self._root]
            while queue:
                current: Node = queue.pop(0)
                print(current.key, end=' ')
                if current.left: queue.append(current.left)
                if current.right: queue.append(current.right)

    def count_internal(self):
        def count_internal(node):
            if node is None:
                return 0
            is_internal = 1 if node.left or node.right else 0
            return is_internal + count_internal(node.left) + count_internal(node.right)

        if self.is_empty():
            return 0

        return count_internal(self._root.left) + count_internal(self._root.right)

    def _get_node(self, key: object) -> Node:
        _, current = self._get_parent(key)
        return current

    def degree(self, key: object) -> int:
        node = self._get_node(key)
        if node is None:
            return -1

        degree = 0
        if node.left is not None:
            degree += 1
        if node.right is not None:
            degree += 1

        return degree

    def height(self, key: object) -> int:
        node = self._get_node(key)
        if node is None:
            return -1

        def height(node):
            if node is None:
                return -1
            return 1 + max(height(node.left), height(node.right))

        return height(node)

    def level(self, key: object) -> int:
        # Objetivo: retornar o nível de um nó
        # Retorno: o nível do nó representado pela chave. Caso não seja encontrada a chave, retornar -1.
        pass

    def ancestor(self, key: object) -> str:
        # Objetivo: retornar os ancestrais (chave) lado a lado.
        # Retorno: lista em texto com as chaves lado a lado (separadas por espaço) que representam os ancestrais.
        # Caso não seja encontrada a chave, retornar None.
        pass
