def floydWarshall(dist):
    for k in range(len(dist)):
        for i in range(len(dist)):
            for j in range(len(dist)):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf') and dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist




print(floydWarshall([[0, 4, float('inf'), 5, float('inf')], [float('inf'), 0, 1,float('inf'), 6], [2, float('inf'), 0, 3, float('inf')], [float('inf'), float('inf'), 1, 0, 2], [1, float('inf'), float('inf'), 4, 0]]))
