import numpy as np
from queue import Queue, PriorityQueue
from copy import deepcopy


def isValid(nums, current_pos):
    x = current_pos[0]
    y = current_pos[1]
    n = len(nums)
    if 0 <= x <= n - 1 and 0 <= y <= n - 1 and nums[x][y] == 0:
        return True
    else:
        return False


def solver(nums, start=[0, 0]):
    length = len(nums)
    goal = [length - 1, length - 1]
    four_directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    route = []

    def back(position=start, pos_list=None):
        if pos_list is None:
            pos_list = [start]
        if position == goal:
            route.append(pos_list)
        else:
            pos_x = position[0]
            pos_y = position[1]
            for direction in four_directions:
                next_position = [pos_x + direction[0], pos_y + direction[1]]
                if isValid(nums, next_position):
                    this_way = pos_list[:]
                    this_way.append(next_position)
                    nums[pos_x][pos_y] = 1
                    back(next_position, this_way)
                    nums[pos_x][pos_y] = 0

    back()
    return route


map = np.array(
    [
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]
    ])
map2 = np.array(
    [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 1, 0, 0, 0, 1],
        [0, 1, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0],
    ])


def track_route(nums, goal, start=(0, 0)):
    cur_pos = goal
    route = [goal]
    while cur_pos != start:
        x = cur_pos[0]
        y = cur_pos[1]
        last_pos = nums[x][y]
        route.append(last_pos)
        cur_pos = last_pos
    return route


def bfs(nums, start=[0, 0]):
    arr = deepcopy(nums)
    queue = Queue()
    queue.put(start)
    route = []
    n = len(arr)
    pre = [[None for _ in range(n)] for _ in range(n)]
    goal = [n - 1, n - 1]
    last_pos = start
    while not queue.empty():
        cur_pos = queue.get()
        pos_x = cur_pos[0]
        pos_y = cur_pos[1]
        # store last pos
        pre[pos_x][pos_y] = last_pos
        if cur_pos == goal:
            print("found exit")
            return
        for neighbors in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
            next_pos = [pos_x + neighbors[0], pos_y + neighbors[1]]
            if isValid(arr, next_pos):
                queue.put(next_pos)
        arr[pos_x][pos_y] = 1
        last_pos = cur_pos

    print('not able to find exit')


def shortest_path(nums, start=[0, 0]):
    arr = deepcopy(nums)
    pq = PriorityQueue()
    n = len(arr)
    pre = [[None for _ in range(n)] for _ in range(n)]
    distance = np.repeat(100, n * n).reshape((n, n))
    distance[start[0]][start[1]] = 0
    pq.put((distance[start[0]][start[1]], start))
    goal = [n - 1, n - 1]
    while not pq.empty():
        cur_pos = pq.get()[1]
        pos_x = cur_pos[0]
        pos_y = cur_pos[1]
        # store last pos
        if cur_pos == goal:
            print("found exit")
            return list(reversed(track_route(pre, goal)))
        for neighbor in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
            next_pos = [pos_x + neighbor[0], pos_y + neighbor[1]]
            if isValid(arr, next_pos):
                if distance[pos_x][pos_y] + 1 < distance[next_pos[0]][next_pos[1]]:
                    pq.put((1 + distance[pos_x][pos_y], next_pos))
                    distance[next_pos[0]][next_pos[1]] = distance[pos_x][pos_y] + 1
                    pre[next_pos[0]][next_pos[1]] = tuple(cur_pos)
        arr[pos_x][pos_y] = 1

    print('not able to find exit')


def heuristic(goal, curr):
    return abs(goal[0] - curr[0]) + abs(goal[1] - curr[1])


def a_star(nums, start=[0, 0]):
    arr = deepcopy(nums)
    pq = PriorityQueue()
    n = len(arr)
    goal = [n - 1, n - 1]
    pre = [[None for _ in range(n)] for _ in range(n)]
    distance = np.repeat(100, n * n).reshape((n, n))
    distance[start[0]][start[1]] = 0
    pq.put((0 + heuristic(goal, start), start))
    while not pq.empty():
        cur_pos = pq.get()[1]
        pos_x = cur_pos[0]
        pos_y = cur_pos[1]
        # store last pos
        if cur_pos == goal:
            print("found exit")
            return list(reversed(track_route(pre, goal)))
        for neighbor in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
            next_pos = [pos_x + neighbor[0], pos_y + neighbor[1]]
            if isValid(arr, next_pos):
                estimate = heuristic(goal, next_pos)
                if distance[pos_x][pos_y] + 1 < distance[next_pos[0]][next_pos[1]]:
                    pq.put((1 + distance[pos_x][pos_y] + estimate, next_pos))
                    distance[next_pos[0]][next_pos[1]] = distance[pos_x][pos_y] + 1 + estimate
                    pre[next_pos[0]][next_pos[1]] = tuple(cur_pos)
        arr[pos_x][pos_y] = 1

    print('not able to find exit')


b = shortest_path(map)
