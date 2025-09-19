import heapq
def dijkstra(V, edges, src):
        dict1={}
        for k in range(len(edges)):
            if edges[k][0] in dict1:
                dict1[edges[k][0]][edges[k][1]]=edges[k][2]
            else:
                dict1[edges[k][0]]={edges[k][1]:edges[k][2]}
            if edges[k][1] in dict1:
                dict1[edges[k][1]][edges[k][0]]=edges[k][2]
            else:
                dict1[edges[k][1]]={edges[k][0]:edges[k][2]}
    
        x = [float('inf')]*V
        y=[0]*V
        x[src]=0
        heap = [(0, src)]
        while heap:
            d,node=heapq.heappop(heap)
            if y[node]==1:
                continue
            y[node]=1
            for i in dict1[node]:
                if d+dict1[node][i]<x[i]:
                    x[i]=d+dict1[node][i]
                    heapq.heappush(heap,[x[i],i])
        
        
        return x
print(dijkstra(3,[[0, 1, 1], [1, 2, 3], [0, 2, 6]],2))