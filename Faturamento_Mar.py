import json

with open('faturamento_mar.json', 'r') as file:
    fat_dia = json.load(file)

print("Faturamento do mês de Março:\n")
for k, v in fat_dia.items():
    print(k, ":", v)

fat_dia_ordenado = sorted(fat_dia.items(), key=lambda x: x[1])

print("\nFaturamento do mês de Março ordenado:\n")
for k, v in fat_dia_ordenado:
    print(k, ":", v)
    
media=sum(int(v) for v in fat_dia.values()) / len(fat_dia)
print("\nA média de faturamento do mês de Março foi de:", round(media, 2))

maxi=max(fat_dia, key=lambda k: fat_dia[k])
mini=min(fat_dia, key=lambda k: fat_dia[k])

print("\nMaior faturamento(", maxi, ":", fat_dia[maxi], ")")
print("Menor faturamento(", mini, ":", fat_dia[mini], ")")
