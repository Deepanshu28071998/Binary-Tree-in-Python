class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


def height(root):
  if root is None:
    return 0
  else:
    return max(height(root.left), height(root.right)) + 1


# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Height of the binary tree is", height(root))
