class Graph():
    def __init__(self, graph_size) :
        self.size = graph_size
        self.graph = [[0 for _ in range(graph_size)]for _ in range(graph_size)]

def graph_generator_a(graph_str):
    splited_list = graph_str.split()
    edge_list= []
    for i in splited_list: edge_list.extend(i.split("-"))
    graph_size = int(sorted(edge_list, reverse=True)[0]) + 1
    graph = Graph(graph_size)
    for row, col in edge_list:
        graph.graph[row][col] = 1
        graph.graph[col][row] = 1
    return graph


def graph_generator(edge_str):
    global nodeName_data
    splited_list = edge_str.split()
    # print(splited_list)
    edge_list= []
    for i in splited_list: edge_list.extend(list(map(int, i.split("-"))))
    # print(edge_list)
    graph_size = int(sorted(edge_list, reverse=True)[0]) + 1
    # print(graph_size)
    graph = Graph(graph_size)
    for i in range(len(edge_list)):
        if i % 2 == 0:
            a = edge_list[i]
            b = edge_list[i+1]
            graph.graph[a][b] = 1
            graph.graph[b][a] = 1
    print("graph is generate")
    print_graph(graph)
    return graph


def print_graph(g) :
    global nodeName_data
    print('	', end='')
    for v in range(g.size) :
        print("%9s" % nodeName_data[v][0], end = ' ')
    print()
    for row in range(g.size) :
        print("%9s" %nodeName_data[row][0], end = ' ')
        for col in range(g.size) :
            print("%8d" % g.graph[row][col], end = ' ')
        print()
    print()


def graph_put_data(graph):
    global nodeName_data
    for idx in range(graph.size):
        graph.graph[idx][idx] = nodeName_data[idx][1]
    print("data is store in data")
    print_graph(graph)
    return graph


def find_max_stock(g):
    global nodeName_data

    stack = []
    visitedAry = []
    stock_temp= []

    # find init
    current = 0
    stack.append(current)
    visitedAry.append(current)
    stock_temp.append([current ,g.graph[current][current]])

    while (len(stack) != 0) :
        next = None
        for vertex in range(g.size-1) :
            if g.graph[current][vertex+1] == 1 :
                if vertex+1 in visitedAry :
                    pass
                else :
                    next = vertex+1
                    break

        if next != None :
            current = next
            stack.append(current)
            visitedAry.append(current)
            stock_temp.append([current ,g.graph[current][current]])
        else :
            current = stack.pop()
    # print(stock_temp)
    sorted_temp = sorted(stock_temp ,key=lambda x :x[1] , reverse=True)
    print(f"{nodeName_data[sorted_temp[0][0]][0]} has most honey-butter chip. Stock is {sorted_temp[0][1]}")


if __name__ == '__main__':
    str= "0-1 0-2 1-2 1-3 2-3 3-4"
    node_name="fuck fuck fuck fuck fuck"
    nodeName_data = [[i, 0] for i in node_name.split(" ")]
    nodeName_data = [['GS25', 30], ['CU', 60], ['Seven11', 10], ['MiniStop', 90], ['Emart24', 40]]

    graph_one=graph_generator(str)
    graph_one= graph_put_data(graph_one)
    find_max_stock(graph_one)

