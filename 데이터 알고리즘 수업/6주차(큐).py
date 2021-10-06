#큐
queue = [None, None, None, None]
front, rear = -1

rear +=1
queue[rear] = "딸기"

rear += 1
queue[rear] = "바나나"

rear += 1
queue[rear] = "초코"



def dequeue():
    global front, rear, queue

    
    for _ in range(len(queue)-1):
        front += 1
        print(queue[front])
        queue[front] = None

    front = -1

dequeue()
print(queue)

def isqueuefull():
    global front, rear, queue
    
    if len(queue) != (rear - front):
        print("자리가 남았습니다.")
        return False
    else:
        print("큐가 가득 차 있습니다.")
        return True

def isqueueempty():
    global front, rear, queue
    
    if len(queue) != (rear - front):
        print("자리가 남았습니다.")
        return True
    else:
        print("큐가 가득 차 있습니다.")
        return False


def enqueue(data):
    global front, rear, queue

    if None  in queue:
       findindex = queue.index(None)
       queue[findindex] = data

enqueue("피스타치오")
print(queue)
    
