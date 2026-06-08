class TwoStacksQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, x):
        self.stack_in.append(x)

    def _transfer(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        self._transfer()
        return self.stack_out.pop()

    def front(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        self._transfer()
        return self.stack_out[-1]

    def size(self):
        return len(self.stack_in) + len(self.stack_out)

    def is_empty(self):
        return self.size() == 0

    def clear(self):
        self.stack_in.clear()
        self.stack_out.clear()

    def display(self):
        if self.is_empty():
            print("Очередь пуста")
            return
        self._transfer()
        print("Очередь:", self.stack_out[::-1] + self.stack_in)


if __name__ == "__main__":
    q = TwoStacksQueue()

    for i in range(1, 6):
        q.enqueue(i)
        print(f"enqueue({i})")

    q.display()
    print(f"Первый элемент: {q.front()}")
    print(f"Размер: {q.size()}")

    print(f"\ndequeue() -> {q.dequeue()}")
    q.display()

    print("\n=== Очистка очереди ===")
    q.clear()
    print(f"Очередь пуста: {q.is_empty()}")
    q.display()
