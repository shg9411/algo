class Queue:
    def __init__(self, num):
        self.__maximum = num
        self.__queue = [None for _ in range(num+1)]
        self.__size = 0
        self.__front = 0
        self.__rear = 0

    def offer(self, num):
        if not self.isFull():
            self.__queue[self.__rear] = num
            self.__rear = (self.__rear+1) % (self.__maximum+1)
            self.__size += 1
        else:
            print("Queue is full")

    def peek(self):
        if not self.isEmpty():
            return "peek", self.__queue[self.__front]
        else:
            return "Queue is empty"

    def poll(self):
        if not self.isEmpty():
            val = self.__queue[self.__front]
            self.__size -= 1
            self.__front = (self.__front+1) % (self.__maximum+1)
            return "poll", val
        else:
            return "Queue is empty"

    def isEmpty(self):
        return self.__size == 0

    def isFull(self):
        return self.__size == self.__maximum


class QueueWithStack:
    def __init__(self):
        self.__front = []
        self.__rear = []
        self.__size = 0

    def offer(self, num):
        self.__rear.append(num)
        self.__size += 1

    def move(self):
        while self.__rear:
            self.__front.append(self.__rear.pop())

    def peek(self):
        if not self.isEmpty():
            if not self.__front:
                self.move()
            return "peek", self.__front[-1]
        else:
            return "Queue is empty"

    def poll(self):
        if not self.isEmpty():
            if not self.__front:
                self.move()
            self.__size -= 1
            return "poll", self.__front.pop()
        else:
            return "Queue is empty"

    def isEmpty(self):
        return self.__size == 0


# q.offer(num) 삽입
# print(q.peek()) 확인만
# print(q.poll()) 뽑아서 반환

print("# 배열 활용 큐")
q = Queue(2)
q.offer(3)
q.offer(4)
q.offer(5)
print(q.peek())
print(q.poll())
print(q.poll())
print(q.poll())

q = Queue(10)
print("1~10 offer")
for i in range(1, 11):
    q.offer(i)
print("poll")
for i in range(1, 11):
    print(q.poll())


print("\n# 스택 2개로 구현한 큐")
# []는 java의 스택과 같은 용도로 사용하였습니다.
q = QueueWithStack()
q.offer(3)
print(q.peek())
print(q.poll())
print(q.poll())


print("1~10 offer")
for i in range(1, 11):
    q.offer(i)
print("poll")
for i in range(1, 11):
    print(q.poll())
