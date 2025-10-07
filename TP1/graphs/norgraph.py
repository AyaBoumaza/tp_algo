import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()


a = int(input("Combien de sommets ? "))
print("Entrez les noms des sommets :")
for i in range(a):
    node = input(f"S{i+1}: ")
    G.add_node(node)

b = int(input("nombre d'arêtes ? "))
print("Entrez les arêtes comme ça sommet1 sommet2):")
for i in range(b):
    u, v = input(f"A{i+1}: ").split()
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

if nx.is_connected(G):
    print("Le graphe est connexe ")
else:
    print("Le graphe nest pas connexe ")

plt.figure(figsize=(6, 5))
nx.draw(G, with_labels=True, node_color='skyblue', node_size=800, font_weight='bold')
plt.title("Graphe non orienté")
plt.show()
