from binarytree import Node
import networkx as nx
import matplotlib.pyplot as plt
from hierarchy_pos import hierarchy_pos, add_edges, in_order

#ABR

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def find_min(node):
    """Find the node with minimum value in a subtree"""
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete(root, value):
    if root is None:
        return root
    if value < root.value:
        root.left = delete(root.left, value)
    elif value > root.value:
        root.right = delete(root.right, value)
    else:
    #one child node
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        
    #two child node
        temp = find_min(root.right)
        root.value = temp.value
        root.right = delete(root.right, temp.value)
    return root

def search(root, value):
    if root is None or root.value == value:
        return root
    if value < root.value:
        return search(root.left, value)
    return search(root.right, value)


values = list(map(int, input("Entrez les valeurs séparées par des espaces : ").split()))
root = None
for v in values:
    root = insert(root, v)

print("\nArbre Binaire de Recherche :")
print(root)


print("\nParcours in-ordre :")
in_order(root)
print()

G = nx.DiGraph()
add_edges(G, root)

pos = hierarchy_pos(G, root=root.value)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800, arrows=False)
plt.title("Arbre Binaire de Recherche ")
plt.show()

print("Hauteur:", root.height)
print("Taille:", root.size)
print("Équilibré:", root.is_balanced)

# Delete operations
while True:
    print("\nOptions:")
    print("1. Supprimer une valeur")
    print("2. Afficher l'arbre")
    print("3. Quitter")
    
    choice = input("Choisissez une option (1-3): ")
    
    if choice == '1':
        if root is None:
            print("L'arbre est vide!")
            continue
            
        value_to_delete = int(input("Entrez la valeur à supprimer: "))
        
        # Check if value exists
        if search(root, value_to_delete) is None:
            print(f"La valeur {value_to_delete} n'existe pas dans l'arbre.")
        else:
            root = delete(root, value_to_delete)
            print(f"Valeur {value_to_delete} supprimée.")
            
            
            if root is not None:
                G = nx.DiGraph()
                add_edges(G, root)
                pos = hierarchy_pos(G, root=root.value)
                plt.figure(figsize=(10, 6))
                nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=800, arrows=False)
                plt.title(f"Arbre après suppression de {value_to_delete}")
                plt.show()
                
                print("\nArbre après suppression:")
                print(root)
                print("Parcours in-ordre:")
                in_order(root)
                print()
                print("Hauteur:", root.height)
                print("Taille:", root.size)
                print("Équilibré:", root.is_balanced)
            else:
                print("L'arbre est maintenant vide.")
                
    elif choice == '2':
        if root is not None:
            G = nx.DiGraph()
            add_edges(G, root)
            pos = hierarchy_pos(G, root=root.value)
            plt.figure(figsize=(10, 6))
            nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800, arrows=False)
            plt.title("Arbre Binaire de Recherche Actuel")
            plt.show()
            
            print("\nArbre actuel:")
            print(root)
            print("Parcours in-ordre:")
            in_order(root)
            print()
            print("Hauteur:", root.height)
            print("Taille:", root.size)
            print("Équilibré:", root.is_balanced)
        else:
            print("L'arbre est vide!")
            
    elif choice == '3':
        print("Au revoir!")
        break
    else:
        print("Option invalide!")