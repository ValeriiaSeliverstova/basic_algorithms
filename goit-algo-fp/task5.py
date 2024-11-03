import uuid
import networkx as nx
import matplotlib.pyplot as plt
import heapq

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, visited_colors):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [visited_colors.get(node[0], "#1296F0") for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def build_heap_tree(heap):
    heapq.heapify(heap)
    nodes = [Node(val) for val in heap]
    n = len(nodes)
    for i in range(n):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < n:
            nodes[i].left = nodes[left_index]
        if right_index < n:
            nodes[i].right = nodes[right_index]
    return nodes[0] if nodes else None

def generate_color_sequence(steps):
    colors = []
    for i in range(steps):
        shade = hex(128 + int(127 * i / steps))[2:]
        color = f"#{shade}{shade}{shade}"
        colors.append(color)
    return colors

def depth_first_search(tree_root):
    stack = [tree_root]
    visited_colors = {}
    colors = generate_color_sequence(len(stack))

    step = 0
    while stack:
        node = stack.pop()
        if node and node.id not in visited_colors:
            visited_colors[node.id] = colors[step % len(colors)]
            step += 1
            stack.append(node.right)
            stack.append(node.left)
            draw_tree(tree_root, visited_colors)
    return visited_colors

def breadth_first_search(tree_root):
    queue = [tree_root]
    visited_colors = {}
    colors = generate_color_sequence(len(queue))

    step = 0
    while queue:
        node = queue.pop(0)
        if node and node.id not in visited_colors:
            visited_colors[node.id] = colors[step % len(colors)]
            step += 1
            queue.append(node.left)
            queue.append(node.right)
            draw_tree(tree_root, visited_colors)
    return visited_colors

# Приклад використання з бінарною купою
heap = [10, 4, 5, 0, 1, 3]
root = build_heap_tree(heap)

print("Обхід у глибину:")
depth_first_search(root)

print("Обхід у ширину:")
breadth_first_search(root)
