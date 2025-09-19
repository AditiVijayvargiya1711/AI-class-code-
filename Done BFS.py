edges=[[2,3,1], [0], [0,4], [0], [2]]
def bfs(edges):
    queue1=[0]
    visited1=[False]*len(edges)
    x=[]
    queue2=[0]
    visited2=[False]*len(edges)
    visited2[0]=True
    y=[]
    def bfs_visited_on_pop():
        while queue1:
            node=queue1.pop(0)
            if not visited1[node]:
                x.append(node)
                visited1[node]=True
                for neighbor in edges[node]:
                    if not visited1[neighbor] and neighbor not in queue1:
                        queue1.append(neighbor)
        return x
    def bfs_visited_on_push():
        while queue2:
            node=queue2.pop(0)
            y.append(node)
            for neighbor in edges[node]:
                    if not visited2[neighbor]:
                        visited2[neighbor]=True
                        queue2.append(neighbor)
        return y
    return bfs_visited_on_pop(),bfs_visited_on_push()
    
print(bfs(edges))