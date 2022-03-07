import math


class PriorityQueue:
    """
    Priority Queue implemented as a binary Max Heap where the value of each node is less than
    or equal to the value of its parent node. Value at root contains maximum priority value.
    Max Heap is represented as list (self.queue) where the root element is stored in self.queue[0],
    and children are stored in self.queue[i], where i > 0.
    """
    def __init__(self) -> None:
        self.queue = []

    @staticmethod
    def get_parent_index(index: int) -> int:
        """
        Retrieves the index of the parent node from the binary heap
        :param index: index of child node
        :return: int: index of parent node
        """
        return math.floor((index - 1) / 2)

    @staticmethod
    def get_left_index(index: int) -> int:
        """
        Retrieves the index of the left child node from the binary heap
        :param index: index of parent node
        :return: int: index of left child node
        """
        return 2 * index + 1

    @staticmethod
    def get_right_index(index: int) -> int:
        """
        Retrieves the index of the right child node from the binary heap
        :param index: index of parent node
        :return: int: index of right child node
        """
        return 2 * index + 2

    def get_node_at_index(self, index):
        """
        Retrieves node at specified index
        :param index: index of node
        :return: dict: {'priority': int, 'command': <function>}
        """
        try:
            return self.queue[index]
        except IndexError as e:
            print(f'Node at index {index} not found.')
            return None

    def get_parent_node(self, index: int) -> dict:
        """
        Retrieves the parent of the child node from the binary heap
        :param index: index of child node
        :return: dict: parent node
        """
        return self.get_node_at_index(self.get_parent_index(index))

    def get_left_node(self, index: int) -> dict:
        """
        Retrieves the left child of the parent node from the binary heap
        :param index: index of parent node
        :return: int: left child node
        """
        return self.get_node_at_index(self.get_left_index(index))

    def get_right_node(self, index: int) -> dict:
        """
        Retrieves the right child of the parent node from the binary heap
        :param index: index of parent node
        :return: int: right child node
        """
        return self.get_node_at_index(self.get_right_index(index))

    def has_parent_node(self, index: int) -> bool:
        """
        Checks if the current node has a parent node.
        :param index: index of child node
        :return: bool: True if parent node exists, else False
        """
        return self.get_parent_index(index) >= 0

    def has_left_node(self, index: int) -> bool:
        """
        Checks if the current node has a left child node.
        :param index: index of current node
        :return: bool: True if child node exists, else False
        """
        return self.get_left_index(index) < len(self.queue)

    def has_right_node(self, index: int) -> bool:
        """
        Checks if the current node has a right child node.
        :param index: index of current node
        :return: bool: True if child node exists, else False
        """
        return self.get_right_index(index) < len(self.queue)

    def swap_nodes(self, index1: int, index2: int) -> None:
        """
        Swaps two nodes in the binary heap
        :param index1: Index of node 1
        :param index2: Index of node 2
        :return: None
        """
        self.queue[index1], self.queue[index2] = self.queue[index2], self.queue[index1]

    def insert_node(self, node: dict) -> None:
        """
        Inserts node into the binary heap
        :param node: dict - {'priority': int, 'command': <function>}
        :return: None
        """
        if not isinstance(node, dict) or not all(['priority' in node, 'command' in node]):
            raise ValueError("Expected node of type dict: {'priority': int, 'command': <function>}")
        if not callable(node.get('command')):
            raise TypeError(f"No callable command found in node: {node}")
        self.queue.append(node)
        self.heapify_up(len(self.queue) - 1)

    def insert_nodes(self, nodes: list) -> None:
        if not isinstance(nodes, list):
            raise ValueError("Expected list of nodes: [{'priority': int, 'command': <function>}, ...]")
        for node in nodes:
            self.insert_node(node)

    def pop_priority_node(self) -> dict:
        """
        Pops top node from binary heap. Top node contains the highest priority value.
        :return: node of type dict: {'priority': int, 'command': <function>}
        """
        first_node = self.queue.pop(0) if self.queue else {}
        if self.queue:
            last_node = self.queue.pop(-1)
            self.queue.insert(0, last_node)
            self.heapify_down(0)
        return first_node

    def exec_next_command(self):
        """
        Pops and executes the next top priority command
        :return None:
        """
        node = self.pop_priority_node()
        if node and callable(node.get('command')):
            func = node['command']
            func()

    def heapify_up(self, index: int) -> None:
        """
        Moves current node up binary heap until parent priority > current priority > child priorities
        :param index: index of current node
        :return: None
        """
        if self.has_parent_node(index):
            parent_node = self.get_parent_node(index)
            if parent_node and parent_node['priority'] < self.queue[index]['priority']:
                parent_index = self.get_parent_index(index)
                self.swap_nodes(parent_index, index)
                self.heapify_up(parent_index)

    def heapify_down(self, index: int) -> None:
        """
        Moves current node down binary heap until parent priority > current priority > child priorities
        :param index: index of current node
        :return: None
        """
        child_index = index
        if self.has_left_node(index):
            left_node = self.get_left_node(index)
            if left_node and left_node['priority'] > self.queue[index]['priority']:
                child_index = self.get_left_index(index)
        if self.has_right_node(index):
            right_node = self.get_right_node
            if right_node and right_node(index)['priority'] > self.queue[child_index]['priority']:
                child_index = self.get_right_index(index)
        if child_index != index:
            self.swap_nodes(index, child_index)
            self.heapify_down(child_index)


def print_test():
    print('test')


if __name__ == '__main__':
    import unittest
    q = PriorityQueue()
    nodes = [
        {'priority': 1, 'command': print_test},
        {'priority': 10, 'command': print_test},
        {'priority': 10, 'command': print_test},
        {'priority': 3, 'command': print_test},
        {'priority': 3, 'command': print_test},
        {'priority': 4, 'command': print_test},
        {'priority': 6, 'command': print_test},
        {'priority': 0, 'command': print_test}
    ]
    q.insert_nodes(nodes)
    # for i in q.queue:
    #     print(i)
    print(q.queue)
    q.exec_next_command()
    q.exec_next_command()
    q.exec_next_command()
    q.exec_next_command()
    q.exec_next_command()
    q.exec_next_command()
    q.exec_next_command()
    q.exec_next_command()
    q.exec_next_command()
    q.exec_next_command()
    q.exec_next_command()
    q.exec_next_command()
    q.exec_next_command()
    q.exec_next_command()
    print(q.queue)
