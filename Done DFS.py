
edges=[[2,3,1], [0], [0,4],[0], [2]]
def dfs(edges):
    visited1=[False]*len(edges)
    x1=[]
    stack1=[0]
    def dfs_itr_visited_on_pop():
        while stack1:
            node=stack1.pop()
            if not visited1[node]:
                visited1[node]=True
                x1.append(node)
                for neighbor in edges[node]:
                    if not visited1[neighbor]:
                        stack1.append(neighbor)
        return x1
    visited2=[False]*len(edges)
    visited2[0]=True
    x2=[]
    stack2=[0]
    def dfs_itr_visited_on_push():
        while stack2:
            node=stack2.pop()
            x2.append(node)
            for neighbor in edges[node]:
                if visited2[neighbor]==False:
                    visited2[neighbor]=True
                    stack2.append(neighbor)
        return x2
    visited3=[False]*len(edges)
    x3=[]
    node3=0
    def dfs_rec_visited_on_pop(node3):
            if not visited3[node3]:
                visited3[node3]=True
                x3.append(node3)
                for neighbor in edges[node3]:
                    if not visited3[neighbor]:
                        dfs_rec_visited_on_pop(neighbor)
            return x3
    visited4=[False]*len(edges)
    visited4[0]=True
    x4=[]
    node4=0
    def dfs_rec_visited_on_push(node4):
            x4.append(node4)
            for neighbor in edges[node4]:
                if visited4[neighbor]==False:
                    visited4[neighbor]=True
                    dfs_rec_visited_on_push(neighbor)
            return x4
    return dfs_itr_visited_on_pop(), dfs_itr_visited_on_push(),dfs_rec_visited_on_pop(node3),dfs_rec_visited_on_push(node4)
print(dfs(edges))
