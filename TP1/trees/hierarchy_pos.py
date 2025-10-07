import networkx as nx

def in_order(node):
    if node:
        in_order(node.left)
        print(node.value, end=" ")
        in_order(node.right)


#add_edges
def add_edges(graph, node, parent=None):
    if node:
        graph.add_node(node.value)
        if parent:
            graph.add_edge(parent.value, node.value)
        add_edges(graph, node.left, node)
        add_edges(graph, node.right, node)


# hierarchy_pos.py

def hierarchy_pos(G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
    """
    Compute hierarchical layout for a tree graph.
    Source: adapted from https://stackoverflow.com/a/29597209
    Parameters:
        - G: NetworkX graph (tree)
        - root: root node value
        - width: total horizontal space
        - vert_gap: gap between levels (vertical)
        - vert_loc: vertical starting point
        - xcenter: horizontal center of the tree
    Returns:
        - A dict of positions {node: (x, y)} for drawing with nx.draw()
    """
    pos = {}
    def _hierarchy_pos(G, root, leftmost, rightmost, current_vert_loc, parent=None, parsed=[]):
        if root not in parsed:
            parsed.append(root)
            pos[root] = ((leftmost + rightmost) / 2, current_vert_loc)
            neighbors = list(G.neighbors(root))
            if len(neighbors) != 0:
                dx = (rightmost - leftmost) / len(neighbors)
                nextx = leftmost
                for neighbor in neighbors:
                    nextx += dx
                    _hierarchy_pos(G, neighbor, nextx - dx, nextx, current_vert_loc - vert_gap, root, parsed)
        return pos
    return _hierarchy_pos(G, root, 0, width, vert_loc)
