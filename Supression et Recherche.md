# Suppression
    # ------------------------
    def _delete(self, node, key, logs):
        if node is None:
            logs.append(f"❌ Clé {key} introuvable.")
            return None
        if key < node.key:
            logs.append(f"⬅️ Aller à gauche depuis {node}")
            node.left = self._delete(node.left, key, logs)
        elif key > node.key:
            logs.append(f"➡️ Aller à droite depuis {node}")
            node.right = self._delete(node.right, key, logs)
        else:
            logs.append(f"🗑️ Suppression du nœud {node}")
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                # rotation selon le type de heap
                if (self.heap_type == "max" and node.left.priority < node.right.priority) or \
                   (self.heap_type == "min" and node.left.priority > node.right.priority):
                    node = self.rotate_left(node, logs)
                    node.left = self._delete(node.left, key, logs)
                else:
                    node = self.rotate_right(node, logs)
                    node.right = self._delete(node.right, key, logs)
        return node

    def delete(self, key):
        logs = [f"DELETE {key}"]
        self.root = self._delete(self.root, key, logs)
        logs.append("✅ Suppression terminée.")
        return logs

    # ------------------------
    # Recherche
    # ------------------------
    def search(self, key):
        logs = []
        node = self.root
        while node:
            logs.append(f"🔎 Visite {node}")
            if key == node.key:
                logs.append(f"✅ Trouvé {key} avec priorité {node.priority}")
                return True, logs, node
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        logs.append(f"❌ Clé {key} non trouvée.")
        return False, logs, None

    # ------------------------
    # Parcours
    # ------------------------
    def inorder(self):
        res = []
        def _in(n):
            if not n: return
            _in(n.left)
            res.append((n.key, n.priority))
            _in(n.right)
        _in(self.root)
        return res

    def postorder(self):
        res = []
        def _post(n):
            if not n: return
            _post(n.left)
            _post(n.right)
            res.append((n.key, n.priority))
        _post(self.root)
        return res

    def breadth_first(self):
        res = []
        if not self.root:
            return res
        q = deque([self.root])
        while q:
            node = q.popleft()
            res.append((node.key, node.priority))
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return res
