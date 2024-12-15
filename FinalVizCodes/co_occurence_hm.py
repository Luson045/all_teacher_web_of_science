import matplotlib.pyplot as plt
import matplotlib.cm as cm
import networkx as nx

G = nx.Graph()
for topic1 in co_occurrence_matrix.index:
    for topic2 in co_occurrence_matrix.columns:
        if co_occurrence_matrix.loc[topic1, topic2] > 0 and topic1 != topic2:
            G.add_edge(topic1, topic2, weight = co_occurrence_matrix.loc[topic1, topic2])

domain_professors = co_occurrence_matrix.sum(axis = 1)
node_sizes = [50 + 50 * domain_professors[node] for node in G.nodes]

node_cmap = cm.get_cmap("tab20", len(G.nodes))
node_colors = [node_cmap(i) for i, node in enumerate(G.nodes)]

edges = G.edges(data = True)
weights = [edge[2]['weight'] for edge in edges]
edge_colors = [cm.PuOr(w / max(weights)) for w in weights]

plt.figure(figsize = (30, 23))
pos = nx.spring_layout(G, k = 7)

nx.draw_networkx_nodes(G, pos, node_size = node_sizes, node_color = node_colors, alpha = 1)
nx.draw_networkx_edges(G, pos, width = [w * 0.3 for w in weights], edge_color = edge_colors, alpha = 0.7)
nx.draw_networkx_labels(G, pos, font_size = 12, font_weight = 'bold', font_color = 'black')

handles = [plt.Line2D([0], [0], marker = 'o', color = 'w', markerfacecolor = node_cmap(i), markersize = 5) 
           for i in range(len(G.nodes))]
plt.legend(handles, list(G.nodes), loc = 'upper left', title = 'Research Domains', fontsize = 8)

plt.title("Co-occurrence Network Graph for Research Categories", fontsize = 20, weight = 'bold')
plt.axis('off')
plt.savefig("/Users/harshvirmangla/Downloads/co_oc_2_blackened_hm.png", format = "png", dpi = 1000, bbox_inches = "tight")

plt.show()
