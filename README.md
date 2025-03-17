Berikut deskripsi yang sesuai untuk repositori berisi implementasi **Greedy Best-First Search (GBFS)**, **A* Tree Search**, dan **A* Graph Search** dalam Python.

# Implementasi Algoritma Pencarian A* dan GBFS dalam Python  

Repositori ini berisi implementasi algoritma pencarian berbasis heuristik yang digunakan untuk menemukan jalur optimal dalam suatu ruang pencarian. Algoritma yang diimplementasikan meliputi metode **Greedy Best-First Search (GBFS)**, **A* Tree Search**, dan **A* Graph Search**.  

## 🔹 Informed Search (Pencarian Berbasis Informasi)  
✅ **Greedy Best-First Search (GBFS)** – Memilih simpul dengan **nilai heuristik terendah (h(n))** tanpa mempertimbangkan biaya perjalanan sebelumnya. GBFS dapat bekerja cepat tetapi tidak selalu menemukan jalur optimal.  

✅ **A* Tree Search** – Menggunakan fungsi evaluasi **f(n) = g(n) + h(n)** untuk menentukan jalur terbaik. Namun, karena tidak menyimpan simpul yang telah dikunjungi, algoritma ini bisa mengunjungi ulang simpul yang sama.  

✅ **A* Graph Search** – Mirip dengan A* Tree Search, tetapi dengan **penyimpanan eksplorasi** untuk menghindari pengulangan kunjungan ke simpul yang telah diproses, sehingga lebih efisien.  

Repositori ini cocok bagi siapa saja yang ingin memahami konsep pencarian optimal dalam graf dan bagaimana cara mengimplementasikannya dalam Python. Semoga bermanfaat dan selamat belajar! 🚀
