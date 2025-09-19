def bellmanFord(V, edges, src):
        #code here
        t=[100000000]*V
        t[src]=0
        for i in range(V):
            for j in range(len(edges)):
                if t[edges[j][0]]!=100000000 and t[edges[j][0]]+edges[j][2]<t[edges[j][1]]:
                    if i==V-1:
                        return [-1]
                    t[edges[j][1]]=t[edges[j][0]]+edges[j][2]
        return t
print(bellmanFord(5,[[1, 3, 2], [4, 3, -1], [2, 4, 1], [1, 2, 1], [0, 1, 5]],0))