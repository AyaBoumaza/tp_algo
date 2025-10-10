import heapq
import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

def show_heap_tree(heap, is_max=False):
    """
    Display the heap as a tree using networkx and matplotlib.
    For a max heap, values are converted back to positive for display.
    """
    if not heap:
        print("(Heap is empty, nothing to display)")
        return

    # For max heap (stored as negatives)
    values = [-x for x in heap] if is_max else heap

    G = nx.DiGraph()

    # Add nodes
    for i, val in enumerate(values):
        G.add_node(i, label=str(val))

    # Add edges based on heap structure
    for i in range(len(values)):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(values):
            G.add_edge(i, left)
        if right < len(values):
            G.add_edge(i, right)

    # Compute positions for a tree layout
    pos = hierarchy_pos(G, 0)
    labels = nx.get_node_attributes(G, 'label')

    plt.figure(figsize=(6, 4))
    nx.draw(G, pos, labels=labels, with_labels=True, node_size=800,
            node_color="lightblue", font_size=10, font_weight="bold", arrows=False)
    plt.title("Heap Tree Representation")
    plt.show()


def hierarchy_pos(G, root, width=1., vert_gap=0.3, vert_loc=0, xcenter=0.5):
    """Recursively compute node positions for a tree-like layout."""
    pos = {root: (xcenter, vert_loc)}
    children = list(G.successors(root))
    if not children:
        return pos
    dx = width / len(children)
    nextx = xcenter - width/2 - dx/2
    for child in children:
        nextx += dx
        pos.update(hierarchy_pos(G, child, width=dx, vert_gap=vert_gap,
                                 vert_loc=vert_loc - vert_gap, xcenter=nextx))
    return pos



# Get user input for heap elements
while True:
    try:
        user_input = input("Enter numbers separated by spaces (e.g., 5 1 9 3): ")
        data = list(map(int, user_input.split()))
        if not data:
            print("List cannot be empty. Try again.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter integers only.")

# Main menu
while True:
    print("\nChoose heap type:")
    print("1. Min Heap")
    print("2. Max Heap")
    print("3. Exit")

    choice1 = input("Enter your choice: ").strip()

    if choice1 == "3":
        print("Exiting program.")
        break

    elif choice1 == "1":
        print("\nMIN HEAP\n")
        heapq.heapify(data)
        print("Initial heap:", data)
        show_heap_tree(data)

        while True:
            print("\nChoose an operation:")
            print("1. Insert a value")
            print("2. Remove root (min value)")
            print("3. Back to main menu")

            choice2 = input("Enter your choice: ").strip()

            if choice2 == "1":
                try:
                    val = int(input("Enter a value to insert: "))
                    heapq.heappush(data, val)
                    print("Heap after insertion:", data)
                    show_heap_tree(data)

                except ValueError:
                    print("Please enter a valid integer.")

            elif choice2 == "2":
                if data:
                    print("Removed smallest value:", heapq.heappop(data))
                    print("Heap after removing min:", data)
                    show_heap_tree(data)

                else:
                    print("Heap is empty, nothing to remove.")

            elif choice2 == "3":
                break
            else:
                print("Invalid choice, please enter 1..3.")

    elif choice1 == "2":
        print("\nMAX HEAP\n")
        max_heap = [-x for x in data]
        heapq.heapify(max_heap)
        print("Initial heap:", [-x for x in max_heap])


        while True:
            print("\nChoose an operation:")
            print("1. Insert a value")
            print("2. Remove root (max value)")
            print("3. Back to main menu")

            choice2 = input("Enter your choice: ").strip()

            if choice2 == "1":
                try:
                    val = int(input("Enter a value to insert: "))
                    heapq.heappush(max_heap, -val)
                    print("Heap after insertion:", [-x for x in max_heap])
                    show_heap_tree(data)

                except ValueError:
                    print("Please enter a valid integer.")

            elif choice2 == "2":
                if max_heap:
                    print("Removed largest value:", -heapq.heappop(max_heap))
                    print("Heap after removing max:", [-x for x in max_heap])
                    show_heap_tree(data)

                else:
                    print("Heap is empty, nothing to remove.")

            elif choice2 == "3":
                break
            else:
                print("Invalid choice, please enter 1..3.")

    else:
        print("Invalid choice, please enter 1..3.")
