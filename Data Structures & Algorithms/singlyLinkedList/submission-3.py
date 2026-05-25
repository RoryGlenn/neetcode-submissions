class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def _find_node(self, index) -> Node:
        curr = self.head
        count = 0
        while curr:
            if count == index:
                break
            curr = curr.next
            count += 1
        return curr

    def get(self, index: int) -> int:
        if index < self.size:
            if res := self._find_node(index):
                return res.val
        return -1

    def insertHead(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
        else:
            new_head = Node(val)
            new_head.next = self.head
            self.head = new_head
        self.size += 1

    def insertTail(self, val: int) -> None:
        if curr := self._find_node(self.size - 1):
            new_tail = Node(val)
            curr.next = new_tail
        else:
            # list is empty
            self.head = Node(val)
        self.size += 1


    def remove(self, index: int) -> bool:
        curr = self._find_node(index)
        if not curr:
            return False

        if index == 0:
            # remove head
            self.head = curr.next
            curr = None
        elif index - 1 == self.size:
            # remove tail
            curr = None
        else:
            # remove node in middle
            prev = self._find_node(index - 1)
            prev.next = curr.next
        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        curr = self.head
        result = []
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result
