from collections import defaultdict

class DFS_:
    def __init__(self):
        self.graphlist = defaultdict(list)

    # this function  will add edge
    def AddEdge(self,n,v):
        self.graphlist[n].append(v)

    def DFSfun(self,v,visited):
        visited[v] = True
        print(v,end= ' ')
        for i in self.graphlist[v]:
            if visited[i]==False:
                self.DFSfun(i,visited)

    def _dfs(self,v,l):
        visited = [False] * (max(self.graphlist)+l) # the list which will configure that the node is visited or not
        self.DFSfun(v,visited)





DFS_graph=DFS_()  # create object of  DFS class

l = int(input("Enter total number of Edges"))  # get total numbers of edges which are connected to nodes
for i in range(l):
    firstpoint = int(input("Enter first point")) # get the node which the edge moves to another node  means source node
    secondpoint = int(input("Enter Second point")) # destination node of edge
    DFS_graph.AddEdge(firstpoint,secondpoint)

startpoint = int(input("Enter starting point: "))
DFS_graph._dfs(startpoint,l)


