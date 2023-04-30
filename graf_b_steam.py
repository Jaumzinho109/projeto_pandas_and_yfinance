import pandas as pd
import matplotlib.pyplot as plt

criticas = pd.read_csv(r'C:\Users\joaoh\OneDrive\Área de Trabalho\games-release-ALL.csv')
ordenado = criticas.sort_values('rating', ascending=False)
melhor_avaliado = ordenado.head(19)
jogo = melhor_avaliado['game']
avaliacao = melhor_avaliado['rating']
avaliacao_ordenada = avaliacao.sort_values(ascending=True)

fig, ax = plt.subplots(figsize=(18, 11))
ax.barh(jogo, avaliacao_ordenada, color = ['#C0C0C0', '#B0C4DE'])

ax.set_title('Melhores avaliados', fontsize=19)
ax.set_xlabel('Porcentagem de boas avaliações', fontsize=14)
ax.set_ylabel('Nome dos jogos', fontsize=14)

plt.show()