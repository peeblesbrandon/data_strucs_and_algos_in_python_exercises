class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def lca(self, A, B, C):
        LCA = self._lca(A, B, C)
        if isinstance(LCA, TreeNode):
            return LCA.val
        return -1

    def _lca(self, node, val1, val2):
        if node is None:
            return False

        # search subtrees
        inLeft = self._lca(node.left, val1, val2)
        inRight = self._lca(node.right, val1, val2)

        # return LCA if already found
        if isinstance(inLeft, TreeNode):
            return inLeft
        elif isinstance(inRight, TreeNode):
            return inRight

        # determine results
        if inLeft and inRight:
            return node
        elif (inLeft or inRight) and (node.val == val1 or node.val == val2):
            return node
        elif inLeft or inRight or node.val == val1 or node.val == val2:
            return True
        else:
            return False


tree = TreeNode(3)
tree.left = TreeNode(1)

mySolution = Solution()
print(mySolution.lca(tree, 1, 3))