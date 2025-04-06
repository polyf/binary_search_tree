from bst.binary_search_tree import BinarySearchTree

if __name__ == "__main__":

    tree = BinarySearchTree()
    tree.insert(10, "Polyana")
    tree.insert(5, "Liam")
    tree.insert(12, "Alexandre")
    tree.insert(1, "Henry")
    tree.insert(15, "Mário")
    tree.insert(11, "Frederico")

    print("Testando count_internal:")
    print(tree.count_internal())
    print("Testando _str_tree:")
    print(tree.__str__())
    print("Testando degree")
    print(tree.degree(5))
    print("Testando Search")
    print(tree.search(12))
    print("Testando Height")
    print(tree.height(1))


