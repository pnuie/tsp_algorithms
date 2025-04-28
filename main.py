import random

from algorithms import *
from lns import large_neighbor_search
from test_set import *
from util import *

dist = get_distance(points_x, points_y)
# large_neighbor_search(points_x, points_y, dist, N)
# backtracking(points_x, points_y, dist, N)
# greedy(points_x, points_y, dist, N)
# greedy_select_route(points_x, points_y, dist, N)
two_opt(points_x, points_y, dist, N)

