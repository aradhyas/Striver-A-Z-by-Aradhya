class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverseList(self, head):
        # stack = [].  #this has O(N) for both time and space hence the other one which makes space O(1)
        # temp = head
        # while temp:
        #     stack.append(temp.val)
        #     temp = temp.next

        # temp = head

        # while temp:
        #     temp.val = stack.pop()
        #     temp = temp.next

        # return head

        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev
    
    def reverseList_recursive(self, head):
        if head is None or head.next is None:
            return head
        
        new_head = self.reverseList_recursive(head.next)
        head.next.next = head
        head.next = None

        return new_head
    
    def loop(self, head):
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow==fast:
                return True
        
        return False
    
    def head_of_loop(self, head):
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow==fast:
                slow = head
                while(slow!=fast):
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
    
    def length_of_loop(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                count = 1
                curr = slow.next
                while curr != slow:
                    count += 1
                    curr = curr.next
                return count

        return 0
    
    def check_palindrome(self,head):
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        #fast helps us to check whether our ll is even/odd length. if fast is None then it is odd and if fast.next is none then its even
        #so when length is odd we can skip the middle one because that one will be there only once in LL so we do slow=slow.next

        if fast is not None:
            slow = slow.next

        first = head
        second = self.reverseList(slow)
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        
        return True
    
    def even_odd(self,head):
        if head is None or head.next is None:
            return head
        
        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head
    

    def delete_at_position(self, head,n):
        if head is None:
            return None
        
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy
        while n:
            fast = fast.next
            n-=1
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next

        return dummy.next
    
    def delete_middle(self,head):
        if head is None or head.next is None:
            return None
        
        prev= None
        slow = head
        fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        return head

    def merge_for_two_ll(self,left,right):
        temp = ListNode(0)
        tail = temp

        while left is not None and right is not None:
            if left.val <= right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
            if left is not None:
                tail.next = left
            else:
                tail.next = right
        
        return temp.next
        
    def sortList(self, head):
        if head is None or head.next is None:
            return head
        prev = None
        slow = head
        fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None

        left = self.sortList(head)
        right = self.sortList(slow)

        return self.merge_for_two_ll(left, right)
    
    def length_ll(self, head):
        length = 0
        while(head!=None):
            length+=1
            head = head.next
        
        return length
    
    def intersection_of_two_linked_list(self, headA, headB):
        lenA = self.length_ll(headA)
        lenB = self.length_ll(headB)

        diff = abs(lenA - lenB)

        if lenA>lenB:
            while diff > 0:
                headA = headA.next
                diff-=1
        elif lenA<lenB:
            while diff > 0:
                headB = headB.next
                diff-=1

        while headA is not headB:
            headA = headA.next
            headB = headB.next
        return headA



def printList(head):
    temp = head
    result = []
    while temp:
        result.append(str(temp.val))
        temp = temp.next
    print(" → ".join(result))

# ---------- HELPERS TO BUILD LISTS ----------
def build_list(arr):
    dummy = ListNode(0)
    cur = dummy
    for x in arr:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next

def build_cycle_list(arr, pos):
    head = build_list(arr)
    if pos == -1:
        return head
    tail = head
    join = None
    idx = 0
    while tail.next:
        if idx == pos:
            join = tail
        tail = tail.next
        idx += 1
    if idx == pos:
        join = tail
    tail.next = join
    return head

sol = Solution()

head1 = build_list([1,2,3,4,5])
print("Original:")
printList(head1)

mid = sol.middleNode(head1)
print("Middle:", mid.val)

head2 = build_list([1,2,3,4,5])
rev = sol.reverseList(head2)
print("Reversed:")
printList(rev)

head3 = build_list([1,2,3,4,5])
rev2 = sol.reverseList_recursive(head3)
print("Reversed recursive:")
printList(rev2)

head_loop = build_cycle_list([1,2,3,4,5], pos=0)
print("Has loop?", sol.loop(head_loop))
loop_head = sol.head_of_loop(head_loop)
print("Loop head value:", loop_head.val if loop_head else None)
print("Loop length:", sol.length_of_loop(head_loop))

pal = build_list([1,2,3,2,1])
print("Palindrome?", sol.check_palindrome(pal))

eo = build_list([2,1,3,5,6,4,7])
eo_new_head = sol.even_odd(eo)
print("Odd-Even reorder:")
printList(eo_new_head)   # expected: 2 → 3 → 6 → 7 → 1 → 5 → 4

print("\nRemove Nth from end:")
del_head1 = build_list([1,2,3,4,5])
print("Before:")
printList(del_head1)
del_head1 = sol.delete_at_position(del_head1, 2)
print("After deleting 2nd from end:")
printList(del_head1) 

print("\nSort List:")
unsorted_head = build_list([4, 2, 1, 3])
print("Before:")
printList(unsorted_head)

sorted_head = sol.sortList(unsorted_head)
print("After:")
printList(sorted_head)