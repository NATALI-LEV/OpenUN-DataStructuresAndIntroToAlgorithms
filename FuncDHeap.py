import math


class DHeap:
    def __init__(self, max_size, d):
        """
        Initialize a D-ary heap.

        Parameters:
        - max_size (int): Maximum size of the heap.
        - d (int): The branching factor of the heap.
        """    
        self.heap = [0] * max_size
        self.max_size = max_size
        self.size = 0
        self.d = d

    def height(self):
        """
        Calculate the height of the heap.

        Returns:
        - int: Height of the heap.
        """
        return int(math.ceil((math.log(self.size * (self.d - 1) + 1) / math.log(self.d)) - 1))

    def parent_index(self, curr_node_index):
        """
        Get the index of the parent of a node.

        Parameters:
        - curr_node_index (int): Index of the current node.

        Returns:
        - int: Index of the parent node.
        """
        return (curr_node_index - 1) // self.d

    def child_index(self, curr_node_index, requested_child):
        """
        Get the index of a child of a node.

        Parameters:
        - curr_node_index (int): Index of the current node.
        - requested_child (int): The requested child number.

        Returns:
        - int: Index of the requested child node.
        """
        return self.d * curr_node_index + requested_child + 1

    def max_heapify(self, index_to_heapify_from):
        """
        Maintain the max-heap property.

        Parameters:
        - index_to_heapify_from (int): Index from which to start max-heapify.
        """
        max_element_index = index_to_heapify_from

        for child_number in range(self.d):
            child_index_in_heap_array = self.child_index(index_to_heapify_from, child_number)

            if child_index_in_heap_array < self.size and self.heap[child_index_in_heap_array] > self.heap[max_element_index]:
                max_element_index = child_index_in_heap_array

        if max_element_index != index_to_heapify_from:
            self.swap(max_element_index, index_to_heapify_from)
            self.max_heapify(max_element_index)

    def extract_max(self):
        """
        Extract the maximum element from the heap.

        Returns:
        - int: The maximum element.
        """
        max_element = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.max_heapify(0)
        return max_element

    def increase_key(self, index, key):
        """
        Increase the key of a node.

        Parameters:
        - index (int): Index of the node.
        - key (int): New key value.
        """
        if not self.index_in_heap_array_range(index) or key < self.heap[index]:
            return

        self.heap[index] = key

        while index > 0 and self.heap[self.parent_index(index)] < key:
            self.swap(index, self.parent_index(index))
            index = self.parent_index(index)

    def insert(self, key):
        """
        Insert a new key into the heap.

        Parameters:
        - key (int): Key to be inserted.
        """
        self.size += 1
        self.heap[self.size - 1] = float('-inf')
        self.increase_key(self.size - 1, key)

    def __str__(self):
        """
        Convert the heap to a string representation.

        Returns:
        - str: String representation of the heap.
        """
        sb_tree = []
        sb_levels = []

        index_of_first_level_element = 0
        heap_height = self.height() + 1
        
        for level in range(1, heap_height + 1):
            max_elements_in_level = self.d**(level - 1)
            indent = self.d**(heap_height - level) - 1
            spacing = self.d**(heap_height - (level - 1)) - 1

            sb_levels.append(f"Level {level}: ")
            sb_tree.append(' ' * indent)

            elements_printed_from_current_level = 0
            for element_index_in_level in range(index_of_first_level_element, self.size):
                if elements_printed_from_current_level >= max_elements_in_level:
                    break

                sb_tree.append(str(self.heap[element_index_in_level]))
                sb_levels.append(f"{self.heap[element_index_in_level]}, ")
                sb_tree.append(' ' * spacing)

                elements_printed_from_current_level += 1

            index_of_first_level_element = self.child_index(index_of_first_level_element, 0)
            sb_tree.append('\n')
            sb_levels.append('\n')

        return ''.join(sb_tree) + '\n\n' + ''.join(sb_levels)

    
    def print_whitespaces(count):
        """
        Create a string of whitespaces.

        Parameters:
        - count (int): Number of whitespaces.

        Returns:
        - str: String of whitespaces.
        """
        return ' ' * count

    def swap(self, first_element_index, second_element_index):
        """
        Swap two elements in the heap.

        Parameters:
        - first_element_index (int): Index of the first element.
        - second_element_index (int): Index of the second element.
        """
        if not self.index_in_heap_array_range(first_element_index) or not self.index_in_heap_array_range(
                second_element_index):
            return

        self.heap[first_element_index], self.heap[second_element_index] = self.heap[second_element_index], \
                                                                          self.heap[first_element_index]

    def index_in_heap_array_range(self, index_to_check):
        """
        Check if an index is within the valid range of the heap array.

        Parameters:
        - index_to_check (int): Index to check.

        Returns:
        - bool: True if the index is within the valid range, False otherwise.
        """
        return 0 <= index_to_check <= self.max_size
