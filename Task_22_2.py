class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
def get_max_sum(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return root.value
    left = get_max_sum(root.left)
    right = get_max_sum(root.right)
    return (left if left > right else right) + root.value
def print_rout(root,total):

    if total == 0 and root is None:
        return True
    if root is None:
        return False
    left = print_rout(root.left, total - root.value)
    right = False
    if not left:
        right = print_rout(root.right, total - root.value)
    if left or right:
        print(root.value, end=' ')
    return left or right

def printer(root):
    total = get_max_sum(root)
    print("Максимальная сумма от корня до вершины:",total)
    print("Максимальный путь:", end = ' ')
    print_rout(root, total)

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
tree.right.right = TreeNode(6)
tree.right.right.right = TreeNode(7)
tree.right.right.right.right = TreeNode(8)
tree.left.left.left = TreeNode(9)
tree.left.left.right = TreeNode(10)
tree.left.left.left.left = TreeNode(11)
tree.left.left.left.left.left = TreeNode(12)
tree.left.left.left.left.right = TreeNode(13)

print(printer(tree))








