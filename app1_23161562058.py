from collections import deque

def bfs_shortest_path(city_map, start, goal):
    queue = deque([(start, [start])])  # Inisialisasi antrean dengan titik awal
    visited = set()  # Menyimpan node yang sudah dikunjungi
    
    while queue:
        current, path = queue.popleft()
        
        if current == goal:
            return path  # Jika menemukan tujuan, kembalikan jalur
        
        if current not in visited:
            visited.add(current)
            for neighbor in city_map.get(current, []):  # Periksa tetangga dari node saat ini
                queue.append((neighbor, path + [neighbor]))
    
    return None  # Jika tidak ada jalur yang ditemukan

# Contoh peta kota
city_map = {
    'Home': ['Mall', 'School'],
    'Mall': ['Gym', 'Hospital'],
    'School': ['Library'],
    'Gym': ['Hospital'],
    'Library': ['Hospital'],
    'Hospital': []
}

# Mencari jalur dari 'Home' ke 'Hospital'
print(bfs_shortest_path(city_map, 'Home', 'Hospital'))
