import math
import time
import random

from util import show

"""
 points_x, points_y : 노드의 x좌표, y좌표
 dist : 거리행렬
 N : 노드 수
"""

# random destroy
def destroy(N, destroy_num, sol):
    destroy_list = random.sample(range(N), destroy_num)
    for d in destroy_list:
        sol.remove(d)
    return destroy_list

# random repair
def repair(sol, destroy_list):
    insertion_list = random.sample(range(len(sol)), len(destroy_list))
    for i in range(len(destroy_list)):
        sol.insert(insertion_list[i], destroy_list[i])
    return sol


def cal_dist(sol, dist):
    return sum(dist[sol[i - 1]][sol[i]] for i in range(len(sol)))


def large_neighbor_search(points_x, points_y, dist, N, time_limit=2):
    st = time.time()
    # 방문 순서
    sol = [i for i in range(N)]
    obj_val = cal_dist(sol, dist)
    accept_rate = 0.05
    destroy_num = math.ceil(N * 0.3)

    while time.time() - st < time_limit:
        destroy_list = destroy(N, destroy_num, sol)
        current_sol = repair(sol, destroy_list)
        current_obj = cal_dist(current_sol, dist)
        if current_obj < obj_val or random.random() < accept_rate:
            sol = current_sol
            obj_val = current_obj
            print(obj_val)
    print(sol)

    sol = sol + [sol[0]]
    show(points_x, points_y, sol, f"{obj_val}")
