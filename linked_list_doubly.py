class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None  # pointer to previous node
        self.next = None  # pointer to next node


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # start of the list

    # ---------- INSERTIONS ----------

    def insert_front(self, data):
        """Insert a new node at the beginning."""
        new_node = Node(data)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def insert_end(self, data):
        """Insert a new node at the end."""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def insert_after(self, node, data):
        """Insert a new node after a given node object."""
        if node is None:
            return  # nothing to do

        new_node = Node(data)
        new_node.next = node.next
        new_node.prev = node

        if node.next:
            node.next.prev = new_node

        node.next = new_node

    # ---------- DELETIONS ----------

    def delete_front(self):
        """Delete node from the front (head)."""
        if self.head is None:
            return

        # move head forward
        self.head = self.head.next

        if self.head:
            self.head.prev = None

    def delete_end(self):
        """Delete node from the end (tail)."""
        if self.head is None:
            return

        # only one node
        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        # temp is last node
        temp.prev.next = None

    def delete_node(self, node):
        """Delete a given node object from the list."""
        if node is None:
            return

        # if node is head
        if node == self.head:
            self.delete_front()
            return

        # if node is in middle or end
        if node.prev:
            node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev

    # ---------- REVERSE ----------

    def reverse(self):
        """Reverse the doubly linked list in-place."""
        current = self.head
        temp = None

        while current:
            # swap prev and next
            temp = current.prev
            current.prev = current.next
            current.next = temp

            # move to 'next' node (which is previous before swap)
            current = current.prev

        # after loop, temp is at the old head's prev
        if temp:
            self.head = temp.prev

    # ---------- UTILS / DEBUG ----------

    def to_list(self):
        """Return list of data values from head to tail."""
        result = []
        temp = self.head
        while temp:
            result.append(temp.data)
            temp = temp.next
        return result

    def print_forward(self):
        """Print list from head to tail."""
        temp = self.head
        res = []
        while temp:
            res.append(str(temp.data))
            temp = temp.next
        print(" <-> ".join(res))

    def print_backward(self):
        """Print list from tail to head (to verify prev pointers)."""
        if self.head is None:
            print("(empty)")
            return

        # go to tail
        temp = self.head
        while temp.next:
            temp = temp.next

        # traverse backward
        res = []
        while temp:
            res.append(str(temp.data))
            temp = temp.prev
        print(" <-> ".join(res))

dll = DoublyLinkedList()

dll.insert_end(10)
dll.insert_end(20)
dll.insert_end(30)
dll.insert_front(5)

dll.print_forward()    # 5 <-> 10 <-> 20 <-> 30
dll.print_backward()   # 30 <-> 20 <-> 10 <-> 5

dll.reverse()
dll.print_forward()    # 30 <-> 20 <-> 10 <-> 5
