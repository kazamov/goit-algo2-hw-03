import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

G = nx.DiGraph()

edges = [
    ('Термінал 1', 'Склад 1', 25),
    ('Термінал 1', 'Склад 2', 20),
    ('Термінал 1', 'Склад 3', 15),
    ('Термінал 2', 'Склад 3', 15),
    ('Термінал 2', 'Склад 4', 30),
    ('Термінал 2', 'Склад 2', 10),
    ('Склад 1', 'Магазин 1', 15),
    ('Склад 1', 'Магазин 2', 10),
    ('Склад 1', 'Магазин 3', 20),
    ('Склад 2', 'Магазин 4', 15),
    ('Склад 2', 'Магазин 5', 10),
    ('Склад 2', 'Магазин 6', 25),
    ('Склад 3', 'Магазин 7', 20),
    ('Склад 3', 'Магазин 8', 15),
    ('Склад 3', 'Магазин 9', 10),
    ('Склад 4', 'Магазин 10', 20),
    ('Склад 4', 'Магазин 11', 10),
    ('Склад 4', 'Магазин 12', 15),
    ('Склад 4', 'Магазин 13', 5),
    ('Склад 4', 'Магазин 14', 10),
]

G.add_weighted_edges_from(edges)

pos = {
    "Термінал 1": (-5, 0),
    "Термінал 2": (3, 0),
    "Склад 1": (-3, 3),
    "Склад 2": (1, 3),
    "Склад 3": (-3, -3),
    "Склад 4": (1, -3),
    "Магазин 1": (-7, 5),
    "Магазин 2": (-5, 5),
    "Магазин 3": (-3, 5),
    "Магазин 4": (-1, 5),
    "Магазин 5": (1, 5),
    "Магазин 6": (3, 5),
    "Магазин 7": (-7, -5),
    "Магазин 8": (-5, -5),
    "Магазин 9": (-3, -5),
    "Магазин 10": (-1, -5),
    "Магазин 11": (1, -5),
    "Магазин 12": (3, -5),
    "Магазин 13": (5, -5),
    "Магазин 14": (7, -5),
}

graph = [
  (  0,  0, 25, 20, 15,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0),
  (  0,  0,  0, 10, 15, 30,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0),
  (  0,  0,  0,  0,  0,  0, 15, 10, 20,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0),
  (  0,  0,  0,  0,  0,  0,  0,  0,  0, 15, 10, 25,  0,  0,  0,  0,  0,  0,  0,  0),
  (  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 20, 15, 10,  0,  0,  0,  0,  0),
  (  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 20, 10, 15,  5, 10),
  (  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0),
  (  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0),
  (  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0),
  (  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0),
  (  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0),
  (  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0),
  (  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0),
  (  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0),
  (  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0),
  (  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0),
  (  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0),
  (  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0),
  (  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0),
  (  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0),
]

sources = ['Термінал 1', 'Термінал 2']
sinks = ['Магазин 1', 'Магазин 2', 'Магазин 3', 'Магазин 4', 'Магазин 5', 'Магазин 6', 'Магазин 7', 'Магазин 8', 'Магазин 9', 'Магазин 10', 'Магазин 11', 'Магазин 12', 'Магазин 13', 'Магазин 14']

def draw_graph(G, pos):
    plt.figure(figsize=(15, 10))
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=12, font_weight="bold", arrows=True)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

def bfs(capacity_matrix, flow_matrix, source, sink, parent):
    visited = [False] * len(capacity_matrix)
    queue = deque([source])
    visited[source] = True

    while queue:
        current_node = queue.popleft()

        for neighbor in range(len(capacity_matrix)):
            # Перевірка, чи є залишкова пропускна здатність у каналі
            if not visited[neighbor] and capacity_matrix[current_node][neighbor] - flow_matrix[current_node][neighbor] > 0:
                parent[neighbor] = current_node
                visited[neighbor] = True
                if neighbor == sink:
                    return True
                queue.append(neighbor)

    return False

def edmonds_karp(capacity_matrix, source, sink):
    num_nodes = len(capacity_matrix)
    flow_matrix = [[0] * num_nodes for _ in range(num_nodes)]  # Ініціалізуємо матрицю потоку нулем
    parent = [-1] * num_nodes
    max_flow = 0

    while bfs(capacity_matrix, flow_matrix, source, sink, parent):
        path_flow = float('Inf')
        current_node = sink

        while current_node != source:
            previous_node = parent[current_node]
            path_flow = min(path_flow, capacity_matrix[previous_node][current_node] - flow_matrix[previous_node][current_node])
            current_node = previous_node

        current_node = sink
        while current_node != source:
            previous_node = parent[current_node]
            flow_matrix[previous_node][current_node] += path_flow
            flow_matrix[current_node][previous_node] -= path_flow
            current_node = previous_node

        max_flow += path_flow

    return max_flow


def run_task1():
    t = "╔══════════╤═══════════╤════════════════════╗"
    m = "╠══════════╪═══════════╪════════════════════╣"
    s = "╟──────────┼───────────┼────────────────────╢"
    b = "╚══════════╧═══════════╧════════════════════╝"
    r = "║{:^10}│{:^11}│{:^20}║"
    print(t)
    print(r.format('Термінал', 'Магазин', 'Максимальний потік'))
    for i in range(len(sources)):
      print(m)
      for j in range(len(sinks)):
        max_flow = edmonds_karp(graph, list(pos.keys()).index(sources[i]), list(pos.keys()).index(sinks[j]))
        if max_flow == 0: max_flow = '----'
        print (r.format(sources[i], sinks[j], max_flow))
        if j+1 != len(sinks): print(s)
    print(b)

    print('Короткий аналіз:')
    print('1. Алгоритм Едмондса-Карпа шукає оптимальний потік, тому досягнуто максимуму.')
    print('2. Вузькі маршрути (з малою пропускною здатністю) обмежують сумарний потік.')
    print('3. Магазини з мінімальним потоком можна покращити, збільшивши пропускні здатності критичних ребер.')
    print('4. Усунення вузьких місць покращує загальну ефективність логістичної мережі.')

    draw_graph(G, pos)

if __name__ == "__main__":
    run_task1()