import random
import matplotlib.pyplot as plt
import numpy as np

# KONSTANTA & DEFINISI GERAKAN KUDA
N = 8
MOVE_X = [2, 1, -1, -2, -2, -1, 1, 2]
MOVE_Y = [1, 2, 2, 1, -1, -2, -2, -1]

def is_valid(x, y, board):
    return 0 <= x < N and 0 <= y < N and board[x][y] == 0

def get_degree(x, y, board):
    count = 0
    for i in range(8):
        next_x = x + MOVE_X[i]
        next_y = y + MOVE_Y[i]
        if is_valid(next_x, next_y, board):
            count += 1
    return count

def check_closed_tour(end_x, end_y, start_x, start_y):
    for i in range(8):
        if end_x + MOVE_X[i] == start_x and end_y + MOVE_Y[i] == start_y:
            return True
    return False

def solve_warnsdorff(start_x, start_y, is_closed_search=False):
    board = [[0] * N for _ in range(N)]
    current_x, current_y = start_x, start_y
    board[current_x][current_y] = 1
    
    for move_count in range(2, N * N + 1):
        possible_moves = []
        for i in range(8):
            next_x = current_x + MOVE_X[i]
            next_y = current_y + MOVE_Y[i]
            if is_valid(next_x, next_y, board):
                degree = get_degree(next_x, next_y, board)
                possible_moves.append((degree, next_x, next_y))
                
        if not possible_moves:
            return None
        
        possible_moves.sort()
        min_degree = possible_moves[0][0]
        best_moves = [move for move in possible_moves if move[0] == min_degree]
        _, next_x, next_y = random.choice(best_moves)
        current_x, current_y = next_x, next_y
        board[current_x][current_y] = move_count
    
    if is_closed_search:
        return board if check_closed_tour(current_x, current_y, start_x, start_y) else None
    return board

def draw_tour(board, start_x, start_y, tour_name):
    if board is None:
        print("\n Maaf, solusi tidak ditemukan untuk kriteria tersebut dari titik ini.")
        return

    route_x, route_y = [0] * (N*N), [0] * (N*N)
    for i in range(N):
        for j in range(N):
            step = board[i][j]
            route_x[step - 1] = j + 0.5
            route_y[step - 1] = N - i - 0.5
    
    fig, ax = plt.subplots(figsize=(8, 8))
    for i in range(N):
        for j in range(N):
            color = '#D18B47' if (i + j) % 2 == 0 else '#FFCE9E'
            ax.add_patch(plt.Rectangle((j, i), 1, 1, facecolor=color))
            step = board[N - 1 - i][j]
            ax.text(j + 0.5, i + 0.5, str(step), ha='center', va='center', fontsize=9)
    
    ax.plot(route_x, route_y, color='red', linewidth=2, marker='o', markersize=4)
    ax.plot(route_x[0], route_y[0], 'go', markersize=12, label='Mulai (1)')
    ax.plot(route_x[-1], route_y[-1], 'bo', markersize=12, label='Selesai (64)')

    if tour_name == "Closed Tour":
        ax.plot([route_x[-1], route_x[0]], [route_y[-1], route_y[0]], color='red', linestyle='--', linewidth=2)
    
    plt.title(f"Knight's Tour - {tour_name}\nTitik Awal: ({start_x}, {start_y})")
    plt.legend()
    plt.show()

# INPUT
def get_user_input():
    print("=== PROGRAM THE KNIGHT'S TOUR ===")
    try:
        row = int(input("Masukkan Baris awal (0-7): "))
        col = int(input("Masukkan Kolom awal (0-7): "))
        
        if not (0 <= row < 8 and 0 <= col < 8):
            print("Input harus antara 0 sampai 7")
            return None, None, None
            
        print("\nPilih Jenis Tur:")
        print("1. Open Tour (Berakhir di mana saja)")
        print("2. Closed Tour (Kembali ke titik awal)")
        choice = input("Pilihan (1/2): ")
        tour_type = "Open Tour" if choice == "1" else "Closed Tour"
        return row, col, tour_type
    
    except ValueError:
        print("Input harus berupa angka")
        return None, None, None

# EKSEKUSI PROGRAM
start_r, start_c, t_type = get_user_input()

if start_r is not None:
    is_closed = (t_type == "Closed Tour")
    print(f"\nSedang mencari {t_type}...")
    solution = None
    max_attempts = 100 if is_closed else 1
    
    for i in range(max_attempts):
        solution = solve_warnsdorff(start_r, start_c, is_closed_search=is_closed)
        if solution: break
        
    draw_tour(solution, start_r, start_c, t_type)