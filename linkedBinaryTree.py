# NODE CLASS
# constructor for value, parent, left and right
# BINARY TREE CLASS
# constructor for root of tree + size
# size
# insert
# print (in-order traversal)
# height
# contains (return boolean)
# find (return node or None)
# delete (get to later)

class Node:
    __slots__ = '_value', '_parent', '_left', '_right'
    def __init__(self, value, parent=None, left=None, right=None):
        self._value = value 
        self._parent = parent
        self._left = left 
        self._right = right 

    def is_leaf(self):
        if self._left == None and self._right == None:
            return True
        return False

class BinaryTree():
    def __init__(self):
        self._root = None 
        self._size = 0 
    
    def __len__(self):
        return self._size 
    
    def insert(self, value): 
        if self._root == None: 
            self._root = Node(value)
            self._size += 1 
            return True
        else:
            return self._insert(value, self._root)

    def _insert(self, value, cur_node):
        if value < cur_node._value:   # left side
            if cur_node._left == None:
                cur_node._left = Node(value, cur_node) # insert in new node and set parent
                self._size += 1
                return True
            else:
                return self._insert(value, cur_node._left)
        if value > cur_node._value: # right side 
            if cur_node._right == None:
                cur_node._right = Node(value, cur_node) # insert in new node and set parent 
                self._size += 1
                return True
            else: 
                return self._insert(value, cur_node._right)
        else: # value == current node 
            return print(f'Value not added: {value} already exists in tree')

    def inorder_print(self):
        if self._root == None:
            raise Exception("Binary Tree is empty")
        else: 
            self._inorder_print(self._root)
            print()

    def _inorder_print(self, cur_node):
        if cur_node != None:
            self._inorder_print(cur_node._left)  # traverse left side
            print(str(cur_node._value), end=', ')  # visit node
            self._inorder_print(cur_node._right)  # traverse right side

    def preorder_print(self):
        if self._root == None:
            raise Exception('Binary Tree is empty')
        else:
            self._preorder_print(self._root)
            print()

    def _preorder_print(self, cur_node):
        if cur_node != None:
            print(str(cur_node._value), end=', ')
            self._preorder_print(cur_node._left)
            self._preorder_print(cur_node._right)

    def postorder_print(self):
        if self._root == None:
            raise Exception('Binary Tree is empty')
        else:
            self._postorder_print(self._root)
            print()

    def _postorder_print(self, cur_node):
        if cur_node != None:
            self._postorder_print(cur_node._left)
            self._postorder_print(cur_node._right)
            print(str(cur_node._value), end=', ')

    def contains(self, value):
        return self._contains(value, self._root)
    
    def _contains(self, value, cur_node):
        if cur_node == None:
            return False                                       # value not found
        elif value == cur_node._value:
            return True                                        # found value
        elif value < cur_node._value:
            return self._contains(value, cur_node._left)       # search left subtree
        elif value > cur_node._value:
            return self._contains(value, cur_node._right)      # search right subtree

    def find(self, value):
        return self._find(value, self._root)
    
    def _find(self, value, cur_node):
        if cur_node == None:
            return None                                        # value not found
        elif value == cur_node._value:
            return cur_node                                     # found value - return node
        elif value < cur_node._value:
            return self._find(value, cur_node._left)            # search left subtree
        elif value > cur_node._value:
            return self._find(value, cur_node._right)           # search right subtree

    def height(self):
        return self._height(self._root)

    def _height(self, cur_node):
        if cur_node == None or cur_node.is_leaf():
            return 0
        else:
            return 1 + max(self._height(cur_node._left), self._height(cur_node._right)) #self._children if it wasnt a BST

    def delete(self, node):
        if node._left and node._right:
            raise ValueError("Cannot delete node with two children")
        child = node._left if node._left else node._right # get child which could be None
        if child is not None:
            child._parent = node._parent
        if node == self._root:
            self._root = child 
        else: 
            parent = node._parent 
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node                 # convention for deprecated node
        return node._value

    def is_binary_search_tree(self):
        return self._is_binary_search_tree(self._root)

    def _is_binary_search_tree(self, cur_node, min=-float('inf'), max=float('inf')):
        if cur_node == None:
            return True 
        print(f"checking node {cur_node._value} is between {min} and {max} (inclusive)")
        if cur_node._value < min or cur_node._value > max:
            return False
        return self._is_binary_search_tree(cur_node._left, min, cur_node._value - 1) and self._is_binary_search_tree(cur_node._right, cur_node._value + 1, max)


# tests
if __name__ == '__main__':
    from random import randint
    bst = BinaryTree()
    print(f'Starting length is {len(bst)}')
    print('Inserting 100 random integers')
    # for i in range(100):
    #     while bst.insert(randint(0, 1000)) is not True:
    #         continue
    bst.insert(5)
    bst.insert(8)
    bst.insert(2)
    bst.insert(7)
    bst.insert(4)
    bst.insert(1)
    bst.insert(10)
    bst.insert(1008)
    print(f'Length is {len(bst)}')
    print('Printing all values in tree in order...') 
    bst.inorder_print()   
    print(bst.contains(1008))    
    print(bst.find(1008)) 
    print(bst.height())
    print('Preorder traversal of tree...')
    bst.preorder_print()
    print('Postorder traversal of tree...')
    bst.postorder_print()
    node = bst.find(4)
    print("Deleted node with value of:", bst.delete(node))
    print(bst.is_binary_search_tree())

