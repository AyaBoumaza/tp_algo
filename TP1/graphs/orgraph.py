import networkx as nx
import matplotlib.pyplot as plt


G = nx.DiGraph()


a = int(input("Combien de sommets ? "))
print("Entrez les noms des sommets :")
for i in range(a):
    node = input(f"S{i+1}: ").strip()
    G.add_node(node)

b = int(input("nombre d'arêtes ? "))
print("Entrez les arêtes comme ça sommet1 sommet2):")
for i in range(b):
    u, v = input(f"A{i+1}: ").split()
    u, v = u.strip(), v.strip()
    G.add_edge(u, v)


print("Sommets:", G.nodes())
print("Arêtes:", G.edges())
print("Nombre de sommets:", G.number_of_nodes())
print("Nombre darêtes:", G.number_of_edges())
print("Degrés de chaque sommet:")
for node, degree in G.degree():
    print(f"  {node}: {degree}")


density = nx.density(G)
print("Densité du graphe:", round(density, 3))

if nx.is_strongly_connected(G):
    print("Le graphe est connexe ")
else:
    print("Le graphe nest pas connexe ")

pos = nx.spring_layout(G)

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=800)

# Draw edges
nx.draw_networkx_edges(
    G, pos, 
    arrowstyle='->', arrowsize=20,      
    connectionstyle='arc3,rad=0.1',     # curved edges for loops
    edge_color='gray'
)

# Draw labels
nx.draw_networkx_labels(G, pos, font_weight='bold')
plt.title("Graphe orienté")
plt.show()
