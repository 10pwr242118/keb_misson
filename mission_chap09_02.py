class Graph() :
    def __init__ (self, size, graph_name, node_names) :
        self.size = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]
        self.graph_name = graph_name
        self.node_names = node_names


    def print(self):
        print(f"{self.graph_name}")
        print()
        print("    ", end = '')  # 헹렬 우측 최상단, 여백 6칸
        for name in range(self.size):  # for 문으로 row 출력
            print(f"{self.node_names[name]}   " , end = '' )
        print()
        for name in range(self.size):  # for 문으로 coulmn 출력
            print(f"{self.node_names[name]}   " , end = '')
            for node in range(self.size):  # for 문으로 정점 하나씩 출력
                print(f"{self.graph[name][node]}   " , end = '')
            print ()
        print ()


# if __name__ == '__main__':
#     node_names=["a", "b", "c", "d", "e", "f"]
#     g = Graph(6, "해저터널 연결도",node_names)
#     g.print()

if __name__ == '__main__':

