import networkx as nx

input = open("input_day12.txt")
# Create a graph of programs
graph = nx.Graph()

for line in input:
    # Parse the line
    node, neighbors = line.strip().split(' <-> ')
    # Add edges defined by this line
    graph.add_edges_from((node, neighbor) for neighbor in neighbors.split(', '))

print('Part 1:', len(nx.node_connected_component(graph, '0')))
print('Part 2:', nx.number_connected_components(graph))