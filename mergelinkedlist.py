class ListNode:
    def __init__(self, value=0, next=None):
        # Ensure that the node value is within the specified range
        self.value = value
        self.next = next

def mergeTwoLists(list_a, list_b):
    # Create a dummy node to serve as the head of the merged list
    dummy = ListNode(0)
    # Create a pointer to traverse the merged list
    current = dummy
    
    while list_a and list_b:
        # Skip nodes with values greater than 100 or less than -100
        if not (-100 <= list_a.value <= 100):
            list_a = list_a.next
            continue
        if not (-100 <= list_b.value <= 100):
            list_b = list_b.next
            continue

        # Ensure that the node value is within the specified range
        merged_value = min(list_a.value, list_b.value)
        current.next = ListNode(merged_value)
        
        if list_a.value <= list_b.value:
            list_a = list_a.next
        else:
            list_b = list_b.next
        current = current.next
    
    # Append the remaining nodes from the non-empty list to the merged list
    current.next = list_a or list_b
    
    # Return the head of the merged list (excluding the dummy node)
    return dummy.next

# Test the code with the given example
list_a = ListNode(1)
list_a.next = ListNode(2)
list_a.next.next = ListNode(4)

list_b = ListNode(1)
list_b.next = ListNode(3)
list_b.next.next = ListNode(4)

# Merge the two lists
merged_list = mergeTwoLists(list_a, list_b)

# Print the merged list if it is not None
if merged_list is not None:
    print("Merged List:")
    current_merged = merged_list
    while current_merged:
        print(current_merged.value, end=" -> ")
        current_merged = current_merged.next
    print("None")