from src.BinaryTree import BinaryTree, Node


class BinaryTreeInsert:
    def insertNode(self, node, val):
        if node is None:
            return Node(val)

        if node.value > val:
            node.left = self.insertNode(node.left, val)
        else:
            node.right = self.insertNode(node.right, val)

        return node

    def printLeafNode(self, Node):
        if Node is None:
            return
        if (Node.left is None) & (Node.right is None):
            print(Node.value)
            return

        self.printLeafNode(Node.left)
        self.printLeafNode(Node.right)
        return






n60 = Node(60)
n85 = Node(85)
n130 = Node(130)

n80 = Node(80, n60, n85)
n120 = Node(120, right=n130)

n100 = Node(100, n80, n120)

obj = BinaryTreeInsert()
final_node=obj.insertNode(n100, 110)
obj.printLeafNode(final_node)
