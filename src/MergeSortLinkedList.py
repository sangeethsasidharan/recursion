from src.LinkedList import LinkedList, Node


class MergeSortList:
    def merge_sort(self, node1, node2):
        merge_node = Node(0)
        if node1 is None:
            merge_node = node2
            return merge_node
        elif node2 is None:
            merge_node = node1
            return merge_node
        else:
            if node1.data < node2.data:
                merge_node = node1
                merge_node.next = self.merge_sort(node1.next, node2)
            else:
                merge_node = node2
                merge_node.next = self.merge_sort(node1, node2.next)
        return merge_node


n1 = Node(1)
n2 = Node(5)
n3 = Node(6)

n1.next = n2
n2.next = n3

n4 = Node(2)
n5 = Node(3)
n6 = Node(4)
n4.next = n5
n5.next = n6

lilist1 = LinkedList()
lilist2 = LinkedList()
lilist1.head = n1
lilist2.head = n4

obj = MergeSortList()
obj.merge_sort(lilist1.head, lilist2.head)
