import json

# Carregar o arquivo JSON com os dados do faturamento
with open('dados.json', 'r') as file:
	fat_dia = json.load(file)
	
# Exibição dos dias e faturamentos
print("Faturamento do mês de Março:\n")

for item in fat_dia:
	print(item['dia'], ":", item['valor'])

# Cálculo e exibição dos valores ordenados pelo faturamento
fat_dia_ordenado = sorted(fat_dia, key=lambda x: x['valor'])

print("\nFaturamento do mês de Março ordenado:\n")

for item in fat_dia_ordenado:
	print(item['dia'], ":", item['valor'])

# Cálculo e exibição da média de faturamento
valores = [item['valor'] for item in fat_dia]
media = sum(valores) / len(valores)

print("\nA média de faturamento do mês de Março foi de:", round(media, 2))

# Cálculo e exibição do menor e do maior faturamento
max_item = max(fat_dia, key=lambda item: item['valor'])
min_item = min(fat_dia, key=lambda item: item['valor'])

print("\nMaior faturamento(", max_item['dia'], ":", max_item['valor'], ")")
print("Menor faturamento(", min_item['dia'], ":", min_item['valor'], ")")
