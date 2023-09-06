import random


class DSU:
    def __init__(self, n):
        self.parent = list(range(0, n + 1))
        self.count_sets = [0 for _ in range(n + 1)]
        self.n = n

    def find(self, x):
        if self.parent[x] != x:
            res_find = self.find(self.parent[x])
            self.parent[x] = res_find[0]
            self.count_sets[x] += res_find[1]
            return self.parent[x], self.count_sets[x]
        else:
            return x, 0

    def union(self, x, y):
        root_x, root_y = self.find(x)[0], self.find(y)[0]
        if root_x != root_y:
            if random.randint(0, 1):
                self.parent[root_x] = root_y
                self.count_sets[root_x] -= self.count_sets[root_y]
                self.count_sets[root_y] += 1
            else:
                self.parent[root_y] = root_x
                self.count_sets[root_y] -= self.count_sets[root_x]
                self.count_sets[root_x] += 1

    def get_response_answer_2(self, x, y):
        if self.find(x)[0] == self.find(y)[0]:
            return "YES"
        else:
            return "NO"

    def get_response_answer_3(self, x):
        root = self.find(x)
        return root[1] + self.count_sets[root[0]] + 1


if __name__ == '__main__':
    n, m = map(int, input().split())
    requests_list = []
    for _ in range(m):
        requests_list.append(list(map(int, input().split())))


    def get_answers(n, requests_list):
        dsu = DSU(n)
        for request in requests_list:
            if request[0] == 1:
                dsu.union(request[1], request[2])
            elif request[0] == 2:
                print(dsu.get_response_answer_2(request[1], request[2]))
            elif request[0] == 3:
                print(dsu.get_response_answer_3(request[1]))
        pass
    get_answers(n, requests_list)
