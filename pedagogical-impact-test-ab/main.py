import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from statsmodels.stats.weightstats import ztest
'''
hipótese nula e alternativa
H0: A média das notas dos alunos na estratégia A é igual à média das notas dos alunos na B
H1: A média das notas na Estratégia B é maior do que a média das notas na A
'''
media_estrategia_A = 70
desvio_padrao_estrategia_A = 10

media_estrategia_B = 75
desvio_padrao_estrategia_B = 12

# gerando as amostras de notas para cada estratégia de ensino da nossa base
np.random.seed(0)  
amostra_estrategia_A = np.random.normal(loc=media_estrategia_A, scale=desvio_padrao_estrategia_A, size=50)
amostra_estrategia_B = np.random.normal(loc=media_estrategia_B, scale=desvio_padrao_estrategia_B, size=50)

print("Notas da Estratégia A:", amostra_estrategia_A[:5])
print("Notas da Estratégia B:", amostra_estrategia_B[:5])

print(f"\nMédia A: {amostra_estrategia_A.mean():.2f} | Variância A: {amostra_estrategia_A.var():.2f}")
print(f"Média B: {amostra_estrategia_B.mean():.2f} | Variância B: {amostra_estrategia_B.var():.2f}")
'''média da B 3.34 pontos acima, diferença pequena comparada a diferença nas variâncias
com a da B sendo um pouco menor (108 vs 126 - desempenho nesse grupo foi um pouco mais uniforme),
variâncias altas (acima de 100), indica notas muito dispersas'''

'''teste é unilateral à direita porque a hipótese alternativa busca especificamente um ganho (B > A),
em um teste bicaudal o que importa é se as médias são diferentes, olha pras duas caudas'''
z_score, p_value = ztest(amostra_estrategia_A, amostra_estrategia_B, alternative= 'smaller')

print(f"\n Resultados:")
print(f"Z score: {z_score:.4f}")
print(f"P-value: {p_value:.5f}")

alpha = 0.05
if p_value < alpha:
    print("Rejeita a Hipótese Nula. A diferença entre as estratégias é estatisticamente significativa.")
else:
    print("Não há evidências suficientes para rejeitar a Hipótese Nula.")
'''não rejeita a H0, pois P-valor de 0.06341 é maior que o nível de significância de de 0.05,
~6% de chance de observar os dados, diferença pode ser acaso na escolha dos alunos,
não dá para afirmar que a Estratégia B é melhor'''

x = np.linspace(-4, 4, 1000)
y = stats.norm.pdf(x, 0, 1)

plt.figure(figsize=(10, 5))
plt.plot(x, y, label='Distribuição Normal Padrão', color='black')

#pintar regiar rejeição e linha z calculado
z_critico = stats.norm.ppf(1- alpha)
plt.fill_between(x, y, where=(x >= z_critico), color='purple', alpha=0.3, label='Região de Rejeição')
plt.axvline(z_score, color='green', linestyle='--', linewidth=2, label=f'Z score: {z_score:.2f}')

plt.title('Distribuição da Estatística do Teste Z', fontsize=14)
plt.legend()
plt.show()
'''Z calculado (-1.53) à esquerda da distribuição e fora da região crítica, não há evidências para rejeitar a hipótese nula
Z negativo sugere que a média da amostra B não foi superior à da A'''