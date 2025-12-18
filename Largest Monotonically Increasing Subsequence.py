def find_LMIS(sequence):
    n = len(sequence)
    if n == 0:
        return 0, []
    dp = [1] * n
    predecessors = [[] for _ in range(n)]
    max_length = 0

    # Hitung DP dan Predecessors
    for i in range(n):
        for j in range(i):
            if sequence[i] > sequence[j]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    predecessors[i] = [j]
                elif dp[j] + 1 == dp[i]:
                    predecessors[i].append(j)
        max_length = max(max_length, dp[i])

    # Temukan titik akhir
    end_indices = [i for i in range(n) if dp[i] == max_length]

    # Rekonstruksi dengan DFS
    all_lmis = []
    def reconstruct_paths(current_index, current_path):
        current_path.append(sequence[current_index])
        if not predecessors[current_index]:
            all_lmis.append(current_path[::-1])
        else:
            for prev_index in predecessors[current_index]:
                reconstruct_paths(prev_index, list(current_path))
        current_path.pop()

    for end_idx in end_indices:
        reconstruct_paths(end_idx, [])

    return max_length, sorted(all_lmis)

# INPUT
print("=== Program L.M.I.S ===")
print("Masukkan urutan angka dipisahkan dengan spasi atau koma.")
print("Contoh: 4, 1, 13, 7, 0, 2, 8, 11, 3")

raw_input = input("\nInput angka: ")

# Mengganti koma menjadi spasi, lalu memecah string menjadi list
clean_input = raw_input.replace(',', ' ').split()
urutan_user = [int(x) for x in clean_input]

# Eksekusi fungsi
panjang, hasil = find_LMIS(urutan_user)

# OUTPUT
print(f"\n--- HASIL ANALISIS ---")
print(f"Urutan: {urutan_user}")
print(f"Panjang L.M.I.S. Terpanjang: {panjang}")
print(f"Jumlah variasi yang ditemukan: {len(hasil)}")
for i, lmis in enumerate(hasil, 1):
    print(f"{i}. {lmis}")