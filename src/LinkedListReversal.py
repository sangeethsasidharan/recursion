from src.LinkedList import LinkedList, Node


class LinkedListReversal:
    def ReverseLinkedList(self, lilist, reversed_list):
        if lilist.next == None:
            reversed_list = lilist
            return reversed_list

        reversed_list = self.ReverseLinkedList(lilist.next, reversed_list)
        lilist.next.next = lilist
        lilist.next = None

        return reversed_list


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n1.next = n2
n2.next = n3

lilist = LinkedList()
revNode = Node(0)
lilist.head = n1

obj = LinkedListReversal()
revNode=obj.ReverseLinkedList(lilist.head, revNode)
print(revNode.next)

