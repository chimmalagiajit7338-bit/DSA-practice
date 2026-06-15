class LinkedList:
    def __init__(self):
        self.head = None

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def ins_begg(self, data):
        nn = LinkedList.Node(data)
        nn.next = self.head
        self.head = nn

    def ins_end(self, data):
        nn = LinkedList.Node(data)
        if self.head is None:
            self.head = nn
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = nn

    def traversal(self):
        c = self.head
        while c:
            print(c.data, end=" -> ")
            c = c.next
        print("None")


# Testing
ll = LinkedList()
ll.ins_begg(10)
ll.ins_begg(20)
ll.ins_end(5)

ll.traversal()