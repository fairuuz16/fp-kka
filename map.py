from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        # Class constructor and its attributes
        self.graph = defaultdict(list)
        self.static_heuristic = {}
        self.edge_costs = {}
        
    def add_edge(self, from_node, to_node, cost):
        # Add edges with a certain cost to the graph
        self.graph.setdefault(from_node, []).append(to_node)
        self.edge_costs[(from_node, to_node)] = cost

    def add_static_heuristic(self, node, heuristic_value):
        # Add static heuristics for a node
        self.static_heuristic[node] = heuristic_value

    def a_star_search(self, start, finish):
        # Implementation of A* search algorithm
        visited = set()
        priority_queue = [(0, start)]
        g_values = {node: float('inf') for node in self.graph.keys()}
        g_values[start] = 0
        path = {}

        while priority_queue:
            _, current_node = heapq.heappop(priority_queue)

            if current_node in visited:
                continue

            visited.add(current_node)

            if current_node == finish:
                result_path = [current_node]
                while current_node != start:
                    current_node = path[current_node]
                    result_path.append(current_node)
                result_path.reverse()
                return result_path

            for neighbor in self.graph.get(current_node, []):
                if neighbor not in visited:
                    tentative_g_value = g_values[current_node] + self.edge_costs.get((current_node, neighbor), float('inf'))
                    if tentative_g_value < g_values.get(neighbor, float('inf')):
                        g_values[neighbor] = tentative_g_value
                        h_value = self.static_heuristic.get(neighbor, 0)
                        f_value = tentative_g_value + h_value
                        heapq.heappush(priority_queue, (f_value, neighbor))
                        path[neighbor] = current_node

        return None

g = Graph()

# JALUR UTARA
g.add_edge('SURABAYA PASAR TURI', 'LAMONGAN', 38)
g.add_edge('LAMONGAN', 'BOJONEGORO', 62)
g.add_edge('BOJONEGORO', 'CEPU', 36)
g.add_edge('CEPU', 'NGROMBO', 80)
g.add_edge('NGROMBO', 'SEMARANG TAWANG', 49)
g.add_edge('SEMARANG TAWANG', 'PEKALONGAN',	89)
g.add_edge('PEKALONGAN', 'TEGAL', 60)
g.add_edge('TEGAL',	'CIREBON', 71)
g.add_edge('CIREBON', 'JATIBARANG', 40)
g.add_edge('JATIBARANG', 'CIKAMPEK', 98)
g.add_edge('CIKAMPEK', 'KARAWANG', 22)

g.add_edge('LAMONGAN', 'SURABAYA PASAR TURI', 38)
g.add_edge('BOJONEGORO', 'LAMONGAN', 62)
g.add_edge('CEPU', 'BOJONEGORO', 36)
g.add_edge('NGROMBO', 'CEPU', 80)
g.add_edge('SEMARANG TAWANG', 'NGROMBO', 49)
g.add_edge('PEKALONGAN', 'SEMARANG TAWANG', 89)
g.add_edge('TEGAL', 'PEKALONGAN', 60)
g.add_edge('CIREBON', 'TEGAL',	71)
g.add_edge('JATIBARANG', 'CIREBON', 40)
g.add_edge('CIKAMPEK', 'JATIBARANG', 98)
g.add_edge('KARAWANG', 'CIKAMPEK', 22)

# JALUR TENGAH
g.add_edge('SURABAYA GUBENG', 'SEPANJANG', 45)
g.add_edge('SEPANJANG',	'MOJOKERTO', 45)
g.add_edge('MOJOKERTO',	'JOMBANG', 23)
g.add_edge('JOMBANG', 'KERTOSONO', 38)
g.add_edge('KERTOSONO',	'MADIUN', 68)
g.add_edge('MADIUN', 'WALIKUKUN', 43)
g.add_edge('WALIKUKUN',	'SRAGEN', 23)
g.add_edge('SRAGEN', 'SOLO BALAPAN', 30)
g.add_edge('SOLO BALAPAN', 'GUNDIH', 41)
g.add_edge('GUNDIH', 'SEMARANG TAWANG',	66)
g.add_edge('SEMARANG TAWANG', 'PEKALONGAN',	89)
g.add_edge('PEKALONGAN', 'TEGAL', 60)
g.add_edge('TEGAL',	'CIREBON', 71)
g.add_edge('CIREBON', 'JATIBARANG', 40)
g.add_edge('JATIBARANG', 'CIKAMPEK', 98)
g.add_edge('CIKAMPEK', 'KARAWANG', 22)

