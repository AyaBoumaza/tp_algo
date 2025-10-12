import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

try:
    n = int(input("Combien de sommets ? "))
except ValueError:
    print("Entrez un entier valide.")
    exit()

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
print("Entrez chaque arête sous la forme: sommet1 sommet2 poids (ex: A B 2.5)")
for i in range(m):
    line = input(f"A{i+1}: ").strip()
    if not line:
        continue
    parts = line.split()
    if len(parts) != 3:
        print(f"Format invalide pour A{i+1} : '{line}' (ignorée)")
        continue
    u, v, w_str = parts
    try:
        w = float(w_str)
    except ValueError:
        print(f"Poids invalide pour A{i+1} : '{w_str}' (ignorée)")
        continue
    G.add_edge(u, v, weight=w)

print("\nSommets :", list(G.nodes()))
print("Arêtes (avec poids) :", [(u, v, d['weight']) for u, v, d in G.edges(data=True)])
print("Nombre de sommets :", G.number_of_nodes())
print("Nombre d'arêtes :", G.number_of_edges())

print("\nDegré (non pondéré) de chaque sommet :")
for node, deg in G.degree():
    print(f"  {node} : {deg}")

print("\nDegré pondéré (somme des poids) de chaque sommet :")
for node, wdeg in G.degree(weight='weight'):
    print(f"  {node} : {wdeg}")

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
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=800, font_weight='bold')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
plt.title("Graphe pondéré (non orienté)")
plt.tight_layout()
plt.show()
