G = nx.DiGraph()

for node, neighbors in g.graph.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor, weight=g.edge_costs.get((node, neighbor, 0)))

pos = nx.circular_layout(G)

node_labels = {node: f"{node}\nH: {g.static_heuristic.get(node, 0)}" for node in G.nodes}
edge_labels = {(node, neighbor): g.edge_costs.get((node, neighbor), 0) for node, neighbor in G.edges}

plt.figure(figsize=(15, 15))

nx.draw(G, pos, with_labels=True, labels=node_labels, node_size=700, node_color="skyblue", font_size=8)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
 