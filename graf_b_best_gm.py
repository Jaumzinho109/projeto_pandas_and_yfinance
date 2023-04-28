import pandas as pd
import matplotlib.pyplot as plt
criticas = pd.read_csv(r'C:\Users\ALUNO\Desktop\games-release-ALL.csv')
ordenado = criticas.sort_values('rating', ascending = False)
melhor_avaliado = ordenado.head(20)
display(melhor_avaliado)