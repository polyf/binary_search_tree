import unittest
from bst.binary_search_tree import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.tree = BinarySearchTree()
        self.tree.insert(10, "Henry")
        self.tree.insert(5, "Alexandre")
        self.tree.insert(15, "Frederico")
        self.tree.insert(3, "Liria")
        self.tree.insert(7, "Polyana")
        self.tree.insert(20, "Liam")

    def test_degree(self):
        self.assertEqual(self.tree.degree(10), 2)  # Nó com dois filhos
        self.assertEqual(self.tree.degree(5), 2)  # Nó com dois filhos
        self.assertEqual(self.tree.degree(3), 0)  # Nó folha (grau 0)
        self.assertEqual(self.tree.degree(99), -1)  # Nó inexistente

    def test_height(self):
        self.assertEqual(self.tree.height(10), 2)  # Altura da árvore a partir da raiz (10)
        self.assertEqual(self.tree.height(5), 1)  # Altura a partir do nó 5
        self.assertEqual(self.tree.height(3), 0)  # Altura da folha
        self.assertEqual(self.tree.height(99), -1)  # Nó inexistente

    def test_level(self):
        self.assertEqual(self.tree.level(10), 0)  # Raiz
        self.assertEqual(self.tree.level(5), 1)  # Filho esquerdo da raiz
        self.assertEqual(self.tree.level(20), 2)  # Nó na profundidade 2
        self.assertEqual(self.tree.level(99), -1)  # Nó inexistente

    def test_ancestor(self):
        self.assertEqual(self.tree.ancestor(3), "10 5")  # Ancestrais do nó 3
        self.assertEqual(self.tree.ancestor(20), "10 15")  # Ancestrais do nó 20
        self.assertIsNone(self.tree.ancestor(10))  # Raiz não possui ancestrais
        self.assertIsNone(self.tree.ancestor(99))  # Nó inexistente

    def test_count_internal(self):
        self.assertEqual(self.tree.count_internal(), 2)  # Nós internos: 5, 15
        self.tree.delete(15)
        self.assertEqual(self.tree.count_internal(), 1)  # Após remoção do nó 15, nós internos: 5
        self.tree.delete(5)
        self.assertEqual(self.tree.count_internal(), 1)  # Após remoção do nó 5, nó interno: 3


if __name__ == "__main__":
    unittest.main()
