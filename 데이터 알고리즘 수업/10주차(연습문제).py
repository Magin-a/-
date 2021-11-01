import random
class Treenode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

box = []
root = None
data = ["바나나우유", "레쓰비", "도시락", "삼다수"]
sellary = [random.choice(data) for _ in range(20)]

print("오늘 판매된 물건(중복O)", sellary)

node = Treenode()
node.data = sellary[0]
root = node
box.append(node)

for name in sellary[1:]:

    node = Treenode()
    node.data = name

    current = root