g.add_edge('SEPANJANG', 'SURABAYA GUBENG', 45)
g.add_edge('MOJOKERTO', 'SEPANJANG', 45)
g.add_edge('MOJOKERTO',	'JOMBANG', 23)
g.add_edge('KERTOSONO', 'JOMBANG', 38)
g.add_edge('MADIUN', 'KERTOSONO', 68)
g.add_edge('WALIKUKUN', 'MADIUN', 43)
g.add_edge('SRAGEN', 'WALIKUKUN', 23)
g.add_edge('SOLO BALAPAN', 'SRAGEN', 30)
g.add_edge('GUNDIH', 'SOLO BALAPAN', 41)
g.add_edge('SEMARANG TAWANG', 'GUNDIH', 66)
g.add_edge('PEKALONGAN', 'SEMARANG TAWANG', 89)
g.add_edge('TEGAL', 'PEKALONGAN', 60)
g.add_edge('CIREBON', 'TEGAL',	71)
g.add_edge('JATIBARANG', 'CIREBON', 40)
g.add_edge('CIKAMPEK', 'JATIBARANG', 98)
g.add_edge('KARAWANG', 'CIKAMPEK', 22)

# JALUR SELATAN
g.add_edge('SURABAYA GUBENG', 'SEPANJANG', 45)
g.add_edge('SEPANJANG',	'MOJOKERTO', 23)
g.add_edge('MOJOKERTO',	'JOMBANG', 38)
g.add_edge('JOMBANG', 'KERTOSONO', 68)
g.add_edge('KERTOSONO',	'MADIUN', 43)
g.add_edge('MADIUN', 'WALIKUKUN', 23)
g.add_edge('WALIKUKUN',	'SRAGEN', 23)
g.add_edge('SRAGEN', 'SOLO BALAPAN', 30)
g.add_edge('SOLO BALAPAN', 'TUGU', 56)
g.add_edge('TUGU', 'KEDUNDANG', 29)
g.add_edge('KEDUNDANG', 'KUTOARJO', 36)
g.add_edge('KUTOARJO', 'KEBUMEN', 28)
g.add_edge('KEBUMEN', 'KROYA', 47)
g.add_edge('KROYA', 'TASIKMALAYA', 130)
g.add_edge('TASIKMALAYA', 'CIPEUNDEUY', 33)
g.add_edge('CIPEUNDEUY', 'NAGREG', 43)
g.add_edge('NAGREG', 'PADALARANG', 45)

g.add_edge('SEPANJANG', 'SURABAYA GUBENG', 45)
g.add_edge('MOJOKERTO', 'SEPANJANG', 23)
g.add_edge('JOMBANG', 'MOJOKERTO', 38)
g.add_edge('KERTOSONO', 'JOMBANG', 68)
g.add_edge('MADIUN', 'KERTOSONO', 43)
g.add_edge('WALIKUKUN', 'MADIUN', 23)
g.add_edge('SRAGEN', 'WALIKUKUN', 23)
g.add_edge('SOLO BALAPAN', 'SRAGEN', 30)
g.add_edge('TUGU', 'SOLO BALAPAN', 56)
g.add_edge('KEDUNDANG', 'TUGU', 29)
g.add_edge('KUTOARJO', 'KEDUNDANG', 36)
g.add_edge('KEBUMEN', 'KUTOARJO', 28)
g.add_edge('KROYA', 'KEBUMEN', 47)
g.add_edge('TASIKMALAYA', 'KROYA', 130)
g.add_edge('CIPEUNDEUY', 'TASIKMALAYA', 33)
g.add_edge('NAGREG', 'CIPEUNDEUY', 43)
g.add_edge('PADALARANG', 'NAGREG', 45)


# JALUR TAMBAHAN
g.add_edge('HALIM',	'PASAR SENEN',	9)
g.add_edge('PADALARANG', 'TEGALUAR', 28)
g.add_edge('SURABAYA PASAR TURI', 'SURABAYA GUBENG', 5)

g.add_edge('PASAR SENEN', 'HALIM', 9)
g.add_edge('TEGALUAR', 'PADALARANG', 28)
g.add_edge('SURABAYA GUBENG', 'SURABAYA PASAR TURI', 5)


# HEURISTIK STASIUN 
g.add_static_heuristic('SURABAYA PASAR TURI', 35)
g.add_static_heuristic('LAMONGAN', 60)
g.add_static_heuristic('BOJONEGORO', 50)
g.add_static_heuristic('CEPU', 60)
g.add_static_heuristic('NGROMBO', 70)
g.add_static_heuristic('SEMARANG TAWANG', 35)
g.add_static_heuristic('PEKALONGAN', 55)
g.add_static_heuristic('TEGAL', 45)
g.add_static_heuristic('CIREBON', 45)
g.add_static_heuristic('JATIBARANG', 60)
g.add_static_heuristic('CIKAMPEK', 65)
g.add_static_heuristic('KARAWANG', 45)
                       
