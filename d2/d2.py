# find second largest node in the tree.
# with BST, in-order traversal will give all the nodes in sorted order.
# O(N)

# exploring the right node first
# called reverse in-order traversal
def sedond_largest(root):
    def inorder(node):
        if not node or conunt == 2:
            return
        if node.right:
            inorder(node.right)
        count += 1

        if count == 2:
            val = node.val
            return

        if node.left:
            inorder(node.left)
    count = 0
    val = None
    inorder(root)
    return val:wq



 
