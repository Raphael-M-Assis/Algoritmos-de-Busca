from graph import graph

def search_route(graph, start, goal):
    
    cidadesVisitadas = [start]
    proximaCidade = start
    cidadesVizinhas = []
    distanciaCidadesVizinhas = {}

    def calcDistancia(next_city, start):
        distancia = 0
        
        for city, distance in graph[start].items():
            if city == next_city:
                distancia = distance

                if city not in cidadesVisitadas:
                    distanciaCidadesVizinhas[city] = distancia
        
        return distancia

    if start == goal:
        return print("Você já está no destino")
    
    while start != goal:
        print("-------------------")
        print("-------------------")
        print("Atual: ", start)
        print("-> ADJACENTES")
        for next_city, _ in graph[start].items():
            cidadesVizinhas.append(next_city)
            if next_city not in cidadesVisitadas:
                print(next_city, " - ", calcDistancia(next_city, start))
            
        for city in cidadesVizinhas:
            if city not in cidadesVisitadas:
                #proxima cidade recebe a cidade com menor distancia
                proximaCidade = min(distanciaCidadesVizinhas, key=distanciaCidadesVizinhas.get)
              
        cidadesVisitadas.append(proximaCidade)
        distanciaCidadesVizinhas = {}
        start = proximaCidade            
    
    return cidadesVisitadas

start = "Lugoj"
goal = "Bucareste"
path = search_route(graph, start, goal)
print(path)
