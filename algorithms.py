import random
import sys
import time
from collections import deque

from util import *
from test_set import *

visited = [0] * (N + 1)


def backtracking(points_x, points_y, dist, N):
    global visited

    def bt(dist, N, x, acc, count, route, global_best=[], global_cost=10 ** 9):
        if count == N:
            if not dist[x][0]: return
            if acc + dist[x][0] < global_cost:
                global_cost = acc + dist[x][0]
                global_best = route + [0]
            return global_best, global_cost

        if global_cost <= acc:
            return global_best, global_cost

        for i in range(N):
            if not visited[i] and dist[x][i]:
                visited[i] = 1
                global_best, global_cost = bt(dist, N, i, acc + dist[x][i], count + 1, route + [i], global_best,
                                              global_cost)
                visited[i] = 0
        return global_best, global_cost

    st = time.time()
    visited[0] = 1
    result_route, result_cost = bt(dist, N, 0, 0, 1, [0])
    visited = [0] * (N + 1)
    print("backtracking------------------------------")
    print(f"cost : {result_cost}")
    print(f"route : {result_route}")
    print(f"소요시간 {time.time() - st}")
    show(points_x, points_y, result_route)


def greedy(points_x, points_y, dist, N, start=0):
    global visited
    visited = [0] * (N + 1)
    st = time.time()
    visited[start] = 1
    result_route = [start]
    result_cost = 0
    s = start
    for _ in range(N - 1):
        g = min((j for j in range(N) if not visited[j]), key=lambda j: dist[s][j])
        result_cost += dist[s][g]
        result_route.append(g)
        visited[g] = 1
        s = g
    result_cost += dist[s][start]
    result_route.append(start)
    print("greedy------------------------------")
    print(f"cost : {result_cost}")
    print(f"route : {result_route}")
    print(f"소요시간 {time.time() - st}")
    show(points_x, points_y, result_route)


def random_select(points_x, points_y, dist, N, start=0):
    global visited
    visited = [0] * (N + 1)
    st = time.time()
    visited[start] = 1
    result_route = [start]
    result_cost = 0
    s = start
    for _ in range(N - 1):
        g = random.choice([i for i in range(N) if not visited[i]])
        result_cost += dist[s][g]
        result_route.append(g)
        visited[g] = 1
        s = g
    result_cost += dist[s][start]
    result_route.append(start)
    print(f"cost : {result_cost}")
    print(f"route : {result_route}")
    print(f"소요시간 {time.time() - st}")
    show(points_x, points_y, result_route)


def eplsilon_greedy(points_x, points_y, dist, N, start=0, p=0.05):
    global visited
    visited = [0] * (N + 1)
    st = time.time()
    visited[start] = 1
    result_route = [start]
    result_cost = 0
    s = start
    for _ in range(N - 1):
        if random.random() < p:
            g_ = min((j for j in range(N) if not visited[j]), key=lambda j: dist[s][j])
            visited[g_] = 1
            g = min((j for j in range(N) if not visited[j]), key=lambda j: dist[s][j])
            visited[g_] = 0
        else:
            g = min((j for j in range(N) if not visited[j]), key=lambda j: dist[s][j])
        result_cost += dist[s][g]
        result_route.append(g)
        visited[g] = 1
        s = g
    result_cost += dist[s][start]
    result_route.append(start)
    print(f"cost : {result_cost}")
    print(f"route : {result_route}")
    print(f"소요시간 {time.time() - st}")
    show(points_x, points_y, result_route)


subroutine_visit = []


def greedy_select_route(points_x, points_y, dist, N):
    global subroutine_visit, visited

    def check_subroutine(c, cost, route, cnt):
        if len(route) == cnt:
            if cnt == N:
                return False, route, cost
            else:
                return True, [], cost
        subroutine = True
        result_route, result_cost = [], 0
        for n in graph[c]:
            if not subroutine_visit[n]:
                subroutine_visit[n] = True
                subroutine, result_route, result_cost = check_subroutine(n, cost + dist[c][n], route + [n], cnt)

        if subroutine and len(graph[c]) < 2:
            return False, [], 0
        if subroutine:
            return True, [], 0

        return subroutine, result_route, result_cost

    sys.setrecursionlimit(10 ** 9)
    visited = [0] * (N + 1)
    route_dist = []
    st = time.time()
    for i in range(N):
        for j in range(i + 1, N):
            route_dist.append((i, j, dist[i][j]))
    route_dist.sort(key=lambda x: -x[2])
    graph = [[] for _ in range(N)]
    cnt = 0
    while route_dist:
        i, j, d = route_dist.pop()
        if visited[i] > 1 or visited[j] > 1: continue
        cnt += 1
        graph[i].append(j)
        graph[j].append(i)
        visited[i] += 1
        visited[j] += 1
        subroutine_visit = [False] * N
        if cnt > 2:
            subroutine, result_route, result_cost = check_subroutine(i, 0, [], cnt)
            if len(result_route) == N:
                break
            if subroutine:
                cnt -= 1
                graph[i].pop()
                graph[j].pop()
                visited[i] -= 1
                visited[j] -= 1
    result_route = result_route + [result_route[0]]
    print("greedy select------------------------------")
    print(f"cost : {result_cost}")
    print(f"route : {result_route}")
    print(f"소요시간 {time.time() - st}")
    show(points_x, points_y, result_route)


def two_opt(points_x, points_y, dist, N):
    iteration = 0
    improved = True
    result_route = [i for i in range(N)] + [0]
    st = time.time()
    result_cost = sum(dist[result_route[i]][result_route[i + 1]] for i in range(N))
    show(points_x, points_y, result_route)
    while improved:
        iteration += 1
        show(points_x, points_y, result_route)
        improved = False
        for i in range(1, N - 1):
            for j in range(i + 1, N):
                # before : 기존 경로 / after : 변경된 부분
                before = (dist[result_route[i - 1]][result_route[i]] + dist[result_route[j]][result_route[j + 1]])
                after = (dist[result_route[i - 1]][result_route[j]] + dist[result_route[i]][result_route[j + 1]])
                if after - before < 0:
                    result_cost += after - before
                    result_route = result_route[:i] + list(reversed(result_route[i:j + 1])) + result_route[j + 1:]
                    improved = True
                    # show(points_x, points_y, result_route)
    print("2opt------------------------------")
    print(f"cost : {result_cost}")
    print(f"iteration : {iteration}")
    print(f"route : {result_route}")
    print(f"소요시간 {time.time() - st}")
    show(points_x, points_y, result_route)
