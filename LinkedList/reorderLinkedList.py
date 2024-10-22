from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Utility function to print the linked list
    def __str__(self):
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result)

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # find tail node and place it in the cur varaible         
        current = head
        # tail = None
        prev = None
        while(current.next):
            prev = current
            current = current.next
            
        tail = current
        # print(current.val,prev.val)
        nextp = ListNode()
        curr = head
        # print()
        i = 0
        # while not (prev == nextp and prev == nextp.next):
        # while(i<2):
        while not (prev == nextp):
            nextp = curr.next
            curr.next = tail            
            tail.next = nextp
            prev.next = None
            tail = prev
            curr = nextp
            # i += 

        print(prev,tail,curr)
            
        # if prev == nextp:
        #     curr.next = nextp


        

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Test cases
def main():
    solution = Solution()

    # Test Case 1: Input list [1, 2, 3, 4]
    list1 = create_linked_list([1, 2, 3, 4])
    print("Original List 1: ", list1)
    solution.reorderList(list1)
    print("Reordered List 1: ", list1)
    
    print("\n")

    # Test Case 2: Input list [1, 2, 3, 4, 5]
    list2 = create_linked_list([1, 2, 3, 4, 5])
    print("Original List 2: ", list2)
    solution.reorderList(list2)
    print("Reordered List 2: ", list2)

    print("\n")

    # Test Case 3: Input list [1, 2, 3]
    list3 = create_linked_list([1, 2, 3])
    print("Original List 3: ", list3)
    solution.reorderList(list3)
    print("Reordered List 3: ", list3)

    print("\n")

    # Test Case 4: Input list [1, 2]
    list4 = create_linked_list([1, 2])
    print("Original List 4: ", list4)
    solution.reorderList(list4)
    print("Reordered List 4: ", list4)

    print("\n")

    # Test Case 5: Input list [1]
    list5 = create_linked_list([1])
    print("Original List 5: ", list5)
    solution.reorderList(list5)
    print("Reordered List 5: ", list5)

    print("\n")

    # Test Case 6: Empty list
    list6 = create_linked_list([])
    print("Original List 6: ", list6)
    solution.reorderList(list6)
    print("Reordered List 6: ", list6)

if __name__ == "__main__":
    main()
