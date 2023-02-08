
class bidirectional_node():
    def __init__ (self):
        self.data = None
        self.reverse = None
        self.right = None


def print_node(start):
    current = start
    if current.right == None:
        return
    print("right-->  ", end = '')
    print(current.data, end = '')
    while current.right != None:
        current = current.right
        print(current.data, end = '')
    print()
    print("reverse-->  ", end = '')
    print(current.data, end = '')
    while current.reverse != None:
        current = current.left
        print(current.data, end = '')

head, current, pre = None, None, None
data = ["a", "b", "c", "d", "e"]

if __name__ == '__main__':
    node = bidirectional_node()
    node.data = data[0]
    head = node
    
    for d in data[1:]:
        pre = node
        node = bidirectional_node()
        node.data = d
        pre.reverse = node
        node.right = pre

    print_node(head)