class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if self.next is None:
            return f'{self.val}'
        
        return f'{self.val}->{self.next.__str__()}'