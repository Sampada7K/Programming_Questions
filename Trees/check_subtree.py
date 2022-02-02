# Given two trees, check whether T2 is a subtree of T1
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def check_subtree(node1, node2):
    # Empty tree is always a subtree
    if node2 is None:
        return True
    # Bigger tree(T1) end reached, but not the smaller tree(T2)
    if node1 is None:
        return False
    # Matching node found
    if node1.data == node2.data:
        if match_tree(node1.left, node2.left) and match_tree(node1.right, node2.right):
            return True
    # Matching node not found, check using left and right subtrees for bigger tree(T1)
    return check_subtree(node1.left, node2) or check_subtree(node1.right, node2)


def match_tree(node1, node2):
    # Nothing left in both subtrees
    if node1 is None and node2 is None:
        return True
    # Mismatch in data or either subtree ends
    if node1.data != node2.data or node1 is None or node2 is None:
        return False
    else:
        return match_tree(node1.left, node2.left) and match_tree(node1.right, node2.right)
