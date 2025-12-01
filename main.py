import stack
import queue

q = queue.Queue()
s = stack.Stack(None)

if __name__ == "__main__":
    q.enqueue(5)
    s.push(5)
    item = s.peek()
    print(item)
    item = q.peek()
    print(item)
    q.dequeue()
    s.pop()
    item = s.peek()
    print(item)
    item = q.peek()
    print(item)