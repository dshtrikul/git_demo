from collections import deque

graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C', 'H'],
         'E': ['F'],
         'F': ['C'],
         'H': ['D']}


def regroup(path, lst=[]):
    for i in path:
        if len(i) > 1:
            regroup(i)
        else:
            lst.append(i[0])
    return lst


def find_shortest_path(graph, start, end):
    dict = {start: [start]}
    q = deque(start)
    while len(q):
        at = q.popleft()
        for next in graph[at]:
            if next not in dict:
                dict[next] = [dict[at], next]
                q.append(next)
    dict = regroup(dict.get(end))
    return (dict, len(dict))


path = find_shortest_path(graph, 'A', 'H')
print(path)

