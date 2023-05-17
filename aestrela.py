from graph import graph
from destiny import destiny

def search_route(graph, destiny, start, goal):
    
    ## vetor de cidades visitadas que já inicia com a cidade de partida
    cidadesVisitadas = [start]
    proximaCidade = start
    cidadesVizinhas = []
    distanciaCidadesVizinhas = {}

    def distanciaTotal(next_city, start):
        distancia = 0
        
        for city, distance in graph[start].items():
            if city == next_city:
                distancia = distance + destiny[next_city]
                
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
        for next_city, distance in graph[start].items():
            cidadesVizinhas.append(next_city)

            print(next_city)
            print("Dist. Heuristica: ", destiny[next_city])
            print("Dist. Estrada: ", distance)
            if next_city not in cidadesVisitadas:
                print("Dist. A*: ", distanciaTotal(next_city, start), "\n")
        
        for city in cidadesVizinhas:
            if city not in cidadesVisitadas:
                #proxima cidade recebe a cidade com menor distancia
                proximaCidade = min(distanciaCidadesVizinhas, key=distanciaCidadesVizinhas.get)
                         
        distanciaCidadesVizinhas = {}
        cidadesVisitadas.append(proximaCidade)
        start = proximaCidade 
    
    return cidadesVisitadas

start = "Lugoj"
goal = "Bucareste"
path = search_route(graph, destiny, start, goal)
print('\n\nVoce chegou ao seu destino!')
print(path)
