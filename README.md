
# Algoritmo Simulated Annealing aplicado ao Problema do Caixeiro Viajante (TSP)

## Objetivo

O objetivo deste trabalho é resolver o **Problema do Caixeiro Viajante (TSP)** usando o algoritmo de **Simulated Annealing**. O TSP é um problema clássico de otimização combinatória em que um caixeiro viajante deve visitar um conjunto de cidades e retornar à cidade de origem, minimizando a distância total percorrida.

## Metodologia

Foi utilizado o algoritmo **Simulated Annealing (SA)**, uma metaheurística inspirada no processo de recozimento (annealing) em metalurgia, que busca soluções ótimas para problemas de otimização. O SA tenta evitar mínimos locais, aceitando soluções piores com uma certa probabilidade, que diminui ao longo do tempo (resfriamento).

## Estrutura do Código

### 1. Cálculo da Distância Euclidiana entre duas cidades:

A função `distance(city1, city2)` recebe duas cidades, representadas por suas coordenadas (x, y), e calcula a distância euclidiana entre elas.

```python
def calcular_distancia(cidade1, cidade2):
    return math.sqrt((cidade1[0] - cidade2[0])**2 + (cidade1[1] - cidade2[1])**2)
```

### 2. Cálculo da Distância Total de uma Rota:

A função `def calcular_distancia_total(rota, cidades)` recebe uma rota (uma lista de índices representando a ordem das cidades a serem visitadas) e calcula a distância total percorrida pelo caixeiro viajante ao visitar as cidades na ordem definida pela rota.

```python
def calcular_distancia_total(rota, cidades):
    distancia_total = 0
    for i in range(len(rota)):
        # Soma as distâncias entre cidades consecutivas
        distancia_total += calcular_distancia(cidades[rota[i]], cidades[rota[(i + 1) % len(rota)]])
    return distancia_total
```

### 3. Geração de uma Solução Inicial Aleatória:

A função `def gerar_solucao_inicial(n)` cria uma solução inicial para o TSP, gerando uma ordem aleatória das cidades.

```python
def gerar_solucao_inicial(n):
    solucao = list(range(n))  
    random.shuffle(solucao)   
    return solucao
```

### 4. Perturbação da Solução Atual:

A função `perturbar_solucao(solucao)` gera uma nova solução vizinha trocando duas cidades aleatórias de lugar na solução atual. Isso permite explorar o espaço de soluções.

```python
def perturbar_solucao(solucao):
    nova_solucao = solucao[:] 
    i, j = random.sample(range(len(solucao)), 2)  
    nova_solucao[i], nova_solucao[j] = nova_solucao[j], nova_solucao[i] 
    return nova_solucao
```

### 5. Função de Aceitação Probabilística:

A função `probabilidade_aceitacao(custo_atual, novo_custo, temperatura)` determina a probabilidade de aceitar a nova solução com base na diferença de custo entre a solução atual e a nova solução, e na temperatura do sistema. Se a nova solução for melhor, ela é aceita diretamente. Caso contrário, é aceita com uma certa probabilidade.

```python
def probabilidade_aceitacao(custo_atual, novo_custo, temperatura):
    if novo_custo < custo_atual:
        return 1.0  
    return math.exp((custo_atual - novo_custo) / temperatura) 
```

### 6. Algoritmo de Simulated Annealing:

A função `def caixeiro_viajante_sa(cidades, temperatura_inicial, taxa_resfriamento, iteracoes)` implementa o algoritmo Simulated Annealing. Ele começa com uma solução inicial aleatória e, a cada iteração, gera uma solução vizinha. Se a nova solução for melhor, ela é aceita. Se for pior, pode ser aceita com uma probabilidade baseada na temperatura. A temperatura diminui ao longo do tempo (cooling).

```python
def caixeiro_viajante_sa(cidades, temperatura_inicial, taxa_resfriamento, iteracoes):
    solucao_atual = gerar_solucao_inicial(len(cidades)) 
    custo_atual = calcular_distancia_total(solucao_atual, cidades) 
    melhor_solucao = solucao_atual[:]  
    menor_custo = custo_atual
    temperatura = temperatura_inicial 

    for _ in range(iteracoes):  
        nova_solucao = perturbar_solucao(solucao_atual)  
        novo_custo = calcular_distancia_total(nova_solucao, cidades)  

        if probabilidade_aceitacao(custo_atual, novo_custo, temperatura) > random.random():
            solucao_atual = nova_solucao 
            custo_atual = novo_custo  

            if custo_atual < menor_custo:
                melhor_solucao = solucao_atual[:]
                menor_custo = custo_atual

        temperatura *= taxa_resfriamento  

    return melhor_solucao, menor_custo
```

### 7. Geração de Cidades Aleatórias:

Uma instância de 10 cidades foi criada, cada uma com coordenadas aleatórias entre 0 e 100.

```python
numero_cidades = 10
cidades = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(numero_cidades)]
```

### 8. Execução do Algoritmo:

Definimos os parâmetros do algoritmo, como a temperatura inicial, a taxa de resfriamento e o número de iterações. O algoritmo é então executado para encontrar a melhor rota.

```python
temperatura_inicial = 1000  
taxa_resfriamento = 0.99 
iteracoes = 10000  

melhor_rota, menor_distancia = caixeiro_viajante_sa(cidades, temperatura_inicial, taxa_resfriamento, iteracoes)
```

### 9. Exibição dos Resultados:

Ao final, a melhor rota encontrada e a distância mínima obtida são exibidas.

```python
print(f"Melhor rota encontrada: {melhor_rota}")
print(f"Menor distância obtida: {menor_distancia:.2f}")
```
