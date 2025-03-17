# -*- coding: utf-8 -*-
"""GBFS

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zSnSIi6rS4qcMx8xdpqw7aBMOEiysT0H

**Kode sebelum di ubah nilai nilai nya**
"""

from queue import PriorityQueue

# Fungsi untuk algoritma Greedy Best-First Search
def greedy_best_first_search(graph, start, goal):
    frontier = PriorityQueue()  # Antrian prioritas berdasarkan heuristik
    frontier.put((heuristic[start], start))  # Menambahkan simpul awal dengan nilai heuristik
    explored = set()  # Set untuk menyimpan simpul yang sudah dieksplorasi
    visited_order = []  # List untuk mencatat urutan kunjungan simpul

    while not frontier.empty():
        _, current_node = frontier.get()  # Ambil simpul dengan heuristik terendah
        visited_order.append(current_node)
        print("Mengunjungi simpul:", current_node)

        if current_node == goal:
            print("\nSimpul tujuan ditemukan!")
            print("Urutan kunjungan simpul:", " → ".join(visited_order))
            return True  # Berhenti jika simpul tujuan ditemukan

        explored.add(current_node)  # Tandai sebagai sudah dieksplorasi

        for neighbor in graph[current_node]:
            if neighbor not in explored:
                priority = heuristic[neighbor]  # Nilai heuristik sebagai prioritas
                frontier.put((priority, neighbor))  # Tambahkan ke antrian

    print("\nSimpul tujuan tidak ditemukan!")
    print("Urutan kunjungan simpul:", " → ".join(visited_order))
    return False  # Jika simpul tujuan tidak ditemukan

# Daftar heuristik untuk setiap simpul
heuristic = {
    'A': 9,
    'B': 4,
    'C': 2,
    'D': 5,
    'E': 3,
    'S': 7,
    'G': 0  # Simpul tujuan memiliki nilai heuristik 0
}

# Graf berbentuk adjacency list
graph = {
    'S': {'A', 'E'},
    'A': {'B', 'C'},
    'B': {'D'},
    'C': {'G'},
    'D': {'G'},
    'E': {'D'}
}

# Titik awal dan tujuan
start_node = 'S'
goal_node = 'G'

# Panggil fungsi Greedy Best-First Search
greedy_best_first_search(graph, start_node, goal_node)

"""**kode pas udah di ubah nilai nya**

"""

from queue import PriorityQueue

# Fungsi untuk Algoritma Greedy Best-First Search
def greedy_best_first_search(graph, start, goal):
    frontier = PriorityQueue()  # Antrian prioritas berdasarkan heuristik
    frontier.put((heuristic[start], start))

    came_from = {}  # Menyimpan jalur yang ditempuh
    explored = set()  # Set untuk menyimpan simpul yang sudah dikunjungi
    visited_order = []  # Urutan simpul yang dikunjungi

    while not frontier.empty():
        h_value, current_node = frontier.get()
        visited_order.append((current_node, h_value))  # Simpan simpul dan heuristiknya

        print(f"Mengunjungi simpul: {current_node} (h = {h_value})")

        if current_node == goal:
            print("\nSimpul tujuan ditemukan!")
            print("Urutan kunjungan simpul:")
            for node, h in visited_order:
                print(f"  - {node} (h = {h})")

            path, total_cost = reconstruct_path(came_from, start, goal, graph)
            print("\nJalur terbaik:", " → ".join(path))
            print(f"Total bobot jalur: {total_cost}")
            return path, total_cost  # Kembalikan jalur terbaik

        explored.add(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in explored and neighbor not in came_from:
                frontier.put((heuristic[neighbor], neighbor))
                came_from[neighbor] = current_node  # Simpan jalur

    print("\nSimpul tujuan tidak ditemukan!")
    print("Urutan kunjungan simpul:", " → ".join(node for node, _ in visited_order))
    return None, None

# Fungsi untuk membangun kembali jalur dari goal ke start
def reconstruct_path(came_from, start, goal, graph):
    path = [goal]
    total_cost = 0

    while path[-1] != start:
        prev = came_from[path[-1]]
        total_cost += graph[prev][path[-1]]  # Tambahkan bobot jalur
        path.append(prev)

    path.reverse()
    return path, total_cost

# Daftar heuristik untuk setiap simpul
heuristic = {
    'S': 6,
    'A': 4,
    'B': 3,
    'C': 3,
    'D': 1,
    'G': 0  # Simpul tujuan memiliki nilai heuristik 0
}

# Graf berbentuk adjacency list dengan bobot
graph = {
    'S': {'A': 3, 'B': 2},
    'A': {'D': 5, 'B': 1},
    'B': {'C': 2},
    'C': {'D': 3, 'G': 4},
    'D': {'G': 1}
}

# Titik awal dan tujuan
start_node = 'S'
goal_node = 'G'

# Panggil fungsi Greedy Best-First Search
greedy_best_first_search(graph, start_node, goal_node)