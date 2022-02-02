class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head_node):
        self.head = head_node

    def append_node(self, data):
        new_node = Node(data)
        current_node = self.head

        if current_node:
            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = new_node

        else:
            self.head = new_node

    def insert_at_start(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def print(self):
        current_node = self.head

        while current_node is not None:
            print(f'{current_node.data} --> ', end='')
            current_node = current_node.next

    def delete_duplicate_nodes(self):
        current = self.head
        previous = None
        data_set = set()

        while current is not None:

            if current.data in data_set:
                previous.next = current.next

            else:
                data_set.add(current.data)
                previous = current
            current = current.next

    def kth_from_last(self, k):
        current = self.head
        forward = self.head

        for i in range(k):
            if forward is None:
                print("k is greater than length of list")
                return -1
            forward = forward.next

        while forward is not None:
            current = current.next
            forward = forward.next

        return current.data

    def delete_middle_node(self, node):
        node.data = node.next.data
        node.next = node.next.next

    def partition(self, partition_value):
        current = self.head
        exchange_pointer = self.head

        while current is not None:
            if current.data >= partition_value:
                exchange_pointer = current
                break
            current = current.next

        if current is None:
            return

        runner = exchange_pointer.next

        while runner is not None:
            if runner.data < partition_value:
                temp = exchange_pointer.data
                exchange_pointer.data = runner.data
                runner.data = temp
                exchange_pointer = exchange_pointer.next
            runner = runner.next

    def reverse(self):
        previous = None
        current = self.head
        if current is None:
            return
        forward = self.head.next
        if forward is None:
            return

        while forward is not None:

            current.next = previous
            previous = current
            current = forward
            forward = forward.next

        current.next = previous
        self.head = current

    def rec_reverse(self):
        def reverse(next_address, current):
            if current.next is None:
                self.head = current
                current.next = next_address
                return
            else:
                forward = current.next
                reverse(current, forward)
                current.next = next_address
        curr = self.head
        reverse(None, curr)


def sum_linked_list(head1, head2):
    output_list = LinkedList(None)
    carry = 0

    curr1 = head1
    curr2 = head2
    while curr1 is not None and curr2 is not None:
        o_data = curr1.data + curr2.data + carry
        carry = o_data // 10
        output_list.append_node(o_data % 10)
        curr1 = curr1.next
        curr2 = curr2.next

    if curr1 is None and curr2 is None:
        if carry > 0:
            output_list.append_node(carry)
        return output_list.head

    if curr1 is None and curr2 is not None:
        while curr2 is not None:
            o_data = curr2.data + carry
            carry = o_data // 10
            output_list.append_node(o_data % 10)
            curr2 = curr2.next

        if carry > 0:
            output_list.append_node(carry)
        return output_list.head

    if curr2 is None and curr1 is not None:
        while curr1 is not None:
            o_data = curr1.data + carry
            carry = o_data // 10
            output_list.append_node(o_data % 10)
            curr1 = curr1.next

        if carry > 0:
            output_list.append_node(carry)
        return output_list.head

# linked_list1 = LinkedList(None)
# linked_list1.append_node(7)
# linked_list1.append_node(1)
# linked_list1.append_node(6)
# linked_list1.append_node(9)
# linked_list1.append_node(9)
# linked_list1.print()
# print()
#
# linked_list2 = LinkedList(None)
# linked_list2.append_node(5)
# linked_list2.append_node(9)
# linked_list2.append_node(3)
# linked_list2.print()
# print()
#
# o_head = sum_linked_list(linked_list1.head, linked_list2.head)
# while o_head is not None:
#     print(f'{o_head.data} --> ', end='')
#     o_head = o_head.next


def sum_rev_linked_list(list1, list2):

    runner1 = list1.head
    len1 = 0
    len2 = 0
    while runner1 is not None:
        len1 += 1
        runner1 = runner1.next

    runner2 = list2.head
    while runner2 is not None:
        len2 += 1
        runner2 = runner2.next

    if len1 > len2:
        diff = len1-len2
        for i in range(diff):
            list2.insert_at_start(0)

    if len2 > len1:
        diff = len2-len1
        for i in range(diff):
            list1.insert_at_start(0)

    list1.print()
    print()
    list2.print()
    print()

    def add_link_list(node1, node2, carry):
        if node1 is None and node2 is None:
            o_list = LinkedList(None)
            return 0, o_list
        else:
            carry, o_list = add_link_list(node1.next, node2.next, carry)
            sum = node1.data + node2.data + carry
            carry = sum // 10
            sum = sum % 10
            o_list.insert_at_start(sum)
            return carry, o_list

    car = 0
    curr1 = list1.head
    curr2 = list2.head

    output_carry, output_list = add_link_list(curr1, curr2, car)
    if output_carry > 0:
        output_list.insert_at_start(output_carry)
    return output_list


# linked_list1 = LinkedList(None)
# linked_list1.append_node(6)
# linked_list1.append_node(1)
# linked_list1.append_node(7)
#
#
# linked_list2 = LinkedList(None)
# linked_list2.append_node(9)
# linked_list2.append_node(9)
# linked_list2.append_node(5)
# linked_list2.append_node(9)
#
#
# o_list = sum_rev_linked_list(linked_list1, linked_list2)
# o_list.print()

def check_palindrome(linked_list):
    head = linked_list.head
    current = linked_list.head
    l = 0
    while current is not None:
        l += 1
        current = current.next
    if l == 1:
        return True

    mid_point = l // 2 - 1

    mid_node = linked_list.head
    for i in range(mid_point):
        mid_node = mid_node.next

    linked_list.head = mid_node.next
    linked_list.rec_reverse()
    mid_node.next = linked_list.head
    linked_list.head = head
    linked_list.print()
    print()

    start = linked_list.head
    mid = mid_node.next
    for i in range(mid_point+1):
        if start.data != mid.data:
            return False
        start = start.next
        mid = mid.next
    return True


# linked_list1 = LinkedList(None)
# linked_list1.append_node(1)
# linked_list1.append_node(2)
# linked_list1.append_node(3)
# linked_list1.append_node(4)
# linked_list1.append_node(3)
# linked_list1.append_node(2)
# linked_list1.append_node(1)
# linked_list1.print()
# print()
#
# print(check_palindrome(linked_list1))

def check_intersection(head_1: Node, head_2: Node):
    l1 = 0
    l2 = 0

    curr1 = head_1
    prev1 = head_1

    while curr1.next is not None:
        l1 += 1
        prev1 = curr1
        curr1 = curr1.next
    l1 += 1

    curr2 = head_2
    prev2 = head_2
    while curr2.next is not None:
        l2 += 1
        prev2 = curr2
        curr2 = curr2.next
    l2 += 1

    print(l1, l2)

    if prev1.next != prev2.next:
        return None

    diff = abs(l1-l2)
    if diff > 0:
        if l1 > l2:
            for i in range(diff):
                head_1 = head_1.next

        else:
            for i in range(diff):
                head_2 = head_2.next

    curr1 = head_1
    curr2 = head_2
    while curr1 is not None:
        if curr1 == curr2:
            return curr1
        curr1 = curr1.next
        curr2 = curr2.next


# head1 = Node(1)
# head1.next = Node(2)
#
#
# head2 = Node(10)
# head2.next = Node(9)
# head2.next.next = Node(8)
#
# head1.next.next = head2
#
# # 10-9-2-3
#
# i_node = check_intersection(head1, head2)
# if i_node:
#     print(f'Lists intersecting at {i_node.data}')
# else:
#     print("Non-intersecting lists")


def detect_loop(head_1) -> Node or None:

    curr = head_1
    fast = head_1

    while fast.next is not None and fast.next.next is not None:
        curr = curr.next
        fast = fast.next.next
        if curr == fast:
            break

    if fast.next is None or fast.next.next is None:
        return None

    curr = head_1
    while curr != fast:
        curr = curr.next
        fast = fast.next
    return curr


head1 = Node(1)
head1.next = Node(2)
head1.next.next = head1


l_node = detect_loop(head1)
if l_node:
    print(f'Loop detected at {l_node.data}')
else:
    print("No loop detected")












