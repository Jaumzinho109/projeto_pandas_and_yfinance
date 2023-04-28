import pandas as pd
import matplotlib.pyplot as plt
vendas = pd.read_csv(r'C:\Users\ALUNO\Desktop\best_selling_switch_games.csv')
filt = vendas[vendas['developer'] == 'Nintendo EPD']
filt = filt.sort_values('copies_sold', ascending = True)
titulo = filt['title']
copias_vend = filt['copies_sold']
labels = [titulo]
vals = [copias_vend]
fig, ax = plt.subplots(figsize =(15,8))
ax.barh(filt['title'], filt['copies_sold'])
plt.show()