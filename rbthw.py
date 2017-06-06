from collections import deque


class Color(object):
    RED = True
    BLACK = False


class Node(object):
    key = None
    value = None
    left = None
    right = None
    color = None
    count = None

    def __init__(self, key, value=None, color=Color.BLACK):
        self.key = key
        self.value = value
        self.color = color
        self.count = 0

    def is_red(self):
        return self.color is Color.RED


class RedBlackTree(object):
    root = None

    @classmethod
    def from_lot(cls, keys):
        if not keys:
            return
        tree = cls()
        for k in keys:
            tree.put(k)
        return tree

    def as_lot(self, colored=False):
        tree_lot = []
        if not self.root:
            return tree_lot

        q = deque()
        nodes_in_current_level = 1
        nodes_in_next_level = 0
        q.append(self.root)

        while q:
            current_node = q.popleft()
            nodes_in_current_level -= 1
            if current_node:
                tree_lot.append('[%s]' % current_node.key
                                if colored and current_node.is_red() else current_node.key)
                q.append(current_node.left)
                q.append(current_node.right)
                nodes_in_next_level += 2
            if nodes_in_current_level == 0:
                nodes_in_current_level = nodes_in_next_level
                nodes_in_next_level = 0
        return tree_lot

    def put(self, key, value=None):
        self.root = self._put(key, value, self.root)
        self.root.color = Color.BLACK

    def _put(self, key, value=None, node=None):
        if node is None:
            return Node(key, value, Color.RED)
        if key < node.key:
            node.left = self._put(key, value, node.left)
        elif key > node.key:
            node.right = self._put(key, value, node.right)
        else:
            node.value = value

        if self.is_red(node.right) and not self.is_red(node.left):
            node = self.rotate_left(node)
        if self.is_red(node.left) and self.is_red(node.left.left):
            node = self.rotate_right(node)
        if self.is_red(node.left) and self.is_red(node.right):
            self.flip_colors(node)

        node.count = 1 + self._size(node.left) + self._size(node.right)

        return node

    def get(self, key):
        current = self.root
        while current is not None:
            if key < self.root.key:
                current = self.root.left
            elif key > self.root.key:
                current = self.root.right
            else:
                return current.value
        return None

    def size(self):
        return self._size(self.root)

    def _size(self, node):
        return 0 if node is None else node.count

    def is_red(self, node):
        if not node:
            return Color.BLACK
        return node.is_red()

    def rotate_left(self, node):
        assert self.is_red(node.right)
        node_right = node.right
        node.right = node_right.left
        node_right.left = node
        node_right.color = node.color
        node.color = Color.RED
        return node_right

    def rotate_right(self, node):
        assert self.is_red(node.left)
        node_left = node.left
        node.left = node_left.right
        node_left.right = node
        node_left.color = node.color
        node.color = Color.RED
        return node_left

    def flip_colors(self, node):
        assert not self.is_red(node)
        assert self.is_red(node.left)
        assert self.is_red(node.right)
        node.color = Color.RED
        node.left.color = Color.BLACK
        node.right.color = Color.BLACK

    def RedBlackTreesize(root):
        if root is None:
            return -1
        if root:
            if root.left:
                return 1 + RedBlackTreesize(root.left)
            if root.right:
                return 1 + RedBlackTreesize(root.right)
        else:
            return

if __name__ == '__main__':
    f = open("input.txt","r")
    lines = f.readlines()
    for line in lines:
        print(line)
    line = "".join(line)
    number =map(int,line)
    if number is int:
        print (number)
    if int(number)>0: #insert
        inp = number
        RedBlackTree.from_lot(inp)
        res = rbt.as_lot(colored = True)
        print res == res
        
    elif int(number)<0: #delete
        number = abs(int(number))
        RedBlackTree.get(number)
        
        
    else: #print
        RedBlackTreesize()
    
