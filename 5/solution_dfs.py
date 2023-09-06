def get_x(n, graph, min_weight, max_weight):
    def binsearch(l, r, check, params):
        while l < r:
            x = (l + r + 1) // 2
            if check(x, params):
                l = x
            else:
                r = x - 1
        return l

    def dfs(graph, vertex, visited, x):
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor[0] not in visited and neighbor[1] > x:
                dfs(graph, neighbor[0], visited, x)

    def get_amount_component(n, graph, x):
        visited = set()
        amount_component = 0
        for vertex in range(1, n + 1):
            if vertex not in visited:
                dfs(graph, vertex, visited, x)
                amount_component += 1
        return amount_component

    def check(x, init_amount):
        return get_amount_component(n, graph, x) == init_amount

    init_amount = get_amount_component(n, graph, min_weight)
    return binsearch(min_weight, max_weight, check, init_amount)


if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    min_weight, max_weight = 10 ** 9 + 1, 0
    for _ in range(m):
        first_vertex, second_vertex, weight = map(int, input().split())
        if weight < min_weight:
            min_weight = weight
        if weight > max_weight:
            max_weight = weight
        adj[first_vertex].append([second_vertex, weight])
        adj[second_vertex].append([first_vertex, weight])
    print(get_x(n, adj, min_weight - 1, max_weight))
