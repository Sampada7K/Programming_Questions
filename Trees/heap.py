class Heap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def percolate_up(self, index):
        while index//2 > 0:
            if self.heap_list[index] < self.heap_list[index//2]:
                self.heap_list[index], self.heap_list[index//2] = self.heap_list[index//2], self.heap_list[index]
            else:
                break
            index = index//2

    def insert(self, elem):
        self.heap_list.append(elem)
        self.current_size += 1
        self.percolate_up(self.current_size)

    def percolate_down(self, index):
        while (index*2) <= self.current_size:
            print(self.heap_list)
            min_child_index = self.find_min_child_index(index)
            if self.heap_list[index] > self.heap_list[min_child_index]:
                self.heap_list[index], self.heap_list[min_child_index] = \
                    self.heap_list[min_child_index], self.heap_list[index]
            else:
                break
            index = min_child_index
        print(self.heap_list)

    def find_min_child_index(self, index):
        if (index*2)+1 > self.current_size:
            return index*2
        else:
            return index*2 if self.heap_list[index*2] < self.heap_list[(index*2)+1] else (index*2)+1

    def del_min(self):
        min_elem = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.percolate_down(1)
        return min_elem

    def build_heap(self, input_list):
        self.current_size = len(input_list)
        self.heap_list = [0] + input_list
        index = self.current_size//2
        while index > 0:
            self.percolate_down(index)
            index -= 1


in_list = [9, 5, 6, 2, 3]
heap = Heap()
heap.build_heap(in_list)
print(heap.del_min())
heap.insert(4)
print(heap.heap_list)

print(heap.del_min())
print(heap.del_min())
print(heap.del_min())
print(heap.del_min())
print(heap.del_min())