g.add_static_heuristic('SURABAYA GUBENG', 35)
g.add_static_heuristic('SEPANJANG', 70)
g.add_static_heuristic('MOJOKERTO', 70)
g.add_static_heuristic('JOMBANG', 70)
g.add_static_heuristic('KERTOSONO', 50)
g.add_static_heuristic('MADIUN', 40)
g.add_static_heuristic('WALIKUKUN', 70)
g.add_static_heuristic('SRAGEN', 70)
g.add_static_heuristic('SOLO BALAPAN', 35)
g.add_static_heuristic('GUNDIH', 55)
g.add_static_heuristic('SEMARANG TAWANG', 35)
g.add_static_heuristic('PEKALONGAN', 55)
g.add_static_heuristic('TEGAL', 45)
g.add_static_heuristic('CIREBON', 45)
g.add_static_heuristic('JATIBARANG', 60)
g.add_static_heuristic('CIKAMPEK', 65)
g.add_static_heuristic('KARAWANG', 45)
                       
g.add_static_heuristic('SURABAYA GUBENG', 35)
g.add_static_heuristic('SEPANJANG', 70)
g.add_static_heuristic('MOJOKERTO', 70)
g.add_static_heuristic('JOMBANG', 70)
g.add_static_heuristic('KERTOSONO', 50)
g.add_static_heuristic('MADIUN', 40)
g.add_static_heuristic('WALIKUKUN', 70)
g.add_static_heuristic('SRAGEN', 70)
g.add_static_heuristic('SOLO BALAPAN', 35)
g.add_static_heuristic('TUGU', 35)
g.add_static_heuristic('KEDUNDANG', 80)
g.add_static_heuristic('KUTOARJO', 45)
g.add_static_heuristic('KEBUMEN', 60)
g.add_static_heuristic('KROYA', 55)
g.add_static_heuristic('TASIKMALAYA', 60)
g.add_static_heuristic('CIPEUNDEUY', 70)
g.add_static_heuristic('NAGREG', 80)
g.add_static_heuristic('PADALARANG', 50)

g.add_static_heuristic('HALIM', 35)
g.add_static_heuristic('PASAR SENEN', 35)
g.add_static_heuristic('PADALARANG', 50)
g.add_static_heuristic('TEGALUAR', 45)

