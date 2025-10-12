import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()   


n = int(input("Combien de sommets ? "))               
print("Entrez les noms des sommets (un par ligne) :")
for i in range(n):
    name = input(f"S{i+1}: ").strip()
    if name:
        G.add_node(name)


if G.number_of_nodes() == 0:
    default_nodes = [f"S{i+1}" for i in range(n)]
    G.add_nodes_from(default_nodes)
    print("Aucun nom fourni — utilisation :", default_nodes)


m = int(input("Combien d'arêtes ? "))
print("Entrez chaque arête sous la forme : sommet1 sommet2 (ex: A B)")
for i in range(m):
    line = input(f"A{i+1}: ").strip()
    if not line:
        continue
    parts = line.split()
    if len(parts) != 2:
        print(f"Format invalide pour A{i+1} : '{line}' (ignorée)")
        continue
    u, v = parts
    G.add_edge(u, v)


print("\nSommets :", list(G.nodes()))
print("Arêtes :", list(G.edges()))
print("Nombre de sommets :", G.number_of_nodes())
print("Nombre d'arêtes :", G.number_of_edges())

print("\nDegré de chaque sommet :")
for node, deg in G.degree():
    print(f"  {node} : {deg}")

density = nx.density(G)
print("\nDensité du graphe :", round(density, 3))


if G.number_of_nodes() > 0:
    try:
        if nx.is_connected(G):
            print("Le graphe est connexe ✅")
        else:
            print("Le graphe n'est pas connexe ⚠️")
    except nx.NetworkXPointlessConcept:
        print("Test de connexité non applicable (graph vide ou trivial).")


pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(7, 5))
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color='lightgreen',
    node_size=800,
    font_weight='bold',
    edge_color='gray'
)
plt.title("Graphe non pondéré (non orienté)")
plt.tight_layout()
plt.show()
