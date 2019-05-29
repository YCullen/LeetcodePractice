import ipdb

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def addTwoNumbers(l1,l2):
    head = ListNode(0)
    carry = 0 
    total = 0
    if not l1 == None:
        if not l2 == None:
            total = l1.val + l2.val
            carry = int(total/10)
            head.val = total%10 + carry
            l2 = l2.next
            l1 = l1.next
        elif:
            total = l1.val + 0
            head.

if __name__ == '__main__':
    a = ListNode(2)
    a.next = ListNode(4)
    a.next.next = ListNode(3)

    b = ListNode(5)
    b.next = ListNode(6)
    b.next.next = ListNode(4)

    ipdb.set_trace()
    print('done')
