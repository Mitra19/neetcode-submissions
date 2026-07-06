class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        # Initialize with fixed capacity containing default values
        self.arr = [0] * capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        # Resize automatically if the array is completely full
        if self.size == self.capacity:
            self.resize()
            
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        # Decrease size to soft-delete the last element
        self.size -= 1
        return self.arr[self.size]

    def resize(self) -> None:
        # Double the capacity capacity
        self.capacity = 2 * self.capacity
        # Create a new larger array and copy old elements over
        new_arr = [0] * self.capacity
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def getSize(self) -> int:
        return self.size
        
    def getCapacity(self) -> int:
        return self.capacity