station = {
    # STASIUN JALUR UTARA
    "SURABAYA PASAR TURI": {
        "name" : "SURABAYA PASAR TURI",
        "lat": -7.24817,
        "lon": 112.7312
    },
    "LAMONGAN": {
        "name" : "LAMONGAN",
        "lat": -7.11249,
        "lon": 112.4202
    },
    "BOJONEGORO": {
        "name" : "BOJONEGORO",
        "lat": -7.16437,
        "lon": 111.8868
    },
    "CEPU": {
        "name" : "CEPU",
        "lat": -7.15417,
        "lon": 111.5912
    },
    "NGROMBO": {
        "name" : "NGROMBO",
        "lat": -7.14526,
        "lon": 110.9004
    },
    "SEMARANG TAWANG": {
        "name" : "SEMARANG TAWANG",
        "lat": -6.96448,
        "lon": 110.4282
    },
    "PEKALONGAN": {
        "name" : "PEKALONGAN",
        "lat": -6.88977,
        "lon": 109.6642
    },
    "TEGAL": {
        "name" : "TEGAL",
        "lat": -6.86737,
        "lon": 109.1428
    },
    "CIREBON": {
        "name" : "CIREBON",
        "lat": -6.70551,
        "lon": 108.5554
    },
    "JATIBARANG": {
        "name" : "JATIBARANG",
        "lat": -6.4729,
        "lon": 108.306
    },
    "CIKAMPEK": {
        "name" : "CIKAMPEK",
        "lat": -6.40607,
        "lon": 107.459
    },
    "KARAWANG": {
        "name" : "KARAWANG",
        "lat": -6.30518,
        "lon": 107.3002
    },

    # STASIUN JALUR TENGAH
    "SURABAYA GUBENG": {
        "name" : "SURABAYA GUBENG",
        "lat": -7.2652,
        "lon": 112.7522
    },
    "SEPANJANG": {
        "name" : "SEPANJANG",
        "lat": -7.34717,
        "lon": 112.6978
    },
    "MOJOKERTO": {
        "name" : "MOJOKERTO",
        "lat": -7.47241,
        "lon": 112.4344
    },
    "JOMBANG": {
        "name" : "JOMBANG",
        "lat": -7.5578,
        "lon": 112.2334
    },
    "KERTOSONO": {
        "name" : "KERTOSONO",
        "lat": -7.5918,
        "lon": 112.1008
    },
    "MADIUN": {
        "name" : "MADIUN",
        "lat": -7.61841,
        "lon": 111.525
    },
    "WALIKUKUN": {
        "name" : "WALIKUKUN",
        "lat": -7.39868,
        "lon": 111.2246
    },
    "SRAGEN": {
        "name" : "SRAGEN",
        "lat": -7.42938,
        "lon": 111.018
    },
    "SOLO BALAPAN": {
        "name" : "SOLO BALAPAN",
        "lat": -7.55719,
        "lon": 110.8214
    },
    "GUNDIH": {
        "name" : "GUNDIH",
        "lat": -7.21869,
        "lon": 110.9
    },
    "SEMARANG TAWANG": {
        "name" : "SEMARANG TAWANG",
        "lat": -6.96448,
        "lon": 110.4282
    },
    "PEKALONGAN": {
        "name" : "PEKALONGAN",
        "lat": -6.88977,
        "lon": 109.6642
    },
    "TEGAL": {
        "name" : "TEGAL",
        "lat": -6.86737,
        "lon": 109.1428
    },
    "CIREBON": {
        "name" : "CIREBON",
        "lat": -6.70551,
        "lon": 108.5554
    },
    "JATIBARANG": {
        "name" : "JATIBARANG",
        "lat": -6.4729,
        "lon": 108.306
    },
    "CIKAMPEK": {
        "name" : "CIKAMPEK",
        "lat": -6.40607,
        "lon": 107.459
    },
    "KARAWANG": {
        "name" : "KARAWANG",
        "lat": -6.30518,
        "lon": 107.3002
    },

    # STASIUN JALUR SELATAN
    "SURABAYA GUBENG": {
        "name" : "SURABAYA GUBENG",
        "lat": -7.2652,
        "lon": 112.7522
    },
    "SEPANJANG": {
        "name" : "SEPANJANG",
        "lat": -7.34717,
        "lon": 112.6978
    },
    "MOJOKERTO": {
        "name" : "MOJOKERTO",
        "lat": -7.47241,
        "lon": 112.4344
    },
    "JOMBANG": {
        "name" : "JOMBANG",
        "lat": -7.5578,
        "lon": 112.2334
    },
    "KERTOSONO": {
        "name" : "KERTOSONO",
        "lat": -7.5918,
        "lon": 112.1008
    },
    "MADIUN": {
        "name" : "MADIUN",
        "lat": -7.61841,
        "lon": 111.525
    },
    "WALIKUKUN": {
        "name" : "WALIKUKUN",
        "lat": -7.39868,
        "lon": 111.2246
    },
    "SRAGEN": {
        "name" : "SRAGEN",
        "lat": -7.42938,
        "lon": 111.018
    },
    "SOLO BALAPAN": {
        "name" : "SOLO BALAPAN",
        "lat": -7.55719,
        "lon": 110.8214
    },
    "TUGU": {
        "name" : "TUGU",
        "lat": -7.78918,
        "lon": 110.3636
    },
    "KEDUNDANG": {
        "name" : "KEDUNDANG",
        "lat": -7.85919,
        "lon": 110.2094
    },
    "KUTOARJO": {
        "name" : "KUTOARJO",
        "lat": -7.7262,
        "lon": 109.9074
    },
    "KEBUMEN": {
        "name" : "KEBUMEN",
        "lat": -7.68188,
        "lon": 109.6622
    },
    "KROYA": {
        "name" : "KROYA",
        "lat": -7.63339,
        "lon": 109.2538
    },
    "TASIKMALAYA": {
        "name" : "TASIKMALAYA",
        "lat": -7.32257,
        "lon": 108.2242
    },
    "CIPEUNDEUY": {
        "name" : "CIPEUNDEUY",
        "lat": -7.09357,
        "lon": 108.1006
    },
    "NAGREG": {
        "name" : "NAGREG",
        "lat": -7.01819,
        "lon": 107.8862
    },
    "PADALARANG": {
        "name" : "PADALARANG",
        "lat": -6.84227,
        "lon": 107.4976
    }
}

###############################################################################################
app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/process_data', methods=['POST'])
def process_data():
    data = request.json.get('data')
    if len(data) == 2:
        rute = []
        goal = []
        stasiun = []

        start_node, finish_node = data

        start_node = start_node.upper()
        finish_node = finish_node.upper()

        path = g.a_star_search(start_node, finish_node)

        if (path is not None):
            print(path)
            
            for place in path:
                rute.append([station[place]["lat"], station[place]["lon"]])

            for stop in path:
                stasiun.append([" " + station[stop]["name"]]) 

            goal = [station[path[-1]]["lat"], station[path[-1]]["lon"]]
            name = [station[path[-1]]["name"]]
            
        print("Ini rute.", rute)
            
        resp = {
            "path": rute,
            "goal": goal,
            "stasiun": stasiun
        }
        return jsonify(resp)
    else:
        return "Data yang diterima tidak sesuai."

if __name__ == '__main__':
    app.run(debug=True)