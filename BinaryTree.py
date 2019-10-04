# Read this MF'er and learn what and how it does what it does
# insert/find are defined recursively
#
#
#
class Node(object):
    def __init__(self, payload=None):
        self.payload = payload
        self.left = None
        self.right = None

    # def __str__(self):
    #     return str(self.payload)


class Tree(object):
    def __init__(self):
        self.root = None

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(myTree.root, "")
        else: print("error")

    def preorder_print(self, start, traversal):
        # root ->left ->right
        if start:
            traversal += (str(start.payload) + " ")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def insert(self, payload):
        if self.root is None:
            self.root = Node(payload)
        else:
            self._insert(payload, self.root)

    def _insert(self, payload, current_node):
        if payload < current_node.payload:
            if current_node.left is None:
                current_node.left = Node(payload)
            else:
                self._insert(payload, current_node.left)

        elif payload > current_node.payload:
            if current_node.right is None:
                current_node.right = Node(payload)
            else:
                self._insert(payload, current_node.right)
        else:
            print("Payload already in tree")

    def find(self, payload):
        if self.root:
            is_found = self._find(payload, self.root)
            if is_found:
                return True
            else:
                return False
        else:
            return None

    def _find(self, payload, current_node):
        if payload > current_node.payload and current_node.right:
            return self._find(payload, current_node.right)
        if payload < current_node.payload and current_node.left:
            return self._find(payload, current_node.left)
        if payload == current_node.payload:
            return True

    def height(self, current_node):
        if current_node is None:
            return -1
        left_height = self.height(current_node.left)
        right_height = self.height(current_node.right)
        return 1 + max(left_height, right_height)


myTree = Tree()
#myTree.insert(4)
#myTree.insert(2)
#myTree.insert(5)
#myTree.insert(10)
#myTree.root = Node(0)
#myTree.root.left = Node(2)
#myTree.root.left.left = Node(4)
#myTree.root.left.right = Node(6)
#myTree.root.right = Node(7)
#myTree.root.right.left = Node(12)
#print (myTree.find(2))
#print (myTree.height(myTree.root))

prices = [10, 11, 12, 13, 15, 19, 14]
# least recent -------------->> most recent
for price in prices:
    myTree.insert(price)

z =myTree.print_tree("preorder").split()
x =[int(x) for x in z]
rank = [0 for elements in x]
max = -1;
counter = 0
for i in rank:
    if x[i] > max:
        max = x[i]
        rank[i] = 1
    counter = rank + counter
    if x[i] < max:
        rank[i] = counter
print(rank)