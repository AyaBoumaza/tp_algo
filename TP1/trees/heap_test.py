import streamlit as st
import heapq
import networkx as nx
import matplotlib.pyplot as plt

st.set_page_config(page_title="Heap Visualizer", layout="centered")

# --- Helper functions ---

def hierarchy_pos(G, root, width=1., vert_gap=0.3, vert_loc=0, xcenter=0.5):
    pos = {root: (xcenter, vert_loc)}
    children = list(G.successors(root))
    if not children:
        return pos
    dx = width / len(children)
    nextx = xcenter - width / 2 - dx / 2
    for child in children:
        nextx += dx
        pos.update(
            hierarchy_pos(G, child, width=dx, vert_gap=vert_gap,
                          vert_loc=vert_loc - vert_gap, xcenter=nextx)
        )
    return pos


def show_heap_tree(heap, is_max=False):
    if not heap:
        st.warning("(Heap is empty, nothing to display)")
        return

    values = [-x for x in heap] if is_max else heap
    G = nx.DiGraph()
    for i, val in enumerate(values):
        G.add_node(i, label=str(val))

    for i in range(len(values)):
        left, right = 2 * i + 1, 2 * i + 2
        if left < len(values):
            G.add_edge(i, left)
        if right < len(values):
            G.add_edge(i, right)

    pos = hierarchy_pos(G, 0)
    labels = nx.get_node_attributes(G, 'label')
    fig, ax = plt.subplots(figsize=(6, 4))
    nx.draw(G, pos, labels=labels, with_labels=True, node_size=800,
            node_color="lightblue", font_size=10, font_weight="bold", arrows=False, ax=ax)
    st.pyplot(fig)


# --- Session State Setup ---
if "heap" not in st.session_state:
    st.session_state.heap = []
if "is_max" not in st.session_state:
    st.session_state.is_max = False

# --- UI Layout ---
st.title("🧱 Heap Tree Visualizer (Min / Max Heap)")

heap_type = st.radio("Choose heap type:", ["Min Heap", "Max Heap"])
st.session_state.is_max = (heap_type == "Max Heap")

# --- Input for numbers ---
user_input = st.text_input("Enter numbers separated by spaces (e.g., 5 1 9 3):", "")

if st.button("Build Heap"):
    try:
        numbers = list(map(int, user_input.split()))
        if not numbers:
            st.warning("Please enter at least one number.")
        else:
            if st.session_state.is_max:
                st.session_state.heap = [-x for x in numbers]
                heapq.heapify(st.session_state.heap)
            else:
                st.session_state.heap = numbers
                heapq.heapify(st.session_state.heap)
            st.success("✅ Heap created successfully!")
    except ValueError:
        st.error("Please enter integers only.")

# --- Current heap display ---
if st.session_state.heap:
    st.subheader("Current Heap List:")
    heap_display = [-x for x in st.session_state.heap] if st.session_state.is_max else st.session_state.heap
    st.write(heap_display)

    # Buttons for insert / remove
    col1, col2, col3 = st.columns(3)
    with col1:
        val = st.number_input("Insert value", step=1)
        if st.button("Insert"):
            heapq.heappush(st.session_state.heap, -val if st.session_state.is_max else val)
            st.rerun()

    with col2:
        if st.button("Remove root"):
            if st.session_state.heap:
                removed = -heapq.heappop(st.session_state.heap) if st.session_state.is_max else heapq.heappop(st.session_state.heap)
                st.success(f"Removed root: {removed}")
                st.rerun()
            else:
                st.warning("Heap is empty.")

    with col3:
        if st.button("Reset Heap"):
            st.session_state.heap = []
            st.rerun()

    # --- Show heap tree ---
    show_heap_tree(st.session_state.heap, st.session_state.is_max)
