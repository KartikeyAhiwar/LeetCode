# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# Each node contains:
# - val: the value
# - next: pointer to the next node
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # 🔹 Step 1: Create a dummy node (starting point of merged list)
        # Why?
        # → Avoid edge cases (like empty list or first insertion confusion)
        # → Makes logic clean and uniform
        result = ListNode(0)
        
        # 🔹 'head' is a pointer that will build the merged list
        # It starts from dummy node and keeps moving forward
        head = result

        # 🔁 Step 2: Traverse both lists until one becomes empty
        while list1 and list2:
            
            # 🔍 Step 3: Compare current values of both lists
            # Always pick the smaller value → keeps list sorted
            if list1.val < list2.val:
                
                # 🔗 Attach node from list1 to merged list
                # IMPORTANT: We are NOT creating new nodes
                # → We are reusing existing nodes (called "splicing")
                head.next = list1
                
                # 👉 Move list1 forward
                list1 = list1.next
            
            else:
                # 🔗 Attach node from list2
                head.next = list2
                
                # 👉 Move list2 forward
                list2 = list2.next
            
            # 🔁 Move the 'head' pointer forward
            # (This is the builder of the new list)
            head = head.next

        # 🔚 Step 4: One list is finished
        # The other list may still have remaining elements
        
        # Since lists are already sorted:
        # → Just attach the remaining nodes directly
        # → No need to compare anymore
        head.next = list1 if list1 else list2

        # 🎯 Step 5: Return the merged list
        # We skip the dummy node using result.next
        return result.next