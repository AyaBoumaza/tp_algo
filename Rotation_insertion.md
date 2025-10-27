# Rotation et insertion 
#Rotation
    def rotate_right(self, y, logs=None):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        if logs is not None:
            logs.append(f"🔄 Rotation droite : pivot {y} -> nouveau root {x}")
        return x

    def rotate_left(self, x, logs=None):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        if logs is not None:
            logs.append(f"🔄 Rotation gauche : pivot {x} -> nouveau root {y}")
        return y

    # ------------------------
    # Insertion (BST + Heap)
    # ------------------------
    def _insert(self, node, key, priority, logs, path):
        if node is None:
            node = TreapNode(key, priority)
            logs.append(f"✅ Création du nœud {node}")
            path.append(('place', node.key, node.priority))
            return node

        if key == node.key:
            logs.append(f"⚠️ Clé {key} déjà existante ({node}), insertion ignorée.")
            return node

        if key < node.key:
            logs.append(f"➡️ Aller à gauche depuis {node}")
            node.left = self._insert(node.left, key, priority, logs, path)
            if node.left:
                if (self.heap_type == "max" and node.left.priority > node.priority) or \
                   (self.heap_type == "min" and node.left.priority < node.priority):
                    logs.append(f"⚠️ Violation de la propriété {self.heap_type}-heap à gauche ({node.left.priority} vs {node.priority})")
                    node = self.rotate_right(node, logs)
        else:
            logs.append(f"➡️ Aller à droite depuis {node}")
            node.right = self._insert(node.right, key, priority, logs, path)
            if node.right:
                if (self.heap_type == "max" and node.right.priority > node.priority) or \
                   (self.heap_type == "min" and node.right.priority < node.priority):
                    logs.append(f"⚠️ Violation de la propriété {self.heap_type}-heap à droite ({node.right.priority} vs {node.priority})")
                    node = self.rotate_left(node, logs)
        return node

    def insert(self, key, priority=None):
        logs = []
        path = []
        ptext = priority if priority is not None else 'aléatoire'
        logs.append(f"INSERTION {key} (priorité={ptext}, mode={self.heap_type.upper()}-HEAP)")
        self.root = self._insert(self.root, key, priority, logs, path)
        logs.append("✅ Insertion terminée.")
        return logs, path
