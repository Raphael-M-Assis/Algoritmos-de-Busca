# Definir as cidades e suas conexões
graph = {
    'Arad': {'Sibiu': 140, 'Timisoara': 118, 'Zerind': 75},
    'Bucareste': {'Fagaras': 211, 'Giurgiu': 90, 'Pitesti': 101, 'Urziceni': 85},
    'Craiova': {'Dobreta': 120, 'Pitesti': 138, 'Rimnicu': 146},
    'Dobreta': {'Craiova': 120, 'Mehadia': 75},
    'Eforie': {'Hirsova': 86},
    'Fagaras': {'Bucareste': 211, 'Sibiu': 99},
    'Giurgiu': {'Bucareste': 90},
    'Hirsova': {'Eforie': 86, 'Urziceni': 98},
    'Iasi': {'Neamt': 87, 'Vaslui': 92},
    'Lugoj': {'Mehadia': 70, 'Timisoara': 111},
    'Mehadia': {'Dobreta': 75, 'Lugoj': 70},
    'Neamt': {'Iasi': 87},
    'Oradea': {'Sibiu': 151, 'Zerind': 71},
    'Pitesti': {'Bucareste': 101, 'Craiova': 138, 'Rimnicu': 97},
    'Rimnicu': {'Craiova': 146, 'Pitesti': 97, 'Sibiu': 80},
    'Sibiu': {'Arad': 140, 'Fagaras': 99, 'Oradea': 151, 'Rimnicu': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Urziceni': {'Bucareste': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Vaslui': {'Iasi': 92, 'Urziceni': 142},
    'Zerind': {'Arad': 75, 'Oradea': 71}
}
