import random
import math

# Função para calcular a distância entre duas cidades usando a fórmula da distância euclidiana
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Função que calcula a distância total de uma rota (solução)
def total_distance(route, cities):
    dist = 0
    for i in range(len(route)):
        # Soma as distâncias entre cidades consecutivas
        dist += distance(cities[route[i]], cities[route[(i + 1) % len(route)]])
    return dist

# Gera uma solução inicial aleatória
def generate_initial_solution(n):
    solution = list(range(n))  # Lista com as cidades (0, 1, 2, ..., n-1)
    random.shuffle(solution)   # Embaralha as cidades para criar uma rota inicial
    return solution

# Perturba a solução (gera uma solução vizinha) trocando duas cidades aleatoriamente
def perturb_solution(solution):
    new_solution = solution[:]  # Copia a solução atual
    i, j = random.sample(range(len(solution)), 2)  # Escolhe duas cidades aleatórias
    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]  # Troca as cidades de posição
    return new_solution

# Função de aceitação probabilística baseada na temperatura
def acceptance_probability(current_cost, new_cost, temperature):
    if new_cost < current_cost:
        return 1.0  # Se a nova solução for melhor, aceitamos diretamente
    return math.exp((current_cost - new_cost) / temperature)  # Se for pior, aceitamos com uma certa probabilidade

# Algoritmo de Simulated Annealing para o problema do Caixeiro Viajante
def simulated_annealing(cities, initial_temp, cooling_rate, num_iterations):
    current_solution = generate_initial_solution(len(cities))  # Gera uma solução inicial
    current_cost = total_distance(current_solution, cities)  # Calcula o custo da solução inicial
    best_solution = current_solution[:]  # Inicialmente, a melhor solução é a atual
    best_cost = current_cost
    temperature = initial_temp  # Define a temperatura inicial

    for _ in range(num_iterations):  # Loop de iterações
        new_solution = perturb_solution(current_solution)  # Gera uma solução vizinha
        new_cost = total_distance(new_solution, cities)  # Calcula o custo da nova solução

        # Se a nova solução for melhor ou for aceita pela função de aceitação, a adotamos
        if acceptance_probability(current_cost, new_cost, temperature) > random.random():
            current_solution = new_solution  # Atualiza a solução atual
            current_cost = new_cost  # Atualiza o custo atual

            # Se a nova solução é a melhor que já encontramos, atualizamos a melhor solução
            if current_cost < best_cost:
                best_solution = current_solution[:]
                best_cost = current_cost

        temperature *= cooling_rate  # Diminui a temperatura conforme a taxa de resfriamento

    return best_solution, best_cost  # Retorna a melhor solução e seu custo

# Criar uma instância com 10 cidades com coordenadas aleatórias
num_cities = 10
cities = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(num_cities)]

# Definir os parâmetros do Simulated Annealing
initial_temp = 1000  # Temperatura inicial
cooling_rate = 0.99  # Taxa de resfriamento (cooling)
num_iterations = 10000  # Número de iterações

# Executar o algoritmo Simulated Annealing
best_route, best_cost = simulated_annealing(cities, initial_temp, cooling_rate, num_iterations)

# Exibir os resultados
print(f"Melhor rota encontrada: {best_route}")
print(f"Menor distância obtida: {best_cost:.2f}")
