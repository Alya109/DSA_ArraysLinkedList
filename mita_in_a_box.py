import numpy as np

class MitaInABox:
    def __init__(self, data, capacity=None, dtype=np.int32):
        if capacity is None:
            capacity = len(data)

        if len(data) > capacity:
            raise ValueError("Initial data exceeds capacity")

        self.capacity = capacity
        self.size = len(data)
        self.array = np.zeros(capacity, dtype=dtype)

        for i in range(self.size):
            self.array[i] = data[i]

    def display(self):
        print("Used:", self.array[:self.size])
        print("Size:", self.size)
        print("Capacity:", self.capacity)

    def visualize(self):
        for i in range(self.capacity):
            if i < self.size:
                print(f"[{i}:{self.array[i]}]", end=" ")
            else:
                print(f"[{i}: ]", end=" ")
        print()

    def access(self, index):
        index = int(index)
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        return self.array[index]

    def modify(self, index, value):
        index = int(index)
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        self.array[index] = value

    def search(self, value):
        for i in range(self.size):
            if self.array[i] == value:
                return i
        return -1

    def insert(self, index, value):
        index = int(index)

        if self.size == self.capacity:
            raise OverflowError("Array is full (resize required)")

        if index < 0 or index > self.size:
            raise IndexError("Index out of range")

        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]

        self.array[index] = value
        self.size += 1

    def delete(self, index):
        index = int(index)

        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]

        self.array[self.size - 1] = 0
        self.size -= 1

    def resize_visual(self, new_capacity):
        if new_capacity < self.size:
            raise ValueError("New capacity must be >= current size")

        print("\n--- RESIZE START ---")
        print("Old array:")
        self.visualize()

        new_array = np.zeros(new_capacity, dtype=self.array.dtype)

        print("\nCopying elements:")

        for i in range(self.size):
            new_array[i] = self.array[i]

            # visualize copy step
            print(f"Copied index {i}")
            for j in range(new_capacity):
                if j <= i:
                    print(f"[{j}:{new_array[j]}]", end=" ")
                else:
                    print(f"[{j}: ]", end=" ")
            print()

        self.array = new_array
        self.capacity = new_capacity

        print("\nResize complete.")
        self.visualize()

# box = MitaInABox([1, 2, 3, 4, 5], capacity=5)

# box.visualize()

# # array is full → insert will fail
# box.insert(5, 99)

# box.resize_visual(8)

# box.insert(5, 99)
# box.visualize()
