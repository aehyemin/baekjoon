from typing import Any
class FixedQueue:
    class Empty(Exception):
        pass
    class Full(Exception):
        pass

    def __init__(self,capacity:int) -> None:
        self.no = 0
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.que = [None] * capacity

    # def __len__(self) -> int:
    #     return self.no
    # def is_empty(self) -> bool:
    #     return self.no <= 0
    # def is_full(self) -> bool:
    #     return self.no >= self.capacity
    
    def enque(self, x: Any) -> None:
        self.que[self.rear] = x
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0

    def deque(self) -> Any:
            x = self.que[self.front]
            self.front += 1
            self.no -= 1
            if self.front == self.capacity:
                self.front = 0
            return x


def solve(N, K):
    queue = FixedQueue(N)
    for i in range(1, N+1):
        queue.enque(i)

    result = []
    while queue.no > 0:
        for i in range(K-1):
            queue.enque(queue.deque())
        result.append(queue.deque())

    print("<" + ", ".join(map(str, result)) + ">")


N,K = map(int, input().split())
solve(N, K)