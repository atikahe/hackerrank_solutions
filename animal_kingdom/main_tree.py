

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def inorder(root):

    if not root:
        return

    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


def createTree(parent: list):
    # Create empty dictionary
    # To store index of each node
    d = {}

    # Create n new tree nodes, each having a value from 0 to n-1
    for i in range(len(parent)):
        d[i] = Node(i)
    # d = {0: Node(0), 1: Node(1), 2: Node(2), 3: Node(3), 4: Node(4), 5: Node(5), 6: Node(6), 7: Node(7), 8: Node(8), 9: Node(9)}
 
    # represents root
    root = None

    for i, e in enumerate(parent):
        if e == -1:
            root = d[i]
        else:
            prt = d[e]

            if prt.left is None:
                prt.left = d[i]
            else:
                prt.right = d[i]

    return root

def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)

        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1


def printLevelOrder(root):
    # Total of levels
    h = height(root)

    # Loop per level
    for i in range(1, h+1):
        printCurrentLevel(root, i)


def printCurrentLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data)
    elif level > 1:
        printCurrentLevel(root.left, level-1)
        printCurrentLevel(root.right, level-1)


if __name__ == "__main__":
    parent = [-1, 8, 6, 0, 7, 3, 8, 9, -1, 6]
    # parent = [-1, 0, 1]
    # parent = [-1, 0, 0, 1, 2, 2, 4, 4]

    root = createTree(parent)
    # inorder(root)
    printLevelOrder(root)

