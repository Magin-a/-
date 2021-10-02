#원형리스트(P.160)
class Node():
    def __init__(self):
        self.data = None
        self.link = None


# node1 = Node()
# node1.data = "다현"
# node1.link = node1


# node2 = Node()
# node2.data = "정연"
# node1.link = node2
# node2.link = node1

# node3 = Node()
# node3.data = "사나"
# node2.link = node3
# node3.link = node1

# node4 = Node()
# node4.data = "쯔위"
# node3.link = node4
# node4.link = node1

# current = node1
# print(current.data)
# while current.link != node1:
#     current= current.link
#     print(current.data)

#P.172
def printnode(start):
    current = start
    if current.link != None:
        return
    print(current.data)
    while current.link != start:
        current = current.link
        print(current.data)
    print()

memory = []
head, current, pre = None, None, None
dataArray = ["다현", "정연", "사나", "쯔위"]

if __name__ == "__main__":
    node = Node()
    node.data = dataArray[0]
    head = node
    node.link = head
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head
        memory.append(node)

    printnode(head)

# #P.178
# def insertdata(finddata, insertdata):
#     global pre, current, head

#     if head.data == finddata:
#         newnode = Node()
#         newnode.data = insertdata
#         newnode.link = head
#         current.link = newnode
    
    
#     current = head
#     while current.link != head:
#         pre = current
#         current = current.link
#         if finddata == current.data:
#             newnode = Node()
#             newnode.data = insertdata
#             newnode.link = pre.link
#             current.link = newnode
#             return



# #P.184
# def deletnode(deletnode):
#     global pre, current, memory, head

#     if current.data == deletnode:
#         current = head
#         head = head.link
#         last = head

#     while last.link != current:
#         last = last.link