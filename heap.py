class Heap:
    def __init__(self, comparison_function):
        self.comparison_function = comparison_function
        self._data = []

    def __len__(self):
        return len(self._data)
    
    def insert(self, value):
        self._data.append(value)
        self._upheap(len(self._data) - 1)
    
    def extract(self):
        if len(self._data) == 0:
            raise IndexError('Extract from an empty heap')
        
        self._swap(0, len(self._data) - 1)
        value = self._data.pop()
        if self._data:
            self._downheap(0)
        return value
    
    def top(self):
        if len(self._data) == 0:
            raise IndexError('Top of an empty heap')
        
        return self._data[0]
    
    def _parent(self, j):
        return (j - 1) // 2
    
    def _left(self, j):
        return 2 * j + 1
    
    def _right(self, j):
        return 2 * j + 2
    
    def _has_left(self, j):
        return self._left(j) < len(self._data)
    
    def _has_right(self, j):
        return self._right(j) < len(self._data)
    
    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self.comparison_function(self._data[j], self._data[parent]):
            self._swap(j, parent)
            self._upheap(parent)

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self.comparison_function(self._data[right], self._data[left]):
                    small_child = right
            if self.comparison_function(self._data[small_child], self._data[j]):
                self._swap(j, small_child)
                self._downheap(small_child)

    def _heapify(self):
        start = self._parent(len(self._data) - 1)
        for j in range(start, -1, -1):
            self._downheap(j)