class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def linked_list_insert_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def linked_list_insert_end(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    
    curr = head
    while curr.next is not None:
        curr = curr.next
    curr.next = new_node
    return head

def linked_list_insert_any_position(head, data, index):
    if index == 0:
        return linked_list_insert_beginning(head, data)
    
    new_node = Node(data)
    curr = head
    curr_pointer = 0

    while curr is not None and curr_pointer < index-1:
        curr = curr.next
        curr_pointer+=1

    new_node.next = curr.next
    curr.next = new_node

    return head

def linked_list_delete_beginning(head):
    if head is None:
        return None
    return head.next

def linked_list_delete_end(head):
    if head is None:
        return None

    if head.next is None:
        # only one node
        return None
    
    curr = head
    while curr.next.next is not None:
        curr = curr.next
    
    curr.next = None
    return head


def linked_list_delete_any_position(head, index):
    if head is None:
        # empty list
        return None

    if index == 0:
        # delete first node
        return head.next
    
    curr=head
    curr_pointer = 0

    while curr is not None and curr_pointer < index-1:
        curr = curr.next
        curr_pointer+=1
    
    curr.next = curr.next.next
    return head
        

def print_list(head):
    curr = head
    res = []
    while curr:
        res.append(str(curr.data))
        curr = curr.next
    print(" -> ".join(res) if res else "Empty List")

def main():
    head = None
    print_list(head)

    # 1) Insert at beginning
    head = linked_list_insert_beginning(head, 10) 
    head = linked_list_insert_beginning(head, 5)    
    print("\nAfter inserting at beginning (5, 10):")
    print_list(head)

    # 2) Insert at end
    head = linked_list_insert_end(head, 20) 
    head = linked_list_insert_end(head, 25)         
    print("\nAfter inserting at end (20, 25):")
    print_list(head)

    head = linked_list_insert_any_position(head, 15, 2)
    print("\nAfter inserting 15 at index 2:")
    print_list(head)

    head = linked_list_insert_any_position(head, 1, 0)
    print("\nAfter inserting 1 at index 0 (using any_position):")
    print_list(head)


    head = linked_list_insert_any_position(head, 30, 6)
    print("\nAfter inserting 30 at last index:")
    print_list(head)

    # Delete from beginning
    head = linked_list_delete_beginning(head)      # [20, 30, 40, 50]
    print("\nAfter deleting from beginning:")
    print_list(head)

    # Delete from end
    head = linked_list_delete_end(head)            # [20, 30, 40]
    print("\nAfter deleting from end:")
    print_list(head)

    # Delete at position (0-based)
    head = linked_list_delete_any_position(head, 1)  # delete index 1 → [20, 40]
    print("\nAfter deleting node at index 1:")
    print_list(head)

    # Try deleting first element using any_position
    head = linked_list_delete_any_position(head, 0)  # [40]
    print("\nAfter deleting node at index 0 (using any_position):")
    print_list(head)



if __name__ == "__main__":
    main()
