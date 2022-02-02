class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.data)
        in_order_traversal(node.right)


def covers(root: TreeNode, node: TreeNode):
    if root is None:
        return False
    if root == node:
        return True
    return covers(root.left, node) or covers(root.right, node)


def rec_first_common_ancestor_helper(root, node1, node2):
    if root is None or root == node1 or root == node2:
        return root
    node1_left = covers(root.left, node1)
    node2_left = covers(root.left, node2)
    print(f"Root is {root.data}")
    print(f"node1_left is {node1_left} node2_left is {node2_left}")

    if node1_left != node2_left:
        return root

    # node1 and node2 both are in the left subtree
    if node1_left:
        return rec_first_common_ancestor_helper(root.left, node1, node2)
    # node1 and node2 both are in the right subtree
    else:
        return rec_first_common_ancestor_helper(root.right, node1, node2)


def rec_first_common_ancestor(root, node1, node2):
    # Input validation
    if root is None or node1 is None or node2 is None:
        return None
    # Check if node1 and node2 belong to the tree starting with root
    if (not covers(root, node1)) or (not covers(root, node2)):
        return None
    print("Calling helper")
    return rec_first_common_ancestor_helper(root, node1, node2)


def optimized_first_common_ancestor(root, node1, node2):
    if root:
        print(f"Calling({root.data}, {node1.data}, {node2.data})")
    else:
        print(f"Calling(None, {node1.data}, {node2.data})")
    if root is None or root == node1 or root == node2:
        return root
    x = optimized_first_common_ancestor(root.left, node1, node2)
    if x is not None and x != node1 and x != node2:
        return x
    y = optimized_first_common_ancestor(root.right, node1, node2)
    if y is not None and y != node1 and y != node2:
        return y
    if x is not None and y is not None:
        return root
    # if x is not None and y is None returns x
    # if x is None and y is not None returns y
    # if x is None and y is None returns y(None)
    return x if x else y


n = TreeNode(8)
n.left = TreeNode(4)
n.left.left = TreeNode(2)
n.left.right = TreeNode(6)
n.left.left.left = TreeNode(1)
n.left.left.right = TreeNode(3)
n.left.right.left = TreeNode(5)
n.left.right.right = TreeNode(7)

n.right = TreeNode(12)
n.right.left = TreeNode(10)
n.right.right = TreeNode(14)
n.right.left.left = TreeNode(9)
n.right.left.right = TreeNode(11)
n.right.right.left = TreeNode(13)
n.right.right.right = TreeNode(15)
#                         8
#              4                       12
#         2         6            10           14
#       1   3     5   7        9    11     13    15
# in_order_traversal(n)

# result = rec_first_common_ancestor(n, n.left.right, n.left.right.left)
# if result:
#     print(f"First common ancestor is {result.data}")
# else:
#     print("result is None")

node1_test = n.right.left
print(node1_test.data)
node2_test = n.right.right.right
print(node2_test.data)
optimized_result = optimized_first_common_ancestor(n, node1_test, node2_test)
if optimized_result:
    print(f"First common ancestor is {optimized_result.data}")
else:
    print("result is None")



