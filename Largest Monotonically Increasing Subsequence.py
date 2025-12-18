from graphviz import Digraph
from collections import defaultdict

def LMIS(arr):
    n = len(arr)
    if n == 0:
        return [], 0
    
    dp = [1] * n
    parent = [[] for _ in range(n)]
    
    # Hitung dp dan parent
    for i in range(1, n):
        for j in range(0, i):
            if arr[j] < arr[i]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = [j]
                elif dp[j] + 1 == dp[i]:
                    parent[i].append(j)
    
    # Cari panjang LMIS maksimum
    max_length = max(dp)
    
    # Cari semua index yang memiliki LMIS maksimum
    end_indices = [i for i in range(n) if dp[i] == max_length]
    
    # Backtrack untuk menemukan semua path 
    all_paths = []
    
    def backtrack(idx, path):
        path = [idx] + path
        if dp[idx] == 1:
            all_paths.append(path)
            return
        for p in parent[idx]:
            backtrack(p, path)
    
    for end_idx in end_indices:
        backtrack(end_idx, [])
    
    return all_paths, max_length

def visualize_LMIS_tree(arr):
    
    paths, max_length = LMIS(arr)
    
    # Buat Digraph
    dot = Digraph(comment='LMIS Tree Visualization')
    dot.attr(rankdir='TB')
    dot.attr('node', shape='circle', style='', fillcolor='white', 
            fontname='Arial', fontsize='16', width='0.6', height='0.6')
    dot.attr('edge', color='black', penwidth='1.5')
    dot.attr(splines='line')
    
    # Tracking untuk node yang sudah dibuat per level dan nilai
    node_counter = [0]
    
    def get_or_create_node(value, depth, parent_id):
        node_id = f'node_{node_counter[0]}'
        node_counter[0] += 1
        dot.node(node_id, str(value))
        return node_id
    
    # Buat root node
    root_id = 'root'
    dot.node(root_id, '', shape='circle', width='0.5', height='0.5')
    
    # Dictionary untuk menyimpan nodes per level untuk ranking
    levels = defaultdict(list)
    
    # Fungsi rekursif untuk membangun tree
    def build_tree(idx, depth, parent_id, visited):
        if idx in visited:
            return
        
        visited = visited | {idx}
        value = arr[idx]
        
        # Buat node baru
        node_id = get_or_create_node(value, depth, parent_id)
        levels[depth].append(node_id)
        
        # Tambahkan edge dari parent
        if parent_id is not None:
            dot.edge(parent_id, node_id)
        
        # Cari semua elemen berikutnya yang lebih besar
        for next_idx in range(idx + 1, len(arr)):
            if arr[next_idx] > value:
                build_tree(next_idx, depth + 1, node_id, visited)
    
    # Build tree dari setiap elemen sebagai starting point
    for i in range(len(arr)):
        build_tree(i, 1, root_id, set())
    
    # Tambahkan ranking untuk setiap level agar lebih rapi
    for depth in sorted(levels.keys()):
        if depth > 0:
            with dot.subgraph() as s:
                s.attr(rank='same')
                for node_id in levels[depth]:
                    s.node(node_id)
    
    return dot, paths, max_length

if __name__ == "__main__":
    # contoh soal:
    # [4, 1, 13, 7, 0, 2, 8, 11, 3]
    # [3, 10, 2, 1, 20]

    input = input("Masukkan deretan angka (pisahkan dengan spasi): ")
    arr = list(map(int, input.replace(',', ' ').split()))
    
    print(f"Array: {arr}")
    
    # Cari semua LMIS paths
    paths, max_length = LMIS(arr)
    
    print(f"Panjang LMIS Maksimum: {max_length}")
    print(f"Jumlah LMIS: {len(paths)}")    
    for i, path in enumerate(paths, 1):
        subsequence = [arr[idx] for idx in path]
        print(subsequence)
    
    # Visuaisasi tree
    dot, _, _ = visualize_LMIS_tree(arr)
    dot.render('LMIS_tree', format='png', cleanup=True, view=True)
    print("\nVisuaLMISasi tree telah disimpan sebagai 'LMIS_tree.png'")
    