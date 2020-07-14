# NODE CLASS
# constructor for value, parent, left and right
# BINARY TREE CLASS
# constructor for root of tree + size
# size
# insert
# print (in-order traversal)
# height
# contains (return boolean)
# find (return node or false)
# delete (get to later)

class Node:
    __slots__ = '_value', '_parent', '_left', '_right'
    def __init__(self, value, parent=None, left=None, right=None):
        self._value = value 
        self._parent = parent
        self._left = left 
        self._right = right 

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



if __name__ == '__main__':
    from random import randint
    bst = BinaryTree()
    print(f'Starting length is {len(bst)}')
    print('Inserting 100 random integers')
    for i in range(100):
        while bst.insert(randint(0, 1000)) is not True:
            continue
    bst.insert(1008)
    print(f'Length is {len(bst)}')
    print('Printing all values in tree in order...') 
    bst.inorder_print()   
    print(bst.contains(500))     
