import random
import math

class Node():
    def __init__ (self):
        self.data = None
        self.link = None


def distance(x,y):
    dist =math.sqrt(x**2 + y**2 )
    return dist


def printNodes(start) :
    current = start
    if current == None :
        return
    while current.link != None:
        current = current.link
        print(f'{current.data[0]} 편의점, 거리:{current.data[1]} ')

def makeSimpleLinkedList(convinience) :  
	global memory, head, current, pre

	node = Node()
	node.data = convinience
	memory.append(node)
	if head == None :			
		head = node
		return

	if head.data[1] > convinience[1] :	
		node.link = head
		head = node
		return

	current = head
	while current.link != None :
		pre = current
		current = current.link
		if current.data[1] > convinience[1]:
			pre.link = node
			node.link = current
			return

	current.link = node

memory = []
head, current, pre = None, None, None

data_array = []

if __name__ == '__main__':
    name_list= ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    for i in name_list:
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        dist = distance(x,y)
        temp = [i, dist]
        data_array.append(temp)
    
    for data in data_array:
            makeSimpleLinkedList(data)

    printNodes(head)
