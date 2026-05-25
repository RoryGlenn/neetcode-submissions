class DynamicArray:
    def __init__(self, capacity: int):
        self.array = [0] * capacity
        self.capacity = capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.array[self.size] = n
        self.size += 1

    def popback(self) -> int:
        # result = self.array.pop(self.size-1)
        result = self.array[self.size-1]
        self.array[self.size-1] = 0
        self.size -= 1
        # self.capacity -= 1
        return result

    def resize(self) -> None:
        self.array = self.array + [0] * self.capacity
        self.capacity *= 2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
