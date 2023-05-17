from graph import graph
from destiny import destiny

def search_route(graph, destiny, start, goal):
    
    # implementando algoritmo de busca gulosa

    ## vetor de cidades visitadas que já inicia com a cidade de partida
    cidadesVisitadas = [start]
    proximaCidade = start
    cidadesVizinhas = []
    distanciaCidadesVizinhas = {}

    def calcDistancia(next_city, start):
        distancia = 0
        
        for city, _ in graph[start].items():
            if city == next_city:
                distancia = destiny[city]

                if city not in cidadesVisitadas:
                    distanciaCidadesVizinhas[city] = distancia
        
        return distancia

    if start == goal:
        return print("Você já está no destino")
    
    while start != goal:
        print("Cidade atual: ", start,"\n")
        print("Cidades vizinhas a ", start, ":")
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

start = "Arad"
goal = "Bucareste"
path = search_route(graph, destiny, start, goal)
print(path)
