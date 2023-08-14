def sum_bfs(node, adj_list, inputs):

    queue = [node]
    s = 0
    while queue:
        n = queue.pop(0)
        s += inputs[n]
        queue.extend(adj_list[n])

    return s

def drainagePartition(parent, inputs):

    adj_list = [[] for _ in range(len(parent))]
    for i in range(len(parent)):
        p = parent[i]
        if p != -1:
            adj_list[p].append(i)
    
    total = sum(inputs)
    min_diff = None
    for i in range(1, len(parent)):
        node_sum = sum_bfs(i, adj_list, inputs)
        diff = abs((total - node_sum) - node_sum)
        if min_diff is None or diff < min_diff:
            min_diff = diff

    return min_diff


parent = [-1, 0, 0, 1, 1, 2]
inputs  = [ 1, 2, 2, 1, 1, 1]

print(drainagePartition(parent, inputs))