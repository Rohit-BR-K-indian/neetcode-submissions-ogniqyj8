class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [0] * capacity
        self.length = 0
        self.capacity = capacity

    def get(self, i: int) -> int:
        if i < 0 or i >= self.length:
            raise IndexError("index exceeded")
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        if i < 0 or i >= self.length:
            raise IndexError("index exceeded")
        self.arr[i] = n
        return None

    def pushback(self, n: int) -> None:
        if self.length >= self.capacity:
            self.resize()
        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        if self.length == 0:
            raise IndexError("empty")
        num = self.arr[self.length-1]
        self.length -= 1
        return num

    def resize(self) -> None:
        self.capacity *= 2
        new_arr = [0] * self.capacity
        for x in range(self.length):
            new_arr[x] = self.arr[x]
        
        self.arr = new_arr
        return None

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity
