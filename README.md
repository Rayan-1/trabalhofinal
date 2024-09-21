Aqui está o conteúdo que você pode adicionar ao seu README para documentar o **Simulated Annealing aplicado ao Problema do Caixeiro Viajante (TSP)**:

---

# Algoritmo Simulated Annealing aplicado ao Problema do Caixeiro Viajante (TSP)

## Objetivo

O objetivo deste trabalho é resolver o **Problema do Caixeiro Viajante (TSP)** usando o algoritmo de **Simulated Annealing**. O TSP é um problema clássico de otimização combinatória em que um caixeiro viajante deve visitar um conjunto de cidades e retornar à cidade de origem, minimizando a distância total percorrida.

## Metodologia

Foi utilizado o algoritmo **Simulated Annealing (SA)**, uma metaheurística inspirada no processo de recozimento (annealing) em metalurgia, que busca soluções ótimas para problemas de otimização. O SA tenta evitar mínimos locais, aceitando soluções piores com uma certa probabilidade, que diminui ao longo do tempo (resfriamento).

## Estrutura do Código

### 1. Cálculo da Distância Euclidiana entre duas cidades:

A função `distance(city1, city2)` recebe duas cidades, representadas por suas coordenadas (x, y), e calcula a distância euclidiana entre elas.

```python
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)
```

### 2. Cálculo da Distância Total de uma Rota:

A função `total_distance(route, cities)` recebe uma rota (uma lista de índices representando a ordem das cidades a serem visitadas) e calcula a distância total percorrida pelo caixeiro viajante ao visitar as cidades na ordem definida pela rota.

```python
def total_distance(route, cities):
    dist = 0
    for i in range(len(route)):
        dist += distance(cities[route[i]], cities[route[(i + 1) % len(route)]])
    return dist
```

### 3. Geração de uma Solução Inicial Aleatória:

A função `generate_initial_solution(n)` cria uma solução inicial para o TSP, gerando uma ordem aleatória das cidades.

```python
def generate_initial_solution(n):
    solution = list(range(n))
    random.shuffle(solution)
    return solution
```

### 4. Perturbação da Solução Atual:

A função `perturb_solution(solution)` gera uma nova solução vizinha trocando duas cidades aleatórias de lugar na solução atual. Isso permite explorar o espaço de soluções.

```python
def perturb_solution(solution):
    new_solution = solution[:]
    i, j = random.sample(range(len(solution)), 2)
    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
    return new_solution
```

### 5. Função de Aceitação Probabilística:

A função `acceptance_probability(current_cost, new_cost, temperature)` determina a probabilidade de aceitar a nova solução com base na diferença de custo entre a solução atual e a nova solução, e na temperatura do sistema. Se a nova solução for melhor, ela é aceita diretamente. Caso contrário, é aceita com uma certa probabilidade.

```python
def acceptance_probability(current_cost, new_cost, temperature):
    if new_cost < current_cost:
        return 1.0
    return math.exp((current_cost - new_cost) / temperature)
```

### 6. Algoritmo de Simulated Annealing:

A função `simulated_annealing(cities, initial_temp, cooling_rate, num_iterations)` implementa o algoritmo Simulated Annealing. Ele começa com uma solução inicial aleatória e, a cada iteração, gera uma solução vizinha. Se a nova solução for melhor, ela é aceita. Se for pior, pode ser aceita com uma probabilidade baseada na temperatura. A temperatura diminui ao longo do tempo (cooling).

```python
def simulated_annealing(cities, initial_temp, cooling_rate, num_iterations):
    current_solution = generate_initial_solution(len(cities))
    current_cost = total_distance(current_solution, cities)
    best_solution = current_solution[:]
    best_cost = current_cost
    temperature = initial_temp

    for _ in range(num_iterations):
        new_solution = perturb_solution(current_solution)
        new_cost = total_distance(new_solution, cities)

        if acceptance_probability(current_cost, new_cost, temperature) > random.random():
            current_solution = new_solution
            current_cost = new_cost

            if current_cost < best_cost:
                best_solution = current_solution[:]
                best_cost = current_cost

        temperature *= cooling_rate

    return best_solution, best_cost
```

### 7. Geração de Cidades Aleatórias:

Uma instância de 10 cidades foi criada, cada uma com coordenadas aleatórias entre 0 e 100.

```python
num_cities = 10
cities = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(num_cities)]
```

### 8. Execução do Algoritmo:

Definimos os parâmetros do algoritmo, como a temperatura inicial, a taxa de resfriamento e o número de iterações. O algoritmo é então executado para encontrar a melhor rota.

```python
initial_temp = 1000
cooling_rate = 0.99
num_iterations = 10000

best_route, best_cost = simulated_annealing(cities, initial_temp, cooling_rate, num_iterations)
```

### 9. Exibição dos Resultados:

Ao final, a melhor rota encontrada e a distância mínima obtida são exibidas.

```python
print(f"Melhor rota encontrada: {best_route}")
print(f"Menor distância obtida: {best_cost:.2f}")
```

---

Este conteúdo pode ser adicionado ao arquivo README.md no seu repositório para documentar de maneira completa a implementação do algoritmo.
