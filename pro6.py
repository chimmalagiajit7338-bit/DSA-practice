





class solution(object):
    def hasCycle(self, head):
        t = r = head
        while r and r.next:
            r = r.next.next
            t = t.next
            if r==t:
                return True
        return False
    def reverse(self):
        p = None
        c = self.head
        while c:
            n = c.next
            c.next = p
            p = c
            c = n
        self.head = p
l1.reverse()

