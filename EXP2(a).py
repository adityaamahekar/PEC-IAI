import heapq

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'H': ['P'],
    'E': [],
    'F': [],
    'G': [],
    'P': []
}

heuristic = {
    'A': 10,
    'B': 8,
    'C': 6,
    'D': 7,
    'E': 5,
    'F': 4,
    'G': 2,
    'H': 3,
    'P': 0
}

start = 'A'
goal = 'P'

open_list = [(heuristic[start], start)]
closed = set()

while open_list:
    h, node = heapq.heappop(open_list)

    if node in closed:
        continue

    print(node, end=" ")

    if node == goal:
        print("\nGoal reached!")
        break

    closed.add(node)

    for neighbor in graph[node]:
        if neighbor not in closed:
            heapq.heappush(open_list,
                           (heuristic[neighbor], neighbor))