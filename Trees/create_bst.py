class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.data)
        in_order_traversal(node.right)


def create_bst(sorted_array):
    def create_bst_util(sorted_array1, start, end):
        if end < start:
            return None
        mid_point = (start + end) // 2
        node = Node(sorted_array1[mid_point])
        node.left = create_bst_util(sorted_array1, start, mid_point - 1)
        node.right = create_bst_util(sorted_array1, mid_point + 1, end)
        return node

    return create_bst_util(sorted_array, 0, len(sorted_array) - 1)


a = [1, 2, 3]
n = create_bst(a)
print(n)
in_order_traversal(n)
