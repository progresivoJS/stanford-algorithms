from collections import namedtuple


class _Node():
    def __init__(self, key, val, left=None, right=None, size=1):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        self.size = size


class BinarySearchTree():
    def __init__(self):
        self._root = None

    def _get(self, x, key):
        if x is None:
            raise KeyError

        if key < x.key:
            return self._get(x.left, key)
        elif key > x.key:
            return self._get(x.right, key)
        else:
            return x.val

    def __getitem__(self, key):
        return self._get(self._root, key)

    def _set(self, x, key, val):
        if x is None:
            return _Node(key, val)

        if key < x.key:
            x.left = self._set(x.left, key, val)
        elif key > x.key:
            x.right = self._set(x.right, key, val)
        else:
            x.val = val

        x.size = 1 + self._size(x.left) + self._size(x.right)
        return x

    def __setitem__(self, key, val):
        self._root = self._set(self._root, key, val)

    def _contains(self, x, key):
        if x is None:
            return False

        if key < x.key:
            return self._contains(x.left, key)
        elif key > x.key:
            return self._contains(x.right, key)
        else:
            return True

    def __contains__(self, key):
        return self._contains(self._root, key)

    def _inorder(self, x, a):
        if x is None:
            return
        self._inorder(x.left, a)
        a += [x.key]
        self._inorder(x.right, a)

    def __iter__(self):
        a = []
        self._inorder(self._root, a)
        return iter(a)

    def _floor(self, x, key):
        if x is None:
            return None
        if key < x.key:
            return self._floor(x.left, key)
        elif key > x.key:
            t = self._floor(x.right, key)
            if t is None:
                return x
            else:
                return t
        else:
            return x

    def floor(self, key):
        x = self._floor(self._root, key)
        return None if x is None else x.key

    def _ceiling(self, x, key):
        if x is None:
            return None
        if key > x.key:
            return self._ceiling(x.right, key)
        elif key < x.key:
            t = self._ceiling(x.left, key)
            if t is None:
                return x
            else:
                return t
        else:
            return x

    def ceiling(self, key):
        x = self._ceiling(self._root, key)
        return None if x is None else x.key

    def _size(self, x):
        if x is None:
            return 0
        else:
            return x.size

    def size(self):
        return self._size(self._root)

    def _rank(self, x, key):
        if x is None:
            return 0
        if key == x.key:
            return self._size(x.left)
        elif key < x.key:
            return self._rank(x.left, key)
        else:
            return 1 + self._size(x.left) + self._rank(x.right, key)

    def rank(self, key):
        return self._rank(self._root, key)

    def _select(self, x, k):
        if x is None:
            return None

        if 1 + self._size(x.left) == k:
            return x
        elif 1 + self._size(x.left) < k:
            return self._select(x.right, k - (1 + self._size(x.left)))
        else:
            return self._select(x.left, k)

    def select(self, k):
        x = self._select(self._root, k)
        return None if x is None else x.key


def main():
    st = BinarySearchTree()
    


if __name__ == "__main__":
    main()
