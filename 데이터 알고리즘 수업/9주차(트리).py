class Treenode():
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

# node1 = Treenode()
# node1.data = "화사"

# node2 = Treenode()
# node2.data = "솔라"
# node1.left = node2

# node3 = Treenode()
# node3.data = "문별"
# node1.right = node3

# print(node1.data)

# print(node1.left.data, node1.right.data)

node1 = Treenode()
node1.data = ""

def preder(node):
    if node == None:
        return

    print(node.data)
    preder(node.left)
    preder(node.right)


name = 6
node = Treenode()
node.data = name

memory = []
root = None
dataArray = ["블랭핑크", "레드벨렛", "마마무","에이핑크", "걸스데이", "트와이스"]

node = Treenode()
node.data = dataArray[0]
root = node
memory.append(node)

for name in dataArray[1:]:
    node = Treenode()
    node.data = name

    current = root 
    while True:
        if name < current.data:
            if current.left == None:
                current.left == node
                break
            current = current.left
        else:
            if current.right== None:
               current.right =node
               break
            current = current.right

    memory.append(node)
print("이진 트리 구성 끝")

finddata = ''

current = root
while True:
    if current.data == finddata:
        print("찾음")
        break
    
    elif finddata < current.data:
        if current.left ==None:
            print("없음")
            break
        current = current.left

    else:
        if current.data ==None:
            print("없음")
            break

deletdata = ''
current = root
parent = None
while True:
    if deletdata ==current.data:
        if current.left ==None and current.right == None:
            if parent.left == current:
                parent.left = None  
            else:
                parent.right = None
            del(current)

        elif current.left == None and current.right == None:
            if parent.left == current:
                parent.left = current.left
            else:
                parent.right = current.right
        
        elif current.left == None and current.right != None:
            if parent.left == current:
                parent.left = current.right
                break
            else:
                parent.right = current.left
                

    