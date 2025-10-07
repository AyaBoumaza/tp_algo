import networkx as nx
import matplotlib.pyplot as plt

def add_edges(graph, node, parent=None):
    if node:
        graph.add_node(node.cle)
        if parent:
            graph.add_edge(parent.cle, node.cle)
        add_edges(graph, node.gauche, node)
        add_edges(graph, node.droite, node)

def hierarchy_pos(G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
    pos = {}
    def _hierarchy_pos(G, root, leftmost, rightmost, current_vert_loc, parent=None, parsed=[]):
        if root not in parsed:
            parsed.append(root)
            pos[root] = ((leftmost + rightmost) / 2, current_vert_loc)
            neighbors = list(G.neighbors(root))
            dx = (rightmost - leftmost) / max(len(neighbors),1)
            nextx = leftmost
            for neighbor in neighbors:
                nextx += dx
                _hierarchy_pos(G, neighbor, nextx - dx, nextx, current_vert_loc - vert_gap, root, parsed)
        return pos
    return _hierarchy_pos(G, root, 0, width, vert_loc)

def dessiner_arbre(racine):
    if not racine:
        print("L'arbre est vide.")
        return
    G = nx.DiGraph()
    add_edges(G, racine)
    pos = hierarchy_pos(G, racine.cle)
    plt.figure(figsize=(12, 6))
    nx.draw(G, pos=pos, with_labels=True, arrows=False, node_size=2000, node_color="lightblue", font_size=12)
    plt.show()
