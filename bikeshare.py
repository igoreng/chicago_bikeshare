# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("assets/chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]
data_list_twenty = []
for line in data_list:
    dates = line
    data_list_twenty.append(dates)

print(data_list_twenty[:20])

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
gender_list = []
for line in data_list:
    gender = line[6]
    gender_list.append(gender)

print(gender_list[:20])


# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data, index):
    """
    Adiciona as colunas(features) de uma lista em outra lista, na mesma ordem.

    Argumentos:
        data: itera sobre as amostras para pegar o feature
        index: seleciona o índice desejado da lista de todos os dados

    Retorna:
        Uma lista de um dos features.
    """
    column_list = []
    for data in data_list:
        column = data[index]
        column_list.append(column)
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.
male = 0
female = 0

for line in gender_list:
    if line == "Male":
         male += 1
    elif line == "Female":
        female += 1
    else:
        male = male + 0
        female = female + 0

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função para isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    """
    Realiza a contagem dos gêneros feminino e masculino.

    Argumentos:
        data_list: nome da lista a ser iterada.

    Retorna:
        O número de pessoas do genêro feminino e masculino.
    """
    male = 0
    female = 0

    for line in gender_list:
        if line == "Male":
             male += 1
        elif line == "Female":
            female += 1
        else:
            male = male + 0
            female = female + 0

    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.
def most_popular_gender(data_list):
    """
    Determina qual gênero tem mais recorrência na lista (masculino ou feminino).

    Argumentos:
        data_list: nome da lista a ser iterada.

    Retorna:
        O gênero com mais recorrência na lista.

    """
    if male > female:
        answer = "Male"
    elif male < female:
        answer = "Female"
    else:
        answer = "Equal"

    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta
print("\nTAREFA 7: Verifique o gráfico!")
def count_user(data_list):
    """
    Realiza a contagem dos tipos de usuários: assinantes ou cliente ocasional.

    Argumentos:
        data_list: nome da lista a ser iterada.

    Retorna:
        O número de assinantes ou clientes ocasionais.

    """
    customer = 0
    subscriber = 0

    for line in user_list:
        if line == "Customer":
             customer += 1
        elif line == "Subscriber":
            subscriber += 1
        else:
            subscriber = subscriber + 0
            customer = customer + 0

    return [subscriber, customer]

user_list = column_to_list(data_list, -3)
types = ["Customer", "Subscriber"]
quantity = count_user(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipo')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipo')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Porque 'male + female' representa o número de homens e mulheres presentes na lista de dados, enquanto 'len(data_list)' representa o comprimento total de dados da lista. Ou seja, 'male + female' está contabilizando os dados da lista referentes ao gênero, já 'len(data_list)' contabiliza todos os dados presentes na lista."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)
def calculate_min(data_list):
    """
    Determina o tempo da viagem com menor duração.

    Argumentos:
        data_list: nome da lista a ser iterada.

    Retorna:
        O tempo de duração da menor viagem.

    """
    reference_value = int(data_list[0])
    for i in data_list:
        x = int(i)
        if x < int(reference_value):
            reference_value = x
    return reference_value

def calculate_max(data_list):
    """
    Determina o tempo da viagem com maior duração.

    Argumentos:
        data_list: nome da lista a ser iterada.

    Retorna:
        O tempo de duração da maior viagem.

    """
    reference_value = int(data_list[0])
    for i in data_list:
        x = int(i)
        if x > int(reference_value):
            reference_value = x
    return reference_value

def calculate_mean(data_list):
    """
        Determina a média do tempo de duração de uma viagem.

    Argumentos:
        data_list: nome da lista a ser iterada.

    Retorna:
        A média do tempo de duração de uma viagem.

    """
    sum = 0
    valide_values_list = []
    for i in data_list:
        x = int(i)
        valide_values_list.append(x)

    for x in valide_values_list:
        sum += x

    return round(sum/len(valide_values_list))

def calculate_median(data_list):
    """
    Determina a mediana do tempo de duração das viagens.

    Argumentos:
        data_list: nome da lista a ser iterada.

    Retorna:
        A mediana do tempo de duração das viagens.

    """
    valide_values_list = []
    for i in data_list:
        x = int(i)
        valide_values_list.append(x)

    valide_values_list = sorted(valide_values_list)

    if len(valide_values_list)%2 != 0:
        n = int((len(valide_values_list) + 1) / 2)
        median = valide_values_list[n]
    else:
        n = int((len(valide_values_list)/2) + 0.5)
        m = int((len(valide_values_list)/2) - 0.5)
        sum_items = valide_values_list[n] + valide_values_list[m]
        median = sum_items/2

    return median

min_trip = calculate_min(trip_duration_list)
max_trip = calculate_max(trip_duration_list)
mean_trip = calculate_mean(trip_duration_list)
median_trip = calculate_median(trip_duration_list)


print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
start_stations_list = column_to_list(data_list, -5)
start_stations = set(start_stations_list)

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
#      """
#      Função de exemplo com anotações.
#      Argumentos:
#          param1: O primeiro parâmetro.
#          param2: O segundo parâmetro.
#      Retorna:
#          Uma lista de valores x.
#      """

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

def count_items(column_list):
    item_types = []
    count_items = []
    for line in column_list:
        item_types.append(line)

    count_items = set(item_types)
    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------
