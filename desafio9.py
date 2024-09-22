import random
import math

# Função para calcular a distância entre duas cidades usando a fórmula da distância euclidiana
def calcular_distancia(cidade1, cidade2):
    return math.sqrt((cidade1[0] - cidade2[0])**2 + (cidade1[1] - cidade2[1])**2)

# Função que calcula a distância total de uma rota (solução)
def calcular_distancia_total(rota, cidades):
    distancia_total = 0
    for i in range(len(rota)):
        # Soma as distâncias entre cidades consecutivas
        distancia_total += calcular_distancia(cidades[rota[i]], cidades[rota[(i + 1) % len(rota)]])
    return distancia_total

# Gera uma solução inicial aleatória
def gerar_solucao_inicial(n):
    solucao = list(range(n))  # Lista com as cidades (0, 1, 2, ..., n-1)
    random.shuffle(solucao)   # Embaralha as cidades para criar uma rota inicial
    return solucao

# Perturba a solução (gera uma solução vizinha) trocando duas cidades aleatoriamente
def perturbar_solucao(solucao):
    nova_solucao = solucao[:]  # Copia a solução atual
    i, j = random.sample(range(len(solucao)), 2)  # Escolhe duas cidades aleatórias
    nova_solucao[i], nova_solucao[j] = nova_solucao[j], nova_solucao[i]  # Troca as cidades de posição
    return nova_solucao

# Função de aceitação probabilística baseada na temperatura
def probabilidade_aceitacao(custo_atual, novo_custo, temperatura):
    if novo_custo < custo_atual:
        return 1.0  # Se a nova solução for melhor, aceitamos diretamente
    return math.exp((custo_atual - novo_custo) / temperatura)  # Se for pior, aceitamos com uma certa probabilidade

# Algoritmo de Simulated Annealing para o problema do Caixeiro Viajante
def caixeiro_viajante_sa(cidades, temperatura_inicial, taxa_resfriamento, iteracoes):
    solucao_atual = gerar_solucao_inicial(len(cidades))  # Gera uma solução inicial
    custo_atual = calcular_distancia_total(solucao_atual, cidades)  # Calcula o custo da solução inicial
    melhor_solucao = solucao_atual[:]  # Inicialmente, a melhor solução é a atual
    menor_custo = custo_atual
    temperatura = temperatura_inicial  # Define a temperatura inicial

    for _ in range(iteracoes):  # Loop de iterações
        nova_solucao = perturbar_solucao(solucao_atual)  # Gera uma solução vizinha
        novo_custo = calcular_distancia_total(nova_solucao, cidades)  # Calcula o custo da nova solução

        # Se a nova solução for melhor ou for aceita pela função de aceitação, a adotamos
        if probabilidade_aceitacao(custo_atual, novo_custo, temperatura) > random.random():
            solucao_atual = nova_solucao  # Atualiza a solução atual
            custo_atual = novo_custo  # Atualiza o custo atual

            # Se a nova solução é a melhor que já encontramos, atualizamos a melhor solução
            if custo_atual < menor_custo:
                melhor_solucao = solucao_atual[:]
                menor_custo = custo_atual

        temperatura *= taxa_resfriamento  # Diminui a temperatura conforme a taxa de resfriamento

    return melhor_solucao, menor_custo  # Retorna a melhor solução e seu custo

# Criar uma instância com 10 cidades com coordenadas aleatórias
numero_cidades = 10
cidades = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(numero_cidades)]

# Definir os parâmetros do Simulated Annealing
temperatura_inicial = 1000  # Temperatura inicial
taxa_resfriamento = 0.99  # Taxa de resfriamento (cooling)
iteracoes = 10000  # Número de iterações

# Executar o algoritmo Simulated Annealing
melhor_rota, menor_distancia = caixeiro_viajante_sa(cidades, temperatura_inicial, taxa_resfriamento, iteracoes)

# Exibir os resultados
print(f"Melhor rota encontrada: {melhor_rota}")
print(f"Menor distância obtida: {menor_distancia:.2f}")
