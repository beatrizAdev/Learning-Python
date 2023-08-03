# Preencher uma tupla com os 20 primeiros colocados da tabela do brasileirão, na ordem de colocação.
# Mostrar os 5 primeiros.
# Mostrar os últimos 4 da tabela.
# Os times em ordem alfabética.
# Em que posição está o time do São paulo.

time_brasileirao = ("Botafogo", "Flamengo", "Palmeiras", "Vasco", "Grêmio", "Fluminense", "Bragantino", "Athletico-PR",
                    "São Paulo", "Cuiabá", "Cruzeiro", "Fortaleza", "Internacional", "Atlético-MG", "Corinthians",
                    "Santos", "Goiás", "Bahia", "Coritiba", "América-MG")
posicao = time_brasileirao.index("São Paulo")
print(time_brasileirao)
print(time_brasileirao[0:5])
print(time_brasileirao[-5:])
print(sorted(time_brasileirao))
print(f"O São Paulo está na {posicao} posiçao")
