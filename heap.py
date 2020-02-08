class Heap:
    def __init__(self, min):
        self.array = []
        self.pos   = {}
        self.size  = 0
        self.min   = min

    def compare(self, x, y):
        if self.min == True:
            return x < y
        else:
            return x > y

    def NewHeapNode(self, v, dist):
        return [v, dist]
        
    # A utility function to swap two nodes
    def SwapHeapNode(self, a, b):
        t = self.array[a]
        self.array[a] = self.array[b]
        self.array[b] = t

    def Push(self, v, dist):
        self.array.append(self.NewHeapNode(v, dist))
        self.pos[v] = self.size
        self.size += 1
        self.UpdateKey(v, dist)

    def HeapifyDown(self, parent_idx):

        key         = parent_idx
        left_child  = 2 * parent_idx + 1
        right_child = 2 * parent_idx + 2

        if left_child < self.size and self.compare(self.array[left_child][1], self.array[key][1]):
            key = left_child
        if right_child < self.size and self.compare(self.array[right_child][1], self.array[key][1]):
            key = right_child

        if key != parent_idx:
            # Update the position of the nodes
            self.pos[self.array[key][0]]        = parent_idx
            self.pos[self.array[parent_idx][0]] = key

            # Swap nodes
            self.SwapHeapNode(key, parent_idx)
            self.HeapifyDown(key)

    # Function to extract the root node from heap
    def Extract(self):
        # Return NULL if heap is empty
        if self.IsEmpty():
            return

        # Store the root node
        root = self.array[0]

        # Replace root node with last node
        last_node = self.array[self.size - 1]
        self.array[0] = last_node
        self.array.pop()

        # Update the position of the nodes
        self.pos[last_node[0]] = 0
        self.pos.pop(root[0], None)

        # Reduce heap size and heapify root
        self.size -= 1
        self.HeapifyDown(0)

        return root

    def IsEmpty(self):
        return True if self.size == 0 else False

    def UpdateKey(self, v, dist):
        # Get the index of v in heap array
        idx = self.pos[v]

        # Get the node and update its dist value
        self.array[idx][1] = dist

        # Heapify up this node
        while idx > 0 and self.compare(self.array[idx][1], self.array[int((idx - 1) / 2)][1]):
            # Swap thid node with its parent
            self.pos[self.array[idx][0]] = int((idx - 1) / 2)
            self.pos[self.array[int((idx - 1) / 2)][0]] = idx
            self.SwapHeapNode(idx, int((idx - 1) / 2))

            # Move to parent index
            idx = int((idx - 1) / 2)

    def IsInHeap(self, v):
        if v in self.pos.keys():
            return True
        return False
