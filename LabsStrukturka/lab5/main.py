from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preorder(root, result=None):
    if result is None:
        result = []
    if root:
        result.append(root.value)
        preorder(root.left, result)
        preorder(root.right, result)
    return result


def inorder(root, result=None):
    if result is None:
        result = []
    if root:
        inorder(root.left, result)
        result.append(root.value)
        inorder(root.right, result)
    return result


def postorder(root, result=None):
    if result is None:
        result = []
    if root:
        postorder(root.left, result)
        postorder(root.right, result)
        result.append(root.value)
    return result


def level_order(root):
    result = []
    if root is None:
        return result

    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


def count_paths_to_leaves(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_paths_to_leaves(root.left) + count_paths_to_leaves(root.right)


def create_test_tree_1():
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(20)
    return root


def create_test_tree_2():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    return root


def create_test_tree_3():
    return TreeNode(67)


def create_test_tree_4():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    return root


def test_tree(tree, name):
    print(f"\nДерево: {name}\n")
    print(f"Прямой обход (preorder):   {preorder(tree)}")
    print(f"Симметричный обход (inorder): {inorder(tree)}")
    print(f"Обратный обход (postorder): {postorder(tree)}")
    print(f"Обход в ширину (level_order): {level_order(tree)}")
    print(f"Количество путей от корня до листьев: {count_paths_to_leaves(tree)}")


if __name__ == "__main__":
    test_tree(create_test_tree_1(), "1 (разнообразное)")
    test_tree(create_test_tree_2(), "2 (только левые потомки)")
    test_tree(create_test_tree_3(), "3 (один узел)")
    test_tree(create_test_tree_4(), "4 (полное дерево)")
