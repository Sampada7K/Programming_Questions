import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


def pre_order_traversal(node):
    if node:
        print(node.data)
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)


def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.data)
        in_order_traversal(node.right)


def post_order_traversal(node):
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.data)


def level_order_traversal(node):
    q = []
    if node:
        q.append(node)

    while len(q) != 0:
        child = q.pop(0)
        if child.left:
            q.append(child.left)
        if child.right:
            q.append(child.right)
        print(child.data)


def create_level_linked_list(node):
    q = []
    level_lists = []
    if node:
        q.append(node)

    while len(q) != 0:
        level_q = []
        child_q = []
        for node in q:
            level_q.append(node.data)
            if node.left:
                child_q.append(node.left)
            if node.right:
                child_q.append(node.right)
        level_lists.append(level_q)
        q = child_q

    return level_lists


def create_level_linked_list_recursive(root):
    def create_level_linked_list_recursive_util(node, level, level_lists1):
        if not node:
            return

        if len(level_lists) == level:
            temp_list = [node.data]
            level_lists.append(temp_list)
        else:
            temp_list = level_lists[level]
            temp_list.append(node.data)

        create_level_linked_list_recursive_util(node.left, level + 1, level_lists1)
        create_level_linked_list_recursive_util(node.right, level + 1, level_lists1)

    level_lists = []
    create_level_linked_list_recursive_util(root, 0, level_lists)
    return level_lists


def get_height(node):
    if not node:
        return -1
    return max(get_height(node.left) + 1, get_height(node.right) + 1)


def is_tree_balanced(root):
    if not root:
        return True
    height_diff = abs(get_height(root.left) - get_height(root.right))
    if height_diff > 1:
        return False
    else:
        return is_tree_balanced(root.right) and is_tree_balanced(root.left)


def is_node_balanced(node):
    min_value = -sys.maxsize - 1
    if not node:
        return -1

    left_height = is_node_balanced(node.left)
    if left_height == min_value:
        return min_value

    right_height = is_node_balanced(node.right)
    if right_height == min_value:
        return min_value

    height_difference = abs(left_height - right_height)
    if height_difference > 1:
        return min_value
    else:
        return max(left_height, right_height) + 1


def is_tree_balanced_efficient(root):
    min_value = -sys.maxsize - 1
    return is_node_balanced(root) != min_value


def first_is_tree_bst(root):
    def is_tree_bst_util(node: Node, node_list):
        if node.left:
            is_tree_bst_util(node.left, node_list)
        node_list.append(node.data)
        if node.right:
            is_tree_bst_util(node.right, node_list)
    tree_node_list = []
    if root:
        is_tree_bst_util(root, tree_node_list)
    print(tree_node_list)
    if not tree_node_list == sorted(tree_node_list):
        return False
    return True


def second_is_tree_bst(root):
    def is_tree_bst_util(node: Node, last_visited):
        if node.left:
            if not is_tree_bst_util(node.left, last_visited):
                return False

        if (last_visited is not None) and (node.data <= last_visited):
            return False
        last_visited = node.data

        if node.right:
            if not is_tree_bst_util(node.right, last_visited):
                return False
        return True
    if root:
        return is_tree_bst_util(root, None)


def is_tree_bst(root):
    def is_tree_bst_util(node: Node, min_data, max_data):
        if (max_data is not None) and (node.data > max_data):
            print("in max")
            print(f"Max is {max_data}, node data is {node.data}")
            return False

        if (min_data is not None) and (node.data <= min_data):
            print("in min")
            print(f"Min is {min_data}, node data is {node.data}")
            return False

        if node.left:
            if not is_tree_bst_util(node.left, min_data, node.data):
                return False

        if node.right:
            if not is_tree_bst_util(node.right, node.data, max_data):
                return False
        return True
    if root:
        return is_tree_bst_util(root, None, None)


def in_order_successor(node):
    if node.right:
        temp_node = node.right
        while temp_node.left is not None:
            temp_node = temp_node.left
        return temp_node
    else:
        temp_node = node
        while (temp_node.parent is not None) and (temp_node == temp_node.parent.right):
            temp_node = temp_node.parent
        if not temp_node.parent:
            return None
        return temp_node.parent


n = Node(8)

n.left = Node(4)
n.left.parent = n
n.left.left = Node(2)
n.left.left.parent = n.left
n.left.right = Node(6)
n.left.right.parent = n.left
n.left.left.left = Node(1)
n.left.left.left.parent = n.left.left
n.left.left.right = Node(3)
n.left.left.right.parent = n.left.left
n.left.right.left = Node(5)
n.left.right.left.parent = n.left.right
n.left.right.right = Node(7)
n.left.right.right.parent = n.left.right

n.right = Node(12)
n.right.parent = n
n.right.left = Node(10)
n.right.left.parent = n.right
n.right.right = Node(14)
n.right.right.parent = n.right
n.right.left.left = Node(9)
n.right.left.left.parent = n.right.left
n.right.left.right = Node(11)
n.right.left.right.parent = n.right.left
n.right.right.left = Node(13)
n.right.right.left.parent = n.right.right
n.right.right.right = Node(15)
n.right.right.right.parent = n.right.right



# ll = create_level_linked_list_recursive(n)
# for l in ll:
#     print(l)

# pre_order_traversal(n)
# in_order_traversal(n)
# post_order_traversal(n)
# level_order_traversal(n)

#
# print(get_height(n))
# print(is_tree_balanced(n))
#
# print(is_tree_balanced_efficient(n))

# print(is_tree_bst(n))
# print(second_is_tree_bst(n))

# print(n.parent)
# print(n.left.parent.data)
# print(n.right.parent.data)

# n_node = n.right.right.left

# n_node = n.left.left.right

# n_node = n.right.left

n_node = n.left.right.right

# n_node = n.right.right.right
if in_order_successor(n_node):
    print(f"Input is {n_node.data}")
    print(f"Output is {in_order_successor(n_node).data}")
else:
    print(f"Input is {n_node.data}")
    print("No successor")
