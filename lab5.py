if self.heap[index] > self.heap[parent]:
    class PriorityQueue:
        def __init__(self):
            self.data = []

        def add(self, value):
            self.data.append(value)
            self._upheap(len(self.data) - 1)

        def remove(self):
            if len(self.data) == 0:
                return None

            if len(self.data) == 1:
                return self.data.pop()

            root = self.data[0]
            self.data[0] = self.data.pop()
            self._downheap(0)
            return root
    def _upheap(self, i):
        parent = (i - 1) // 2

        while i > 0 and self.data[i] > self.data[parent]:
            self.data[i], self.data[parent] = self.data[parent], self.data[i]
            i = parent
            parent = (i - 1) // 2
    def _downheap(self, i):
        size = len(self.data)

        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i

            if left < size and self.data[left] > self.data[largest]:
                largest = left

            if right < size and self.data[right] > self.data[largest]:
                largest = right

            if largest == i:
                break

            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            i = largest
#REQD TEST:
pq = PriorityQueue()

pq.add(5)
pq.add(10)
pq.add(3)
pq.add(20)
pq.add(15)

print(pq.data)
# Root should be 20

print(pq.remove())  # 20
print(pq.remove())  # 15
print(pq.remove())  # 10
print(pq.remove())  # 5
print(pq.remove())  # 3